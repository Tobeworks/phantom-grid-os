"""
social.py — Phantom Grid social media asset generator
Reads release.json, builds a tile-generator config, and renders
square MP4s, reels, and carousel PNGs with Phantom Grid brand defaults.

Wraps: github.com/Tobeworks/instagram-tile-generator
"""

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from colorama import init, Fore, Style

init(autoreset=True)

# ── Phantom Grid brand defaults ───────────────────────────────────────────────
PG_ACCENT_COLOR    = "#CC2222"
PG_OVERLAY_COLOR   = "#0E0E0E"
PG_OVERLAY_OPACITY = 0.85
PG_FONT_COLOR      = "#ffffff"
PG_HEADLINE        = "PHANTOM GRID"
PG_CLIP_DURATION   = 30

# Path to the instagram-tile-generator
TILE_GENERATOR_PATH = Path("/Users/tobe/Sites/python/instagram-tile-generator")


def ok(msg):
    print(f"  {Fore.GREEN}✓{Style.RESET_ALL}  {msg}")

def info(msg):
    print(f"  {Fore.CYAN}→{Style.RESET_ALL}  {msg}")

def warn(msg):
    print(f"  {Fore.YELLOW}~{Style.RESET_ALL}  {msg}")

def fail(msg):
    print(f"  {Fore.RED}✗{Style.RESET_ALL}  {msg}")

def header(msg):
    print(f"\n{Fore.WHITE}{Style.BRIGHT}{msg}{Style.RESET_ALL}")
    print("─" * 50)


def find_cover(asset_path: Path) -> str | None:
    """Find any PNG in artwork/ folder."""
    artwork_path = asset_path / 'artwork'
    if not artwork_path.exists():
        return None
    for f in sorted(artwork_path.iterdir()):
        if f.suffix.lower() in {'.png', '.jpg', '.jpeg', '.tiff'}:
            return str(f)
    return None


def find_eurostile_font() -> str | None:
    """Search for Eurostile font on the system."""
    search_paths = [
        Path.home() / 'Library/Fonts',
        Path('/Library/Fonts'),
        Path('/System/Library/Fonts'),
    ]
    for base in search_paths:
        if base.exists():
            for f in base.rglob('*'):
                if 'eurostile' in f.name.lower() and f.suffix.lower() in {'.ttf', '.otf'}:
                    return str(f)
    return None


def generate_social(release_path: str, output_format: str = 'all',
                    clip_duration: int = PG_CLIP_DURATION, force: bool = False):
    path = Path(release_path)

    print(f"\n{Fore.RED}{Style.BRIGHT}PHANTOM GRID — SOCIAL GENERATOR{Style.RESET_ALL}")
    print(f"Target: {path.name}\n")

    # ── 1. Read release.json ──────────────────────────────────────────────────
    header("1. RELEASE DATA")

    json_path = path / 'release.json'
    if not json_path.exists():
        fail("release.json not found — run generate first")
        sys.exit(1)

    with open(json_path) as f:
        data = json.load(f)

    artist  = data.get('artist', 'PHANTOM GRID')
    title   = data.get('title', '')
    catalog = data.get('catalog', '')
    tracks  = data.get('tracks', [])

    ok(f"{catalog} — {artist} — {title}")
    ok(f"{len(tracks)} track(s)")

    # ── 2. Cover ──────────────────────────────────────────────────────────────
    header("2. ASSETS")

    cover = find_cover(path)
    if not cover:
        fail("No cover image found in artwork/")
        sys.exit(1)
    ok(f"Cover: {Path(cover).name}")

    # ── 3. Font ───────────────────────────────────────────────────────────────
    font_path = find_eurostile_font()
    if font_path:
        ok(f"Font: {Path(font_path).name}")
    else:
        warn("Eurostile not found — falling back to system font")

    # ── 4. Build tile-generator config.json ───────────────────────────────────
    header("3. BUILDING CONFIG")

    # Relative cover path for the tile generator (it expects path relative to data_dir)
    cover_rel = os.path.relpath(cover, path)

    tile_tracks = []
    for t in tracks:
        wav_file = t.get('file', '')
        if not wav_file:
            warn(f"Track {t.get('number')} has no file — skipping")
            continue

        tile_tracks.append({
            "audio":    wav_file,
            "image":    cover_rel,
            "headline": PG_HEADLINE,
            "title":    t.get('title', ''),
            "copy":     f"{catalog} — Phantom Grid",
            "start":    None,
            "accent_color":       None,
            "font_color":         None,
            "font":               None,
            "overlay_color":      None,
            "overlay_opacity":    None,
            "typewriter_headline": True,
            "typewriter_title":    True,
            "typewriter_copy":     None,
            "progress_bar_color": None
        })

    tile_config = {
        "ep_title":              f"{catalog}-{title}".lower().replace(' ', '-'),
        "clip_duration":         clip_duration,
        "accent_color":          PG_ACCENT_COLOR,
        "font_color":            PG_FONT_COLOR,
        "font":                  font_path,
        "format":                output_format,
        "overlay_color":         PG_OVERLAY_COLOR,
        "overlay_opacity":       PG_OVERLAY_OPACITY,
        "progress_bar":          True,
        "progress_bar_position": "top",
        "progress_bar_color":    PG_ACCENT_COLOR,
        "typewriter_headline":   True,
        "typewriter_title":      True,
        "typewriter_copy":       False,
        "tracks":                tile_tracks
    }

    # Write temp config.json into the asset folder (tile generator expects it there)
    config_path = path / '_social_config.json'
    with open(config_path, 'w') as f:
        json.dump(tile_config, f, indent=2)

    ok(f"Config written — {len(tile_tracks)} track(s), format: {output_format}")

    # ── 5. Run tile generator ─────────────────────────────────────────────────
    header("4. RENDERING")

    if not TILE_GENERATOR_PATH.exists():
        fail(f"instagram-tile-generator not found at {TILE_GENERATOR_PATH}")
        fail("Update TILE_GENERATOR_PATH in tools/commands/social.py")
        config_path.unlink(missing_ok=True)
        sys.exit(1)

    generator_script = TILE_GENERATOR_PATH / 'generate.py'
    generator_venv   = TILE_GENERATOR_PATH / 'venv' / 'bin' / 'python'

    python_bin = str(generator_venv) if generator_venv.exists() else 'python3'

    cmd = [
        python_bin,
        str(generator_script),
        str(path),
        '--config', str(config_path),
        '--format', output_format,
        '--duration', str(clip_duration),
    ]
    if force:
        cmd.append('--force')

    info(f"Running: {' '.join(cmd)}")
    print()

    result = subprocess.run(cmd, cwd=str(TILE_GENERATOR_PATH))

    # ── 6. Cleanup + Summary ──────────────────────────────────────────────────
    config_path.unlink(missing_ok=True)

    if result.returncode == 0:
        export_path = TILE_GENERATOR_PATH / 'export' / tile_config['ep_title']
        print(f"\n  {Fore.GREEN}{Style.BRIGHT}DONE — assets in:{Style.RESET_ALL}")
        print(f"  {export_path}\n")
    else:
        fail(f"Tile generator exited with code {result.returncode}")
        sys.exit(result.returncode)

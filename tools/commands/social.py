"""
social.py — Phantom Grid social media asset generator
Native implementation: no external tool dependencies.
Input:  release.json + audio/ + artwork/
Output: export/social/square/, export/social/reel/
"""

import json
import os
import subprocess
import sys
import re
from pathlib import Path

import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from colorama import init, Fore, Style

init(autoreset=True)

# ── Brand constants ────────────────────────────────────────────────────────────
ACCENT       = (204, 34, 34)          # #CC2222
ACCENT_ALPHA = (204, 34, 34, 200)
BG_COLOR     = (14, 14, 14)           # #0E0E0E
FONT_COLOR   = (220, 220, 220)
FPS          = 24
FADE_SECS    = 1.5

FORMATS = {
    "square":   (1080, 1080),
    "reel":     (1080, 1920),
}

AUDIO_EXTENSIONS = {'.wav', '.aif', '.aiff'}


def ok(msg):   print(f"  {Fore.GREEN}✓{Style.RESET_ALL}  {msg}")
def info(msg): print(f"  {Fore.CYAN}→{Style.RESET_ALL}  {msg}")
def warn(msg): print(f"  {Fore.YELLOW}~{Style.RESET_ALL}  {msg}")
def fail(msg): print(f"  {Fore.RED}✗{Style.RESET_ALL}  {msg}")
def header(msg):
    print(f"\n{Fore.WHITE}{Style.BRIGHT}{msg}{Style.RESET_ALL}")
    print("─" * 50)


# ── Font loader ────────────────────────────────────────────────────────────────
def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Try Eurostile variants, fall back to system fonts."""
    candidates = [
        "Eurostile MN Extended Bold.ttf",
        "EurostileMNExtended-Bold.ttf",
        "EurostileExtendedW01-Bd.ttf",
        "Eurostile-Bold.ttf",
        "Eurostile.ttf",
    ]
    search_dirs = [
        Path.home() / "Library/Fonts",
        Path("/Library/Fonts"),
        Path("/System/Library/Fonts"),
        Path("."),
    ]
    for name in candidates:
        for d in search_dirs:
            p = d / name
            if p.exists():
                return ImageFont.truetype(str(p), size)
    # fallback
    try:
        return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
    except Exception:
        return ImageFont.load_default()


# ── Audio helpers ──────────────────────────────────────────────────────────────
def load_audio_mono(path: Path, duration: float = 30.0, start: float = 0.0):
    """Load audio as mono float32 array, trimmed to duration."""
    data, sr = sf.read(str(path), dtype='float32', always_2d=True)
    mono = data.mean(axis=1)
    start_frame = int(start * sr)
    end_frame   = int((start + duration) * sr)
    mono = mono[start_frame:end_frame]
    return mono, sr


def compute_waveform_frames(mono: np.ndarray, sr: int,
                             fps: int, n_bars: int) -> list[np.ndarray]:
    """Return list of bar-height arrays (0.0–1.0) per video frame."""
    samples_per_frame = sr // fps
    n_frames = len(mono) // samples_per_frame
    frames = []
    for i in range(n_frames):
        chunk = mono[i * samples_per_frame:(i + 1) * samples_per_frame]
        # Split chunk into n_bars bins and compute RMS per bin
        bins = np.array_split(chunk, n_bars)
        heights = np.array([np.sqrt(np.mean(b ** 2)) for b in bins])
        # Normalize
        peak = heights.max()
        if peak > 0:
            heights = heights / peak
        frames.append(heights)
    return frames


# ── Image helpers ──────────────────────────────────────────────────────────────
def crop_cover(cover_path: Path, size: tuple[int, int]) -> Image.Image:
    """Load and center-crop cover to target size."""
    img = Image.open(cover_path).convert("RGB")
    tw, th = size
    iw, ih = img.size
    scale = max(tw / iw, th / ih)
    new_w = int(iw * scale)
    new_h = int(ih * scale)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - tw) // 2
    top  = (new_h - th) // 2
    return img.crop((left, top, left + tw, top + th))


def apply_overlay(base: Image.Image) -> Image.Image:
    """Dark gradient overlay from center to bottom."""
    w, h = base.size
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw    = ImageDraw.Draw(overlay)
    for y in range(h // 2, h):
        alpha = int(180 * ((y - h // 2) / (h // 2)) ** 1.5)
        draw.line([(0, y), (w, y)], fill=(14, 14, 14, alpha))
    result = base.convert("RGBA")
    result = Image.alpha_composite(result, overlay)
    return result.convert("RGB")


def draw_waveform(img: Image.Image, heights: np.ndarray,
                  w: int, h: int) -> Image.Image:
    """Draw LED-style waveform bars onto image."""
    draw   = ImageDraw.Draw(img)
    n_bars = len(heights)
    bar_w  = max(3, w // (n_bars * 2))
    gap    = bar_w
    total  = n_bars * (bar_w + gap)
    x_off  = (w - total) // 2
    max_h  = int(h * 0.25)
    cy     = int(h * 0.62)

    for i, ht in enumerate(heights):
        bh    = max(4, int(ht * max_h))
        x     = x_off + i * (bar_w + gap)
        y_top = cy - bh // 2
        y_bot = cy + bh // 2

        # Glow layer (wider, low alpha)
        glow_expand = bar_w + 4
        draw.rectangle(
            [x - 2, y_top - 2, x + glow_expand, y_bot + 2],
            fill=(204, 34, 34, 60)
        )
        # Main bar
        draw.rectangle([x, y_top, x + bar_w, y_bot], fill=ACCENT)

    return img


def draw_text(img: Image.Image, artist: str, title: str,
              w: int, h: int) -> Image.Image:
    """Draw artist + title text with Terminal Glow aesthetic."""
    draw = ImageDraw.Draw(img)

    font_title  = load_font(38)
    font_artist = load_font(22)

    # Artist — upper zone
    artist_text = artist.upper()
    bbox = draw.textbbox((0, 0), artist_text, font=font_artist)
    aw   = bbox[2] - bbox[0]
    ax   = (w - aw) // 2
    ay   = int(h * 0.76)
    draw.text((ax + 1, ay + 1), artist_text, font=font_artist,
              fill=(204, 34, 34, 120))
    draw.text((ax, ay), artist_text, font=font_artist, fill=ACCENT)

    # Title — below artist
    title_text = title.upper() + " _"
    bbox = draw.textbbox((0, 0), title_text, font=font_title)
    tw2  = bbox[2] - bbox[0]
    tx   = (w - tw2) // 2
    ty   = ay + 38
    draw.text((tx + 1, ty + 1), title_text, font=font_title,
              fill=(30, 30, 30))
    draw.text((tx, ty), title_text, font=font_title, fill=FONT_COLOR)

    return img


def add_grain(img: Image.Image, intensity: float = 0.03) -> Image.Image:
    """Add subtle film grain to the image."""
    arr   = np.array(img, dtype=np.float32)
    noise = np.random.normal(0, intensity * 255, arr.shape)
    arr   = np.clip(arr + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(arr)


# ── VHS post-processing ────────────────────────────────────────────────────────
def apply_vhs_effect(mp4_path: Path) -> Path:
    """Apply Phantom Grid terminal glow effect stack via FFmpeg. Replaces input."""
    tmp_path = mp4_path.with_suffix('.vhs_tmp.mp4')
    cmd = [
        'ffmpeg', '-i', str(mp4_path),
        '-vf',
        'drawgrid=x=0:y=0:width=0:height=4:color=black@0.2:thickness=2,'
        'noise=alls=14:allf=t+u,'
        'vignette=PI/4.5,'
        'colorchannelmixer=rr=1.05:gg=0.97:bb=0.95',
        '-c:v', 'libx264', '-crf', '18', '-preset', 'slow',
        '-c:a', 'copy',
        str(tmp_path), '-y'
    ]
    result = subprocess.run(cmd, capture_output=True)
    if result.returncode != 0:
        warn(f"VHS effect failed: {result.stderr.decode()[-200:]}")
        tmp_path.unlink(missing_ok=True)
        return mp4_path
    tmp_path.replace(mp4_path)
    ok(f"VHS effect applied → {mp4_path.name}")
    return mp4_path


# ── Main render ────────────────────────────────────────────────────────────────
DEFAULT_SOCIAL_CONFIG = {
    "defaults": {
        "duration":          30,
        "accent_color":      "#CC2222",
        "bg_color":          "#0E0E0E",
        "font_color":        "#DCDCDC",
        "n_bars":            40,
        "fade_secs":         1.5,
        "show_progress_bar": False,
        "vhs_effect":        True
    },
    "tracks": []
}


def hex_to_rgb(h: str) -> tuple:
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def init_social_config(path: Path, release_data: dict):
    """Write social.json skeleton from release.json tracks."""
    config = {
        "defaults": DEFAULT_SOCIAL_CONFIG["defaults"].copy(),
        "tracks": [
            {
                "number":         t.get("number"),
                "title_override": None,
                "start":          None,
                "duration":       None,
                "skip":           False
            }
            for t in release_data.get("tracks", [])
        ]
    }
    out = path / "social.json"
    with open(out, "w") as f:
        json.dump(config, f, indent=2)
    ok(f"social.json written → {out}")
    info("Edit start/duration/title_override per track, then run:")
    info(f"  ./tools/pg social {path}")


def load_social_config(path: Path) -> dict:
    """Load social.json if present, else return defaults."""
    cfg_path = path / "social.json"
    if cfg_path.exists():
        with open(cfg_path) as f:
            cfg = json.load(f)
        ok("social.json loaded")
        return cfg
    warn("No social.json found — using defaults. Run --init to create one.")
    return DEFAULT_SOCIAL_CONFIG.copy()


def render_track(audio_path: Path, cover_path: Path,
                 artist: str, title: str,
                 fmt: str, output_dir: Path,
                 duration: float = 30.0,
                 start_override: float = None,
                 n_bars: int = 40,
                 fade_secs: float = 1.5):
    """Render a single track to MP4."""
    from moviepy import ImageSequenceClip, AudioFileClip

    w, h = FORMATS[fmt]

    info(f"Loading audio: {audio_path.name}")
    try:
        total_dur = sf.info(str(audio_path)).duration
    except Exception:
        total_dur = duration

    # Use override if set, else center-start
    if start_override is not None:
        start = float(start_override)
    else:
        start = max(0.0, (total_dur - duration) / 2)

    mono, sr = load_audio_mono(audio_path, duration=duration, start=start)
    waveform_frames = compute_waveform_frames(mono, sr, FPS, n_bars)
    n_frames = len(waveform_frames)

    info(f"Rendering {n_frames} frames ({fmt} {w}×{h})…")

    base_cover = crop_cover(cover_path, (w, h))
    base_cover = apply_overlay(base_cover)

    frames_np = []
    for i, heights in enumerate(waveform_frames):
        frame = base_cover.copy().convert("RGBA")
        frame = draw_waveform(frame, heights, w, h)
        frame = draw_text(frame, artist, title, w, h)
        frame = add_grain(frame.convert("RGB"))
        frames_np.append(np.array(frame))

        if i % (FPS * 5) == 0:
            pct = int(i / n_frames * 100)
            info(f"  {pct}%")

    # Encode
    slug = re.sub(r'[^\w]+', '_', title.lower()).strip('_')
    out_path = output_dir / f"{slug}.mp4"
    output_dir.mkdir(parents=True, exist_ok=True)

    clip  = ImageSequenceClip(frames_np, fps=FPS)
    audio = AudioFileClip(str(audio_path)).subclipped(start, start + duration)
    audio = audio.with_effects([
        __import__('moviepy.audio.fx', fromlist=['AudioFadeIn']).AudioFadeIn(fade_secs),
        __import__('moviepy.audio.fx', fromlist=['AudioFadeOut']).AudioFadeOut(fade_secs),
    ])
    clip  = clip.with_audio(audio)
    clip.write_videofile(str(out_path), codec='libx264',
                         audio_codec='aac', logger=None)

    ok(f"→ {out_path}")
    return out_path


# ── Entry point ────────────────────────────────────────────────────────────────
def generate_social(release_path: str, fmt: str = "square",
                    duration: float = 30.0, init: bool = False):

    path = Path(release_path)

    print(f"\n{Fore.RED}{Style.BRIGHT}PHANTOM GRID — SOCIAL GENERATOR{Style.RESET_ALL}")
    print(f"Target: {path.name}\n")

    # ── Load release.json ──────────────────────────────────────────────────────
    header("1. RELEASE DATA")
    json_path = path / 'release.json'
    if not json_path.exists():
        fail("release.json not found — run generate first")
        sys.exit(1)
    with open(json_path) as f:
        data = json.load(f)

    artist = data.get('artist', 'UNKNOWN')
    title  = data.get('title',  'UNKNOWN')
    tracks = data.get('tracks', [])
    ok(f"{data.get('catalog','?')} — {artist} — {title}")
    ok(f"{len(tracks)} track(s)")

    # ── Init mode: write social.json and exit ──────────────────────────────────
    if init:
        header("2. INIT")
        init_social_config(path, data)
        return

    # ── Load social.json config ────────────────────────────────────────────────
    header("2. CONFIG")
    cfg      = load_social_config(path)
    defaults = cfg.get("defaults", DEFAULT_SOCIAL_CONFIG["defaults"])
    track_cfgs = {t["number"]: t for t in cfg.get("tracks", [])}

    # ── Find cover ─────────────────────────────────────────────────────────────
    header("3. ASSETS")
    artwork_dir = path / 'artwork'
    covers = sorted(artwork_dir.glob("*.png")) + sorted(artwork_dir.glob("*.jpg"))
    if not covers:
        fail("No cover image found in artwork/")
        sys.exit(1)
    cover_path = covers[0]
    ok(f"Cover: {cover_path.name}")

    # ── Render ─────────────────────────────────────────────────────────────────
    header("4. RENDERING")
    formats    = list(FORMATS.keys()) if fmt == "all" else [fmt]
    fade_secs  = float(defaults.get("fade_secs", 1.5))
    n_bars     = int(defaults.get("n_bars", 40))
    vhs_effect = bool(defaults.get("vhs_effect", True))
    audio_dir  = path / 'audio'

    for t in tracks:
        num      = t.get("number")
        tcfg     = track_cfgs.get(num, {})

        # Skip flag
        if tcfg.get("skip", False):
            warn(f"Track {num} — skipped (social.json)")
            continue

        wav_file = t.get('file')
        if not wav_file:
            warn(f"Track {num} — no file, skipping")
            continue

        audio_path = audio_dir / wav_file
        if not audio_path.exists():
            fail(f"{wav_file} not found")
            continue

        track_title    = tcfg.get("title_override") or t.get("title", title)
        track_duration = float(tcfg.get("duration") or defaults.get("duration", duration))
        track_start    = tcfg.get("start")  # None = auto center

        for f in formats:
            out_dir = path / 'export' / 'social' / f
            out_path = render_track(
                audio_path, cover_path, artist, track_title,
                f, out_dir,
                duration=track_duration,
                start_override=track_start,
                n_bars=n_bars,
                fade_secs=fade_secs
            )
            if vhs_effect:
                apply_vhs_effect(out_path)

    header("5. DONE")
    ok(f"Output: {path / 'export' / 'social'}")
    print()

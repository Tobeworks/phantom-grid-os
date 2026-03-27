"""
convert.py — Phantom Grid MP3 converter
WAV/AIFF → MP3 320kbps CBR with full ID3 tagging + embedded cover art.
Input:  release.json + audio/ + artwork/
Output: export/mp3/
"""

import json
import sys
import re
from pathlib import Path
from datetime import datetime

from colorama import init, Fore, Style
from pydub import AudioSegment
from mutagen.id3 import (
    ID3, TIT2, TPE1, TALB, TRCK, TDRC,
    TCON, TPUB, TXXX, APIC, ID3NoHeaderError
)
from mutagen.mp3 import MP3

init(autoreset=True)

AUDIO_EXTENSIONS = {'.wav', '.aif', '.aiff'}
BITRATE         = '320k'


def ok(msg):    print(f"  {Fore.GREEN}✓{Style.RESET_ALL}  {msg}")
def info(msg):  print(f"  {Fore.CYAN}→{Style.RESET_ALL}  {msg}")
def warn(msg):  print(f"  {Fore.YELLOW}~{Style.RESET_ALL}  {msg}")
def fail(msg):  print(f"  {Fore.RED}✗{Style.RESET_ALL}  {msg}")
def header(msg):
    print(f"\n{Fore.WHITE}{Style.BRIGHT}{msg}{Style.RESET_ALL}")
    print("─" * 50)


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '_', s)
    return s.strip('_')


def load_cover_bytes(artwork_dir: Path) -> tuple[bytes, str] | tuple[None, None]:
    """Return (bytes, mime_type) of first PNG/JPG in artwork/."""
    for ext, mime in [('*.png', 'image/png'), ('*.jpg', 'image/jpeg'),
                      ('*.jpeg', 'image/jpeg')]:
        covers = sorted(artwork_dir.glob(ext))
        if covers:
            return covers[0].read_bytes(), mime
    return None, None


def tag_mp3(mp3_path: Path, track: dict, release: dict,
            cover_bytes: bytes, cover_mime: str):
    """Write ID3 tags + cover to MP3 file."""
    try:
        tags = ID3(str(mp3_path))
    except ID3NoHeaderError:
        tags = ID3()

    year = ''
    rd = release.get('release_date', '')
    if rd and rd != 'YYYY-MM-DD':
        year = rd[:4]

    tags['TIT2'] = TIT2(encoding=3, text=track.get('title', ''))
    tags['TPE1'] = TPE1(encoding=3, text=release.get('artist', ''))
    tags['TALB'] = TALB(encoding=3, text=release.get('title', ''))
    tags['TRCK'] = TRCK(encoding=3,
                        text=f"{track.get('number', 1)}/{len(release.get('tracks', []))}")
    tags['TCON'] = TCON(encoding=3, text=release.get('genre', 'Electronic'))
    tags['TPUB'] = TPUB(encoding=3, text=release.get('label', 'Phantom Grid'))

    if year:
        tags['TDRC'] = TDRC(encoding=3, text=year)

    # Catalog number as custom TXXX frame
    catalog = release.get('catalog', '')
    if catalog:
        tags['TXXX:CATALOGNUMBER'] = TXXX(encoding=3,
                                           desc='CATALOGNUMBER',
                                           text=catalog)

    # Embedded cover art
    if cover_bytes:
        tags['APIC'] = APIC(
            encoding=0,
            mime=cover_mime,
            type=3,          # Cover (front)
            desc='Cover',
            data=cover_bytes
        )

    tags.save(str(mp3_path), v2_version=3)


def convert_release(release_path: str, force: bool = False):
    path = Path(release_path)

    print(f"\n{Fore.RED}{Style.BRIGHT}PHANTOM GRID — MP3 CONVERTER{Style.RESET_ALL}")
    print(f"Target: {path.name}\n")

    # ── Load release.json ──────────────────────────────────────────────────────
    header("1. RELEASE DATA")

    json_path = path / 'release.json'
    if not json_path.exists():
        fail("release.json not found — run generate first")
        sys.exit(1)

    with open(json_path) as f:
        release = json.load(f)

    artist  = release.get('artist', 'UNKNOWN')
    title   = release.get('title',  'UNKNOWN')
    catalog = release.get('catalog', 'PG-XXX')
    tracks  = release.get('tracks', [])

    ok(f"{catalog} — {artist} — {title}")
    ok(f"{len(tracks)} track(s)")

    # ── Cover ──────────────────────────────────────────────────────────────────
    header("2. COVER ART")

    artwork_dir = path / 'artwork'
    cover_bytes, cover_mime = load_cover_bytes(artwork_dir)

    if cover_bytes:
        ok(f"Cover loaded ({len(cover_bytes) // 1024} KB, {cover_mime})")
    else:
        warn("No cover found — MP3s will have no embedded artwork")

    # ── Convert ────────────────────────────────────────────────────────────────
    header("3. CONVERTING")

    audio_dir  = path / 'audio'
    output_dir = path / 'export' / 'mp3'
    output_dir.mkdir(parents=True, exist_ok=True)

    converted = 0
    skipped   = 0
    errors    = 0

    for track in tracks:
        src_file = track.get('file')
        if not src_file:
            warn(f"Track {track.get('number')} — no file defined, skipping")
            continue

        src_path = audio_dir / src_file
        if not src_path.exists():
            fail(f"Track {track.get('number')} — {src_file} not found")
            errors += 1
            continue

        # Output filename: 01_track-title.mp3
        num   = str(track.get('number', 0)).zfill(2)
        slug  = slugify(track.get('title', src_path.stem))
        out_name = f"{num}_{slug}.mp3"
        out_path = output_dir / out_name

        if out_path.exists() and not force:
            warn(f"Track {track.get('number')} — {out_name} exists, skipping (--force to overwrite)")
            skipped += 1
            continue

        info(f"Track {track.get('number')} — converting {src_file} → {out_name}")

        try:
            # Load source audio
            suffix = src_path.suffix.lower()
            if suffix == '.wav':
                audio = AudioSegment.from_wav(str(src_path))
            elif suffix in ('.aif', '.aiff'):
                audio = AudioSegment.from_aiff(str(src_path))
            else:
                audio = AudioSegment.from_file(str(src_path))

            # Export MP3 at 320kbps
            audio.export(str(out_path), format='mp3',
                         bitrate=BITRATE,
                         tags={
                             'artist': artist,
                             'title': track.get('title', ''),
                             'album': title,
                             'tracknumber': str(track.get('number', 1)),
                         })

            # Re-tag with full ID3 data + cover
            tag_mp3(out_path, track, release, cover_bytes, cover_mime)

            size_mb = out_path.stat().st_size / (1024 * 1024)
            ok(f"Track {track.get('number')} — {out_name} ({size_mb:.1f} MB)")
            converted += 1

        except Exception as e:
            fail(f"Track {track.get('number')} — conversion failed: {e}")
            errors += 1

    # ── Summary ────────────────────────────────────────────────────────────────
    header("4. SUMMARY")

    ok(f"{converted} track(s) converted → {output_dir}")
    if skipped:
        warn(f"{skipped} skipped (already exist)")
    if errors:
        fail(f"{errors} error(s)")

    print()

"""
push.py — Phantom Grid CDN uploader
Uploads MP3 previews + artwork to cdn.phantom-grid.de via SFTP.
Updates data/releases.json in the OS repo.

Input:  release.json + export/mp3/ + artwork/
Output: CDN upload + data/releases.json updated
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from colorama import init, Fore, Style

init(autoreset=True)


def ok(msg):     print(f"  {Fore.GREEN}✓{Style.RESET_ALL}  {msg}")
def info(msg):   print(f"  {Fore.CYAN}→{Style.RESET_ALL}  {msg}")
def warn(msg):   print(f"  {Fore.YELLOW}~{Style.RESET_ALL}  {msg}")
def fail(msg):   print(f"  {Fore.RED}✗{Style.RESET_ALL}  {msg}")
def header(msg):
    print(f"\n{Fore.WHITE}{Style.BRIGHT}{msg}{Style.RESET_ALL}")
    print("─" * 50)


def load_env() -> dict:
    """Load .env from OS repo root."""
    env_path = Path(__file__).parents[2] / '.env'
    if not env_path.exists():
        fail(f".env not found at {env_path}")
        fail("Copy .env.example to .env and fill in credentials.")
        sys.exit(1)

    env = {}
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, _, val = line.partition('=')
        env[key.strip()] = val.strip()
    return env


def sftp_connect(env: dict):
    """Return an open paramiko SFTP client. Supports key and password auth."""
    try:
        import paramiko
    except ImportError:
        fail("paramiko not installed — run: pip install paramiko")
        sys.exit(1)

    key_path = env.get('CDN_KEY_PATH', '')
    password  = env.get('CDN_PASSWORD', '')

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    connect_kwargs = dict(
        hostname=env['CDN_HOST'],
        port=int(env.get('CDN_PORT', 22)),
        username=env['CDN_USER'],
    )

    if key_path:
        key_path = os.path.expanduser(key_path)
        connect_kwargs['key_filename'] = key_path
        info(f"Auth: public key ({key_path})")
    elif password:
        connect_kwargs['password'] = password
        info("Auth: password")
    else:
        # Let paramiko try the SSH agent and ~/.ssh/id_* automatically
        info("Auth: SSH agent / default keys")

    ssh.connect(**connect_kwargs)
    return ssh.open_sftp(), ssh


def sftp_makedirs(sftp, remote_path: str):
    """Recursively create remote directories."""
    parts = remote_path.split('/')
    current = ''
    for part in parts:
        if not part:
            continue
        current = f"{current}/{part}"
        try:
            sftp.stat(current)
        except FileNotFoundError:
            sftp.mkdir(current)


def upload_file(sftp, local: Path, remote: str):
    """Upload a single file, show progress."""
    size_kb = local.stat().st_size // 1024
    info(f"  {local.name} ({size_kb} KB) → {remote}")
    sftp.put(str(local), remote)


def test_connection():
    """Test SFTP connection and permissions — no upload."""
    print(f"\n{Fore.RED}{Style.BRIGHT}PHANTOM GRID — SFTP CONNECTION TEST{Style.RESET_ALL}\n")

    header("1. CREDENTIALS")
    env = load_env()
    ok(f"Host:    {env['CDN_HOST']}")
    ok(f"Port:    {env.get('CDN_PORT', 22)}")
    ok(f"User:    {env['CDN_USER']}")
    ok(f"Base:    {env.get('CDN_BASE_PATH', '/releases')}")

    header("2. CONNECTING")
    try:
        sftp, ssh = sftp_connect(env)
        ok("SSH handshake successful")
    except Exception as e:
        fail(f"Connection failed: {e}")
        sys.exit(1)

    header("3. PERMISSIONS")
    cdn_base = env.get('CDN_BASE_PATH', '/releases')
    try:
        sftp.stat(cdn_base)
        ok(f"Base path exists: {cdn_base}")
    except FileNotFoundError:
        warn(f"Base path does not exist: {cdn_base} — will be created on push")

    # Write test
    test_file = f"{cdn_base}/.pg-test"
    try:
        import io
        sftp.putfo(io.BytesIO(b"phantom-grid-test"), test_file)
        sftp.remove(test_file)
        ok("Write + delete permissions OK")
    except Exception as e:
        fail(f"Write test failed: {e}")
        sftp.close(); ssh.close()
        sys.exit(1)

    # List remote
    try:
        entries = sftp.listdir(cdn_base)
        ok(f"Directory listing OK — {len(entries)} item(s) in {cdn_base}")
        for e in entries[:5]:
            info(f"  {e}")
        if len(entries) > 5:
            info(f"  ... and {len(entries) - 5} more")
    except Exception as e:
        warn(f"Could not list directory: {e}")

    sftp.close()
    ssh.close()

    header("RESULT")
    ok("SFTP connection fully operational")
    print()


def push_release(release_path: str, preview_only: bool = False):
    path = Path(release_path)

    print(f"\n{Fore.RED}{Style.BRIGHT}PHANTOM GRID — CDN PUSH{Style.RESET_ALL}")
    print(f"Release: {path.name}\n")

    # ── Load credentials ───────────────────────────────────────────────────────
    header("1. CREDENTIALS")
    env = load_env()
    cdn_base   = env.get('CDN_BASE_PATH', '/releases')
    cdn_public = env.get('CDN_PUBLIC_URL', 'https://cdn.phantom-grid.de')
    ok(f"CDN: {env['CDN_HOST']}")

    # ── Load release.json ──────────────────────────────────────────────────────
    header("2. RELEASE DATA")
    json_path = path / 'release.json'
    if not json_path.exists():
        fail("release.json not found — run ./pg generate first")
        sys.exit(1)

    with open(json_path) as f:
        data = json.load(f)

    catalog = data.get('catalog', path.name)
    artist  = data.get('artist', '')
    title   = data.get('title', '')
    ok(f"{catalog} — {artist} — {title}")

    # ── Resolve files to upload ────────────────────────────────────────────────
    header("3. ASSETS")

    mp3_dir     = path / 'export' / 'mp3'
    preview_dir = path / 'export' / 'preview'
    artwork_dir = path / 'artwork'

    mp3_files     = sorted(mp3_dir.glob('*.mp3'))     if mp3_dir.exists()     else []
    preview_files = sorted(preview_dir.glob('*.mp3')) if preview_dir.exists() else []
    cover_files   = (sorted(artwork_dir.glob('*.jpg')) +
                     sorted(artwork_dir.glob('*.png'))) if artwork_dir.exists() else []

    if not mp3_files and not preview_files:
        fail("No MP3s found — run ./pg convert first")
        sys.exit(1)

    audio_files = preview_files if (preview_only and preview_files) else mp3_files
    audio_label = "preview" if (preview_only and preview_files) else "full"

    ok(f"{len(audio_files)} audio file(s) [{audio_label}]")
    ok(f"{len(cover_files)} artwork file(s)")

    # ── SFTP connect ───────────────────────────────────────────────────────────
    header("4. CONNECTING")
    sftp, ssh = sftp_connect(env)
    ok(f"Connected to {env['CDN_HOST']}")

    # ── Upload ─────────────────────────────────────────────────────────────────
    header("5. UPLOADING")
    slug         = path.name                          # e.g. pg-001-artist-title
    remote_base  = f"{cdn_base}/{slug}"
    remote_audio = f"{remote_base}/audio"
    remote_art   = f"{remote_base}/artwork"

    sftp_makedirs(sftp, remote_audio)
    sftp_makedirs(sftp, remote_art)

    cdn_tracks = []
    for mp3 in audio_files:
        remote_path = f"{remote_audio}/{mp3.name}"
        upload_file(sftp, mp3, remote_path)
        cdn_tracks.append({
            "file":     mp3.name,
            "url":      f"{cdn_public}/releases/{slug}/audio/{mp3.name}",
        })
        ok(f"✓ {mp3.name}")

    cdn_cover = None
    for cover in cover_files[:1]:
        remote_path = f"{remote_art}/{cover.name}"
        upload_file(sftp, cover, remote_path)
        cdn_cover = f"{cdn_public}/releases/{slug}/artwork/{cover.name}"
        ok(f"✓ {cover.name}")

    sftp.close()
    ssh.close()

    # ── Update data/releases.json ──────────────────────────────────────────────
    header("6. UPDATING releases.json")
    repo_root    = Path(__file__).parents[2]
    releases_path = repo_root / 'data' / 'releases.json'

    with open(releases_path) as f:
        releases_data = json.load(f)

    # Build release entry
    entry = {
        "catalog":    catalog,
        "artist":     artist,
        "title":      title,
        "format":     data.get('format', ''),
        "year":       data.get('year', ''),
        "genre":      data.get('genre', ''),
        "cover":      cdn_cover,
        "bandcamp":   data.get('bandcamp_url', ''),
        "tracks":     [],
        "pushed_at":  datetime.now(timezone.utc).isoformat(),
    }

    # Merge track metadata
    release_tracks = data.get('tracks', [])
    for i, t in enumerate(release_tracks):
        cdn_t = cdn_tracks[i] if i < len(cdn_tracks) else {}
        entry["tracks"].append({
            "number":  t.get('number'),
            "title":   t.get('title', ''),
            "bpm":     t.get('bpm', ''),
            "key":     t.get('key', ''),
            "runtime": t.get('runtime', ''),
            "file":    cdn_t.get('file', ''),
            "url":     cdn_t.get('url', ''),
        })

    # Update or insert
    existing = [r for r in releases_data['releases'] if r['catalog'] != catalog]
    releases_data['releases'] = [entry] + existing   # newest first
    releases_data['_meta']['generated'] = datetime.now(timezone.utc).isoformat()

    with open(releases_path, 'w') as f:
        json.dump(releases_data, f, indent=2)

    ok(f"releases.json updated — {len(releases_data['releases'])} release(s)")

    header("7. DONE")
    ok(f"CDN: {cdn_public}/releases/{slug}/")
    info("Next: commit data/releases.json, then push OS repo")
    info("  git add data/releases.json && git commit -m 'release(catalog): push to CDN'")
    print()

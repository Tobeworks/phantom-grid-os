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


def ftp_connect(env: dict):
    """Return an open FTP or FTPS client."""
    import ftplib
    host     = env['CDN_HOST']
    port     = int(env.get('CDN_PORT', 21))
    user     = env['CDN_USER']
    password = env.get('CDN_PASSWORD', '')
    protocol = env.get('CDN_PROTOCOL', 'ftp').lower()

    if protocol == 'ftps':
        ftp = ftplib.FTP_TLS()
        info("Protocol: FTPS (explicit TLS)")
    else:
        ftp = ftplib.FTP()
        info("Protocol: FTP")

    ftp.connect(host, port, timeout=10)
    ftp.login(user, password)

    if protocol == 'ftps':
        ftp.prot_p()  # switch to encrypted data channel

    return ftp


def sftp_connect(env: dict):
    """Return an open paramiko SFTP client. Supports key and password auth."""
    try:
        import paramiko
    except ImportError:
        fail("paramiko not installed — run: pip install paramiko")
        sys.exit(1)

    key_path = env.get('CDN_KEY_PATH', '')
    password = env.get('CDN_PASSWORD', '')

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
        info("Auth: SSH agent / default keys")

    ssh.connect(**connect_kwargs)
    return ssh.open_sftp(), ssh


def get_protocol(env: dict) -> str:
    return env.get('CDN_PROTOCOL', 'sftp').lower()


def ftp_makedirs(ftp, remote_path: str):
    """Recursively create remote directories via FTP."""
    parts = [p for p in remote_path.split('/') if p]
    current = ''
    for part in parts:
        current = f"{current}/{part}"
        try:
            ftp.cwd(current)
        except Exception:
            ftp.mkd(current)


def sftp_makedirs(sftp, remote_path: str):
    """Recursively create remote directories via SFTP."""
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


def upload_file(client, local: Path, remote: str, client_type: str):
    """Upload a single file via FTP or SFTP."""
    import io
    size_kb = local.stat().st_size // 1024
    info(f"  {local.name} ({size_kb} KB) → {remote}")
    if client_type == 'sftp':
        client.put(str(local), remote)
    else:
        with open(local, 'rb') as f:
            client.storbinary(f"STOR {remote}", f)


def test_connection():
    """Test FTP/SFTP connection and permissions — no upload."""
    print(f"\n{Fore.RED}{Style.BRIGHT}PHANTOM GRID — CONNECTION TEST{Style.RESET_ALL}\n")

    header("1. CREDENTIALS")
    env      = load_env()
    protocol = get_protocol(env)
    cdn_base = env.get('CDN_BASE_PATH', '/releases')
    ok(f"Protocol: {protocol.upper()}")
    ok(f"Host:     {env['CDN_HOST']}")
    ok(f"Port:     {env.get('CDN_PORT', 21 if protocol != 'sftp' else 22)}")
    ok(f"User:     {env['CDN_USER']}")
    ok(f"Base:     {cdn_base}")

    header("2. CONNECTING")
    try:
        if protocol == 'sftp':
            client, ssh = sftp_connect(env)
            client_type = 'sftp'
        else:
            client = ftp_connect(env)
            client_type = 'ftp'
            ssh = None
        ok("Connected successfully")
    except Exception as e:
        fail(f"Connection failed: {e}")
        sys.exit(1)

    header("3. PERMISSIONS")
    import io
    test_file = f"{cdn_base}/.pg-test"

    try:
        if client_type == 'sftp':
            try:
                client.stat(cdn_base)
                ok(f"Base path exists: {cdn_base}")
            except FileNotFoundError:
                warn(f"Base path not found: {cdn_base} — will be created on push")
            client.putfo(io.BytesIO(b"phantom-grid-test"), test_file)
            client.remove(test_file)
            entries = client.listdir(cdn_base)
        else:
            try:
                client.cwd(cdn_base)
                ok(f"Base path exists: {cdn_base}")
            except Exception:
                warn(f"Base path not found: {cdn_base} — will be created on push")
                client.cwd('/')
            client.storbinary(f"STOR {test_file}", io.BytesIO(b"phantom-grid-test"))
            client.delete(test_file)
            entries = client.nlst(cdn_base)

        ok("Write + delete permissions OK")
        ok(f"Directory listing OK — {len(entries)} item(s)")
        for e in entries[:5]:
            info(f"  {e}")
        if len(entries) > 5:
            info(f"  ... and {len(entries) - 5} more")

    except Exception as e:
        fail(f"Permission test failed: {e}")
        if client_type == 'sftp':
            client.close(); ssh.close()
        else:
            client.quit()
        sys.exit(1)

    if client_type == 'sftp':
        client.close(); ssh.close()
    else:
        client.quit()

    header("RESULT")
    ok(f"{protocol.upper()} connection fully operational")
    print()


def push_release(release_path: str, preview_only: bool = False):
    path = Path(release_path)

    print(f"\n{Fore.RED}{Style.BRIGHT}PHANTOM GRID — CDN PUSH{Style.RESET_ALL}")
    print(f"Release: {path.name}\n")

    # ── Load credentials ───────────────────────────────────────────────────────
    header("1. CREDENTIALS")
    env = load_env()
    cdn_base   = env.get('CDN_BASE_PATH', '/releases')
    cdn_public = env.get('CDN_PUBLIC_URL')
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

    # ── Connect ────────────────────────────────────────────────────────────────
    header("4. CONNECTING")
    protocol    = get_protocol(env)
    client_type = protocol if protocol in ('sftp',) else 'ftp'
    ssh         = None

    try:
        if client_type == 'sftp':
            client, ssh = sftp_connect(env)
        else:
            client = ftp_connect(env)
        ok(f"Connected via {protocol.upper()} to {env['CDN_HOST']}")
    except Exception as e:
        fail(f"Connection failed: {e}")
        sys.exit(1)

    # ── Upload ─────────────────────────────────────────────────────────────────
    header("5. UPLOADING")
    slug         = path.name
    remote_base  = f"{cdn_base}/{slug}"
    remote_audio = f"{remote_base}/audio"
    remote_art   = f"{remote_base}/artwork"

    if client_type == 'sftp':
        sftp_makedirs(client, remote_audio)
        sftp_makedirs(client, remote_art)
    else:
        ftp_makedirs(client, remote_audio)
        ftp_makedirs(client, remote_art)

    cdn_tracks = []
    for mp3 in audio_files:
        remote_path = f"{remote_audio}/{mp3.name}"
        upload_file(client, mp3, remote_path, client_type)
        cdn_tracks.append({
            "file": mp3.name,
            "url":  f"{cdn_public}/releases/{slug}/audio/{mp3.name}",
        })
        ok(f"✓ {mp3.name}")

    cdn_cover = None
    for cover in cover_files[:1]:
        remote_path = f"{remote_art}/{cover.name}"
        upload_file(client, cover, remote_path, client_type)
        cdn_cover = f"{cdn_public}/releases/{slug}/artwork/{cover.name}"
        ok(f"✓ {cover.name}")

    if client_type == 'sftp':
        client.close()
        ssh.close()
    else:
        client.quit()

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

# Phantom Grid Tools

The `tools/` folder is the operational layer of the Phantom Grid OS.
A CLI that takes a release asset folder from raw audio to validated release data and social media exports.

---

## Setup

Run once after cloning:

```bash
bash tools/setup.sh
```

Creates a Python venv in `tools/venv/` and installs all dependencies.

---

## Usage

```bash
./tools/pg <command> <release-folder-path> [options]
```

All commands take an absolute or relative path to a release asset folder.
Release asset folders live in `phantom-grid-assets/` — outside this repo.

---

## Commands

### `generate`

Scans `audio/` for WAV/AIFF files and writes a pre-filled `release.json`.
Preserves existing manual fields if `release.json` already exists.

```bash
./tools/pg generate ../phantom-grid-assets/pg-001-input-null-vector-field-signals
```

**What it detects automatically:**
- Track filenames → title slugs
- Duration, sample rate, bit depth per file
- Track numbering from filename prefix

**What requires manual input after generation:**
- `artist`, `title`, `release_date`
- Per-track: `title` (human-readable), `duration` (confirm)

---

### `validate`

Validates a release asset folder against the Phantom Grid schema.

```bash
./tools/pg validate ../phantom-grid-assets/pg-001-input-null-vector-field-signals
./tools/pg validate ../phantom-grid-assets/pg-001-... --generate-md
```

**Checks:**
- `release.json` is valid and all required fields are populated
- Each track's audio file exists in `audio/`
- At least one PNG or JPG exists in `artwork/`
- Cover resolution ≥ 3000×3000px

**`--generate-md`** writes a `release_draft.md` to the asset folder on success.

---

### `social`

Renders social media video assets (MP4) from release audio and cover art.
Native implementation — no external tool dependencies.

**Step 1 — Initialize config (run once per release):**

```bash
./tools/pg social ../phantom-grid-assets/pg-001-... --init
```

Writes `social.json` to the asset folder with defaults and one entry per track.

**Step 2 — Edit `social.json`:**

```json
{
  "defaults": {
    "duration": 30,
    "accent_color": "#CC2222",
    "bg_color": "#0E0E0E",
    "font_color": "#DCDCDC",
    "n_bars": 40,
    "fade_secs": 1.5,
    "show_progress_bar": false
  },
  "tracks": [
    {
      "number": 1,
      "title_override": null,
      "start": null,
      "duration": null,
      "skip": false
    }
  ]
}
```

| Field | Description |
|---|---|
| `duration` | Clip length in seconds (default: 30) |
| `accent_color` | Waveform bar color (default: `#CC2222`) |
| `n_bars` | Number of waveform bars (default: 40) |
| `fade_secs` | Audio fade in/out duration |
| `title_override` | Replace track title in video text |
| `start` | Start position in seconds (`null` = auto center) |
| `skip` | Set `true` to exclude a track from rendering |

**Step 3 — Render:**

```bash
./tools/pg social ../phantom-grid-assets/pg-001-... --format square
./tools/pg social ../phantom-grid-assets/pg-001-... --format reel
./tools/pg social ../phantom-grid-assets/pg-001-... --format all
./tools/pg social ../phantom-grid-assets/pg-001-... --duration 45
```

**Output:**
```
phantom-grid-assets/pg-001-.../
└── social/
    ├── square/    ← 1080×1080 MP4 (feed)
    └── reel/      ← 1080×1920 MP4 (stories/reels)
```

---

## Asset Folder Structure

```
phantom-grid-assets/
└── pg-001-input-null-vector-field-signals/
    ├── audio/
    │   ├── 01_track_title.wav        (preferred naming)
    │   └── Artist - Title.wav        (also accepted)
    ├── artwork/
    │   └── cover.png                 (min. 3000×3000px)
    ├── release.json                  ← source of truth
    ├── social.json                   ← social render config
    └── social/
        ├── square/
        └── reel/
```

---

## Coming

| Command | Description |
|---|---|
| `push` | Push release to Bandcamp via API |
| `promo` | Generate promo text from release.json via Claude |


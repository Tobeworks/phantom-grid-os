# PHANTOM GRID — SITE LAYOUT SPEC
## Briefing für den Astro Build

Stack: Astro + Tailwind CSS
Basis: HTML Prototype (stitch_input_null_landing_page) — übernehmen was stimmt, korrigieren was nicht stimmt.

---

## TYPOGRAPHIE

**Primär:** Eurostile / Eurostile Extended — Adobe Fonts / Typekit
**Data:** Inter — Google Fonts
Space Grotesk aus dem Prototype wird vollständig ersetzt.

```css
/* Eurostile via Adobe Fonts */
font-family: 'eurostile', sans-serif;
font-family: 'eurostile-extended', sans-serif; /* Hero only */
```

---

## SEITENSTRUKTUR

```
1. HEADER        — fixed, transparent → #0E0E0E on scroll
2. HERO          — fullscreen, pixel-grid bg, concentric squares
3. LATEST_SIGNALS — Bento Grid, aktuelle Releases
4. TRANSMISSION  — Terminal log + Waveform panel
5. JOIN_THE_GRID — Newsletter / Zugangscode
6. FOOTER
```

---

## 1. HEADER

```
[PHANTOM_GRID]          [RELEASES] [ARCHIVE] [ABOUT]     [●]
```

- Logo links: `PHANTOM_GRID` in Eurostile Extended Bold, Dirty Red, mit Bloom
- Navigation: 3 Items — RELEASES / ARCHIVE / GRID_MESSAGES
- Rechts: Status-Indikator `●` pulsierend in `#CC2222` — zeigt "System aktiv"
- Kein Burger-Menu Desktop. Mobile: Bottom Nav Bar (aus Prototype übernehmen)
- `border: none` — Trennung durch Hintergrundfarbe

---

## 2. HERO

Fullscreen. Pixel-Grid Hintergrund (`radial-gradient`, 24px × 24px, Dirty Red 15% opacity).

**Konzentrische Quadrate** (aus Prototype übernehmen, angepasst):
```
□ 300px  border: primary-container/30   animate-pulse
□ 500px  border: primary-container/20   rotate-45
□ 700px  border: primary-container/10   -rotate-12
□ 900px  border: primary-container/5    rotate-90
```

**Zentrierter Text:**
```
[SYSTEM_INITIALIZED // BOOT_SEQUENCE_COMPLETE]   ← 10px, tracking 0.5em, Dirty Red

PHANTOM_GRID                                      ← Eurostile Extended, 9xl, Black
                                                    drop-shadow: CC2222 0.4 opacity

[ENTER_VOID]  [LATEST_SIGNALS]                   ← Primary + Ghost Button
```

**Bottom Left — Koordinaten (korrigiert):**
```
ORIGIN:    CYBERSPACE
LINEAGE:   DETROIT / FRANKFURT
STATUS:    TRANSMITTING
```
*Kein geografisches lat/long mehr.*

---

## 3. LATEST_SIGNALS

`max-w-7xl`, 3-Column Bento Grid.

**Section Header:**
```
LATEST_SIGNALS                    STREAM_BUFFER: ACTIVE
─────────────────────────────────────────────────────── ← border-bottom, primary-container/20
```

**Release Card:**
```
┌────────────────────────┐
│  [Cover Art 1:1]       │  ← grayscale → color on hover
│  ▶ (on hover)          │
├────────────────────────┤
│  ARTIST: INPUT_NULL    │  ← 10px, Eurostile, Dirty Red, tracking 0.5em
│  VECTOR_FIELD_SIGNALS  │  ← Eurostile Bold, 20px
│                        │
│  BPM: —    KEY: —      │  ← 10px, opacity 50%
└────────────────────────┘
```

**Slot 3 (Placeholder bis zweites Release):**
```
┌────────────────────────┐
│         📡             │
│  INCOMING_TRANSMISSION │
│  SIGNAL PENDING...     │
│                        │
│  [SUBSCRIBE_TO_GRID]   │
└────────────────────────┘
```

---

## 4. TRANSMISSION PANEL

2-Column, `bg-surface-container-low`.

**Links — Waveform:**
```
● WAVE_FORM_ANALYSIS

┌──────────────────────────────────┐
│  [SVG Waveform in #CC2222]       │  ← aus Prototype übernehmen
└──────────────────────────────────┘

FREQ: —    AMP: —    PHASE: —
```

**Rechts — Terminal Log:**
```
CORE_SYSTEM_STATUS
──────────────────────────────

GRID_STABILITY   ████████████  NOMINAL
RELEASES_ACTIVE  ██░░░░░░░░░░  PG-001

┌──────────────────────────────┐
│ > PHANTOM_GRID_OS v0.0.5     │
│ > PG-001: VECTOR_FIELD...    │
│ > TRANSMISSION: ACTIVE       │
│ > ENCRYPTION_KEY: [REDACTED] │
│ > STATUS: OPTIMAL            │
│ _                            │  ← animate-pulse cursor
└──────────────────────────────┘
```

*Border-left: 4px solid #CC2222 auf dem rechten Panel.*

---

## 5. JOIN_THE_GRID

Zentriert, `max-w-3xl`.

```
┌────────────────────────────────────┐
│  LEVEL 3 ENCRYPTION REQUIRED       │  ← border: primary-container/30
└────────────────────────────────────┘

JOIN_THE_GRID

Gain priority access to unreleased signals and transmission logs.

[IDENT_TOKEN@SYSTEM.COM_______][REQUEST_ACCESS]
```

*Email Input + Primary Button, flush (kein gap), exakt aus Prototype.*

---

## 6. FOOTER

```
PHANTOM_GRID                    RELEASES  ARCHIVE  GRID_MESSAGES
© PHANTOM_GRID 2026
CYBERSPACE / DETROIT
```

- `border-top: primary-container/10`
- Copyright: `© PHANTOM_GRID 2026 — CYBERSPACE / DETROIT` — kein "©1982"
- Kein Status-String der nicht stimmt

---

## ASTRO KOMPONENTEN-STRUKTUR

```
src/
├── layouts/
│   └── BaseLayout.astro       ← Scanline overlay, fonts, tailwind config
├── pages/
│   └── index.astro
├── components/
│   ├── Header.astro
│   ├── Hero.astro
│   ├── LatestSignals.astro
│   ├── ReleaseCard.astro
│   ├── TransmissionPanel.astro
│   ├── JoinTheGrid.astro
│   └── Footer.astro
└── styles/
    └── global.css             ← scanline, terminal-glow, bloom-red, pixel-grid
```

---

## WAS AUS DEM PROTOTYPE DIREKT ÜBERNOMMEN WIRD

- Tailwind Config (alle Color Tokens) ✓
- Scanline Overlay CSS ✓
- `.terminal-glow`, `.bloom-red`, `.glass-panel`, `.pixel-grid` ✓
- Konzentrische Quadrate im Hero ✓
- Waveform SVG ✓
- Bottom Mobile Nav ✓
- Alle SNAKE_CASE Labels und Terminologie ✓

## WAS GEÄNDERT WIRD

- Space Grotesk → Eurostile
- Koordinaten: lat/long → CYBERSPACE / DETROIT / FRANKFURT
- Footer Copyright und Claim
- Inhalte: echte Release-Daten (PG-001)
- Navigation: vereinfacht

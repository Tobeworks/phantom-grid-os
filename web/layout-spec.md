# PHANTOM GRID — SITE LAYOUT SPEC
## Briefing for the Astro Build

Stack: Astro + Tailwind CSS
Base: HTML Prototype (stitch_input_null_landing_page) — carry over what works, correct what doesn't.

---

## TYPOGRAPHY

**Primary:** Eurostile / Eurostile Extended — Adobe Fonts / Typekit
**Data:** Inter — Google Fonts
Space Grotesk from the prototype is replaced entirely.

```css
/* Eurostile via Adobe Fonts */
font-family: 'eurostile', sans-serif;
font-family: 'eurostile-extended', sans-serif; /* Hero only */
```

---

## PAGE STRUCTURE

```
1. HEADER         — fixed, transparent → #0E0E0E on scroll
2. HERO           — fullscreen, pixel-grid bg, concentric squares
3. LATEST_SIGNALS — Bento Grid, current releases
4. TRANSMISSION   — Terminal log + Waveform panel
5. JOIN_THE_GRID  — Newsletter / access code
6. FOOTER
```

---

## 1. HEADER

```
[PHANTOM_GRID]          [RELEASES] [ARCHIVE] [ABOUT]     [●]
```

- Logo left: `PHANTOM_GRID` in Eurostile Extended Bold, Dirty Red, with Bloom
- Navigation: 3 items — RELEASES / ARCHIVE / GRID_MESSAGES
- Right: status indicator `●` pulsing in `#CC2222` — signals "system active"
- No burger menu on desktop. Mobile: Bottom Nav Bar (carry over from prototype)
- `border: none` — separation through background color only

---

## 2. HERO

Fullscreen. Pixel-Grid background (`radial-gradient`, 24px × 24px, Dirty Red 15% opacity).

**Concentric squares** (carry over from prototype, adjusted):
```
□ 300px  border: primary-container/30   animate-pulse
□ 500px  border: primary-container/20   rotate-45
□ 700px  border: primary-container/10   -rotate-12
□ 900px  border: primary-container/5    rotate-90
```

**Centered text:**
```
[SYSTEM_INITIALIZED // BOOT_SEQUENCE_COMPLETE]   ← 10px, tracking 0.5em, Dirty Red

PHANTOM_GRID                                      ← Eurostile Extended, 9xl, Black
                                                    drop-shadow: CC2222 0.4 opacity

[ENTER_VOID]  [LATEST_SIGNALS]                   ← Primary + Ghost Button
```

**Bottom left — coordinates:**
```
ORIGIN:    CYBERSPACE
LINEAGE:   DETROIT / FRANKFURT
STATUS:    TRANSMITTING
```
*No geographic lat/long.*

---

## 3. LATEST_SIGNALS

`max-w-7xl`, 3-column Bento Grid.

**Section header:**
```
LATEST_SIGNALS                    STREAM_BUFFER: ACTIVE
─────────────────────────────────────────────────────── ← border-bottom, primary-container/20
```

**Release card:**
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

**Slot 3 (placeholder until second release):**
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

2-column, `bg-surface-container-low`.

**Left — Waveform:**
```
● WAVE_FORM_ANALYSIS

┌──────────────────────────────────┐
│  [SVG Waveform in #CC2222]       │  ← carry over from prototype
└──────────────────────────────────┘

FREQ: —    AMP: —    PHASE: —
```

**Right — Terminal log:**
```
CORE_SYSTEM_STATUS
──────────────────────────────

GRID_STABILITY   ████████████  NOMINAL
RELEASES_ACTIVE  ██░░░░░░░░░░  PG-001

┌──────────────────────────────┐
│ > PHANTOM_GRID_OS v0.1.3     │
│ > PG-001: VECTOR_FIELD...    │
│ > TRANSMISSION: ACTIVE       │
│ > ENCRYPTION_KEY: [REDACTED] │
│ > STATUS: OPTIMAL            │
│ _                            │  ← animate-pulse cursor
└──────────────────────────────┘
```

*Border-left: 4px solid #CC2222 on the right panel.*

---

## 5. JOIN_THE_GRID

Centered, `max-w-3xl`.

```
┌────────────────────────────────────┐
│  LEVEL 3 ENCRYPTION REQUIRED       │  ← border: primary-container/30
└────────────────────────────────────┘

JOIN_THE_GRID

Gain priority access to unreleased signals and transmission logs.

[IDENT_TOKEN@SYSTEM.COM_______][REQUEST_ACCESS]
```

*Email input + Primary Button, flush (no gap), exact carry-over from prototype.*

---

## 6. FOOTER

```
PHANTOM_GRID                    RELEASES  ARCHIVE  GRID_MESSAGES
© PHANTOM_GRID 2026
CYBERSPACE / DETROIT
```

- `border-top: primary-container/10`
- Copyright: `© PHANTOM_GRID 2026 — CYBERSPACE / DETROIT`
- No status strings that aren't accurate

---

## ASTRO COMPONENT STRUCTURE

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

## CARRY OVER FROM PROTOTYPE

- Tailwind config (all color tokens) ✓
- Scanline overlay CSS ✓
- `.terminal-glow`, `.bloom-red`, `.glass-panel`, `.pixel-grid` ✓
- Concentric squares in Hero ✓
- Waveform SVG ✓
- Bottom mobile nav ✓
- All SNAKE_CASE labels and terminology ✓

## CHANGES FROM PROTOTYPE

- Space Grotesk → Eurostile
- Coordinates: lat/long → CYBERSPACE / DETROIT / FRANKFURT
- Footer copyright and claim
- Content: real release data (PG-001)
- Navigation: simplified

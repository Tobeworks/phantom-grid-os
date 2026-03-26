# Phantom Grid — Brand Reference Document
## Living Document — maintained by WAVEJUMPER

---

## 1. Creative Direction

**North Star: "The Terminal Void"**

The Phantom Grid visual system evokes the atmosphere of a redacted government transmission or a classified synthesizer schematic from 1982. It is not retro reproduction — it is a specific future imagined by people who understood machines as living systems.

The aesthetic operates on intentional asymmetry: heavy information clusters balanced against vast, deep black negative space. Vector-line ornamentation and "data-leak" aesthetics create a sense of mechanical precision that is gritty, rhythmic, and uncompromising.

---

### Terminal Glow

**Terminal Glow** is the defining atmospheric quality of the system. It refers to the specific visual behavior of CRT monitors, LED arrays, and vintage hardware displays — light that does not illuminate cleanly but bleeds, blooms, and burns through its medium.

Key properties of Terminal Glow:
- **Bloom:** light sources are never sharp — they carry a soft halo of their own color. Red bleeds red. White bleeds warm.
- **Phosphor persistence:** CRT screens hold an image for a fraction of a second after it changes. In the visual system, this translates to glow states that feel like they're still fading.
- **Screen grain:** the surface is never clean. A CRT tube, an LED matrix, an old photocopy — all carry material texture. The background in Phantom Grid assets is not pure digital black. It is worn, slightly grained, as if the surface has a history.

**Terminal Glow is not a decoration.** It is the light condition under which this label exists.

---

### Hardware Aesthetic — The LED Circle Motif

The hollow circle is the label's primary graphic atom. It references:
- **TR-808 / TR-909 pad arrays** — the LED rings of drum machine interfaces; on and off states; binary rhythm as visual language
- **Step sequencer grids** — patterns that read as music before they are heard
- **Vintage LED indicators** — the status light on a piece of hardware that has been running for 40 years

Rules for the circle motif:
- **Hollow only** — a thin stroke circle with Terminal Glow. Never filled.
- **Glow on the stroke** — the line itself carries the red bloom, as if lit from within.
- **Grid logic** — circles appear in structured arrays, not scattered. The pattern should be readable as a sequence.
- **Worn surfaces** — the background behind any circle array should carry analog texture. Film grain, paper texture, subtle noise. Never clean.

This motif is WAVEJUMPER's signature element. It can appear in cover art, web assets, and UI components — never as decoration, always as a statement about the machine nature of the label.

---

**This system rejects:**
- Rounded corners
- Soft color palettes
- Decorative elements without function
- Templates that could belong to any label
- Clean digital backgrounds — the surface must have a material quality

---

## 2. Color System

### Core Palette

| Token | Hex | Role |
|---|---|---|
| `surface-container-lowest` | `#0E0E0E` | Primary background — near-total black |
| `surface` | `#131313` | Base surface layer |
| `surface-container-low` | `#1C1B1B` | Elevated section background |
| `surface-container` | `#201F1F` | Card / component background |
| `surface-container-high` | `#2A2A2A` | Highest surface layer — "above" context |
| `primary-container` | `#CC2222` | Accent — "Dirty Red" — the heartbeat of the system |
| `on-primary` | `#690005` | Text/icon on red backgrounds |
| `on-surface` | `#E5E2E1` | Primary text — dimmed white |
| `outline-variant` | `#5C403D` | Ghost borders — used at 15% opacity |
| `primary` (glow) | `#FFB4AB` | Bloom / glow layer — at low opacity only |

### Color Rules

**The Dirty Red (`#CC2222`)** is the single accent. It should never feel clean — it should feel like it's burning through the screen. Every use of red carries a Neon Bloom: layered `drop-shadow` or `box-shadow` with `#CC2222` at varying opacity to simulate CRT light bleed.

**The No-Line Rule:** Standard 1px solid borders are prohibited for sectioning content. Boundaries are defined through background color shifts between surface tiers — from `surface-container-lowest` to `surface-container-low`, etc.

**Ghost Borders:** When a perimeter is required for accessibility, use `outline-variant` (`#5C403D`) at 15% opacity. Barely visible — like a faint scanline.

**No Pure White:** Never use `#FFFFFF`. `#E5E2E1` is the maximum brightness — it should feel like a glowing screen, not paper.

### Depth & Elevation

Depth is created through tonal layering, not shadows. The UI reads as a series of stacked terminal windows:

```
#0E0E0E (deepest — void)
  └── #131313 (surface)
        └── #1C1B1B (container-low)
              └── #201F1F (container)
                    └── #2A2A2A (container-high — "above")
```

**Ambient Glow (floating elements only):** `box-shadow` using `#CC2222` at 5% opacity, blur radius 40px minimum. Creates "red heat" beneath the element. Not a shadow — an atmospheric effect.

**Glassmorphism:** Floating elements use `background: rgba(19, 19, 19, 0.8)` with `backdrop-filter: blur(12px)`.

---

## 3. Typography

### Type Scale

| Role | Font | Weight | Size | Tracking |
|---|---|---|---|---|
| Hero / Display | Eurostile Extended | 700 (Bold) | 3.5rem+ | Tight (`-0.03em`) |
| Headline | Eurostile | 700 (Bold) | 1.5rem–2.5rem | Tight (`-0.02em`) |
| Label / Navigation | Eurostile | 400 (Regular) | 0.6875rem–0.875rem | Wide (`0.2em–0.5em`) |
| Body / Data | Inter | 400 / 700 | 0.875rem–1rem | Normal |

### Font Sources

```
Eurostile / Eurostile Extended: Adobe Fonts (Typekit) or licensed web font
— Weights: Regular (400), Bold (700)
— Extended variant for hero/display use

Inter: weights 400, 700
— Google Fonts CDN or self-hosted
```

> **Note:** Eurostile is a commercial typeface (Linotype/Monotype). Requires Adobe Fonts subscription or individual license for web embedding. Do not substitute with free alternatives — the letterform geometry is non-negotiable.

### Typography Rules

**Eurostile is the label font** — all display, headline, navigation, and label text. The squared-off letterforms carry the weight of industrial production: stamped metal, machine-tooled precision. Eurostile Extended at hero scale reads like a control panel from a decommissioned facility. Always uppercase in UI context.

**Eurostile Extended** is reserved for hero/display use only — its horizontal mass demands space. At smaller sizes, use standard Eurostile.

**Inter is data font** — high-density information, body text, technical metadata. Creates functional contrast between "Label System" and "Technical Data."

**Tracking discipline:**
- Hero titles: tight (`-0.03em`) — compressed weight, not airy
- Navigation / labels: wide (`0.2em–0.5em`) — legibility through spacing
- Never decorative — tracking serves a structural function

**Numbers and metadata (BPM, dates, coordinates, timestamps):** monospaced treatment, rendered as technical data points, not editorial text.

### Typographic Lineage

Eurostile is not a neutral choice. It carries a specific historical load that maps directly onto the label's sound genealogy.

**Microgramma → Eurostile (1952–1962)**
Designed by Alessandro Butti and Aldo Novarese. Microgramma (capitals only) became the visual language of engineered futures — NASA documentation, science fiction, industrial manuals. Eurostile extended it into a full typeface. Both share the same formal logic: squared apertures, horizontal emphasis, letterforms that read like machine-stamped metal. This is the visual grammar of "a future imagined by people who understood machines."

**Kraftwerk → Detroit (1978–1985)**
Kraftwerk's *The Man-Machine* (1978) embedded this squared, industrial type aesthetic into electronic music. Juan Atkins cited Kraftwerk directly as the blueprint for Detroit Electro. The typographic language travels with the music: Düsseldorf 1978 → Detroit 1985 → Frankfurt 1992 → Mainz 2026. Using Eurostile is not nostalgia — it is tracing the wire back to the source.

**Eye Q / Frankfurt (1991–1996)**
The Eye Q Records visual identity — Frankfurt, the label home of Sven Väth, Rolf Ellmer, Hardfloor — operated in exactly this squared, technical register. Print materials read like industrial documentation. HYDRO THEORY grew up with these sleeves. The Frankfurt formation is present in the type.

**Neptune's Lair (Drexciya, 1999)**
The album from which HYDRO THEORY takes its name uses schematic, circuit-diagram visual language throughout. Eurostile sits natively in that world — it is the font of the classified document, the decommissioned facility, the underwater transmission station.

**The rule:** Every typographic decision on a Phantom Grid asset should feel like it could have appeared on a piece of documentation from this lineage — or on the faceplate of a machine that was built to last. If it couldn't, it doesn't belong.

---

## 4. Naming & Language Convention

All UI labels, section headings, and system terminology follow **SNAKE_CASE in full uppercase**:

```
PHANTOM_GRID
LATEST_SIGNALS
ENTER_VOID
GRID_MESSAGES
CORE_SYSTEM_STATUS
REQUEST_ACCESS
ENCRYPTION_KEY
```

This is not stylistic affectation — it is the label's voice in digital space. Every element of the interface is framed as a terminal command or system output. Copy that does not fit this register does not belong on a Phantom Grid asset.

**In editorial/body copy** (Bandcamp descriptions, press notes, captions): prose is allowed, but the register remains technical, unsentimental, precise. No superlatives. No hype language. Facts and function.

---

## 5. Visual Effects System

### Scanline Overlay

Applied globally on premium editorial sections and web interfaces:

```css
background: linear-gradient(
  rgba(18, 16, 16, 0) 50%,
  rgba(0, 0, 0, 0.1) 50%
),
linear-gradient(
  90deg,
  rgba(255, 0, 0, 0.02),
  rgba(0, 255, 0, 0.01),
  rgba(0, 0, 255, 0.02)
);
background-size: 100% 2px, 3px 100%;
pointer-events: none;
```

Simulates a cathode-ray tube display. Applied as a fixed overlay above all content.

### Neon Bloom (Red Elements)

Every red icon, line, or typographic element carries a bloom:

```css
/* Terminal glow — text */
text-shadow: 0 0 8px rgba(204, 34, 34, 0.6);

/* Bloom — icons and SVG */
filter: drop-shadow(0 0 10px #CC2222);

/* Strong bloom — hover states */
box-shadow: 0 0 15px #CC2222;
```

### Pixel Grid Background

Used in hero sections and atmospheric panels:

```css
background-image: radial-gradient(
  rgba(204, 34, 34, 0.15) 1px,
  transparent 0
);
background-size: 24px 24px;
```

The grid is always present — sometimes visible, sometimes not.

### Vector Accents

Raw SVG lines (0.1rem stroke width) connecting related information elements. Mimics circuit board trace routing or audio signal chains. Used deliberately, not decoratively.

---

## 6. Component Rules

### Roundedness: Zero

`border-radius: 0` on all elements. No exceptions. Everything is a hard 90-degree angle.

### Buttons

**Primary:** Solid `#CC2222` background, `#690005` text. No border-radius. Hover: `box-shadow: 0 0 15px #CC2222`. Active: `scale(0.95)`. Snap transition — no easing.

**Secondary (Ghost):** Transparent background, `border: 1px solid rgba(204,34,34,0.3)`. Text in `#CC2222`. Hover: `background: rgba(204,34,34,0.1)`.

### Input Fields

Background: `#0E0E0E`. Active state: 1px solid `#CC2222` bottom border only — the "Terminal Input" look. No full border on focus.

### Cards

No divider lines between items. Separation through vertical spacing or surface tier shift. Hover state on image cards: `grayscale(0) brightness(1)` — images start desaturated and reveal on interaction.

### Progress / Level Indicators

Segmented block style — not smooth fills. Evokes vintage VU meters. Inactive segments at 30% opacity.

### Interaction Timing

All hover and active transitions are `duration-75` to `duration-100` — snappy and mechanical, like a switch engaging. No soft easing curves on interactive states.

---

## 7. Layout Principles

**Asymmetry is intentional.** Heavy information clusters are balanced against empty space. "Dead zones" in a layout create tension.

**Align to extremes.** Text aligned far left or far right. Center alignment only for hero moments.

**Grid unit: 24px** (matches pixel-grid background-size). All spacing derives from this base.

**Max-width containers:** `max-w-7xl` (80rem) for content sections. Hero sections are full-bleed.

---

## 8. What Is Forbidden

- `border-radius` on any element
- Pure white (`#FFFFFF`) anywhere in the system
- Smooth color gradients as backgrounds (grid dot pattern or solid surfaces only)
- Standard gray divider lines
- Soft/slow transitions on interactive elements
- Decorative type (any font use that isn't structural)
- Red used without its bloom effect
- Multiple accent colors — `#CC2222` is the only accent
- "Clean" or "friendly" visual language of any kind

---

## 9. Asset Checklist

Before any visual asset is released, verify:

- [ ] Works in monochrome (black and white only)
- [ ] Could not be mistaken for another label
- [ ] Grid structure is present, even if invisible
- [ ] Holds up at 100px wide
- [ ] Red elements carry the Neon Bloom
- [ ] No rounded corners
- [ ] Typography is structural, not decorative
- [ ] Every element has a reason to be where it is
- [ ] Background has material quality — grain, texture, worn surface. Not clean digital black.
- [ ] If circles are used: hollow, glowing stroke, grid-logic array
- [ ] Terminal Glow is present — the asset feels lit, not printed

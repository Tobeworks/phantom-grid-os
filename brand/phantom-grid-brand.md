# Phantom Grid — Brand Reference Document
## Living Document — maintained by Vera Cross

---

## 1. Creative Direction

**North Star: "The Terminal Void"**

The Phantom Grid visual system evokes the atmosphere of a redacted government transmission or a classified synthesizer schematic from 1982. It is not retro reproduction — it is a specific future imagined by people who understood machines as living systems.

The aesthetic operates on intentional asymmetry: heavy information clusters balanced against vast, deep black negative space. Vector-line ornamentation and "data-leak" aesthetics create a sense of mechanical precision that is gritty, rhythmic, and uncompromising.

**This system rejects:**
- Rounded corners
- Soft color palettes
- Decorative elements without function
- Templates that could belong to any label

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
| Hero / Display | Space Grotesk | 900 (Black) | 3.5rem+ | Tight (`-0.05em`) |
| Headline | Space Grotesk | 700 (Bold) | 1.5rem–2.5rem | Tight |
| Label / Navigation | Space Grotesk | 400 | 0.6875rem–0.875rem | Wide (`0.2em–0.5em`) |
| Body / Data | Inter | 400 / 700 | 0.875rem–1rem | Normal |

### Font Sources

```
Space Grotesk: weights 300, 400, 700, 900
Inter: weights 400, 700
Google Fonts CDN
```

### Typography Rules

**Space Grotesk is the label font** — all display, headline, navigation, and label text. Wide letterforms mimic stamped serial numbers on hardware. Always uppercase in UI context.

**Inter is data font** — high-density information, body text, technical metadata. Creates functional contrast between "Artistic Labeling" and "Technical Data."

**Tracking discipline:**
- Hero titles: tight (`-0.05em`) — mass through compression
- Navigation / labels: wide (`0.2em–0.5em`) — legibility through spacing
- Never decorative — tracking serves a structural function

**Numbers and metadata (BPM, dates, coordinates, timestamps):** monospaced treatment, rendered as technical data points, not editorial text.

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

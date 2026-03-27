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

### Section 2.1 — The LED Circle Array: Technical Specification

#### Definition

The LED Circle Array is a structured grid of hollow circles rendered as glowing strokes against a worn dark surface. Each circle references a single LED indicator in an on or off state — the visual language of binary rhythm, drawn from drum machine pad arrays and step sequencer grids. The array is not a decorative texture. It is a notation system.

#### Construction Rules

Each circle in the array is defined by the following properties:

- **Form:** A perfect circle, stroke only. No fill, no background. The interior is void.
- **Stroke weight:** 1–1.5px. Thin enough to read as precision-manufactured, not hand-drawn.
- **Diameter:** Consistent within a single array. Recommended range: 16px–32px depending on context. All circles in one array share one size.
- **Color:** `#CC2222` — the single system accent. Never a different hue.
- **Glow:** Every circle carries a Terminal Glow — a `box-shadow` or `filter: drop-shadow` bloom in `rgba(204, 34, 34, 0.5–0.7)`. The stroke appears lit from within, not illuminated from outside. Inactive circles reduce to 15–30% opacity with no bloom. The on/off contrast is the message.

#### Grid Logic

Circles appear in strict rectangular grids. The spacing unit derives from the system's 24px base grid. Typical configurations: `5×3`, `5×4`, `8×4`, `8×8`. The array must read as a sequence — a pattern that implies rhythm before it is heard. Scattered, random, or decorative placement is a system violation.

The grid is always aligned to a structural axis — left edge, center, or right edge of the containing surface. It does not float freely.

#### Surface Requirement

No circle array is placed on a clean digital background. The surface behind the array must carry material quality: film grain, subtle noise texture, or the slight tonal unevenness of worn paper or a CRT screen. Pure `#0E0E0E` is the floor — the actual rendered surface should read as slightly older than that.

#### States

An array communicates through the ratio of active to inactive circles:

| State | Treatment |
|---|---|
| Active / On | Full stroke, full bloom — `box-shadow: 0 0 8px rgba(204,34,34,0.7)` |
| Inactive / Off | Stroke at 15–20% opacity, no bloom |
| Hover / Interaction | Bloom intensifies — `box-shadow: 0 0 14px rgba(204,34,34,0.9)` |
| Animated | Individual circles flip states — timing 300–500ms intervals, no easing curves |

The pattern formed by active/inactive states should be non-random. It may encode a sequence, a catalog number, a BPM value, or a date in binary — or it may simply read as a plausible step-sequencer pattern. It must never look like noise.

#### Usage Contexts

The circle array is a system-wide graphic atom. It appears in:

- **Hero sections** — large-format, `8×8` or wider, primary visual element
- **Cover art** — center-frame or lower-third, as seen in the CORTEXIA assets
- **UI components** — smaller arrays (`5×3` or `5×4`) as section markers or status displays
- **Footer / secondary zones** — minimal arrays (`5×3`) at reduced scale

In all contexts: the array is a statement about the machine nature of the label, not a background pattern.

#### What the Circle Is Not

- It is not a bullet point.
- It is not a decorative dot grid.
- It is not a loading indicator.
- It does not appear filled.
- It does not appear without its bloom.
- It does not appear on a clean surface.

---

### Section 2.2 — The Blinking Cursor: Terminal Presence Indicator

#### Definition

The blinking cursor is a single rectangular block — or underscore — that pulses on and off at a fixed interval. It references the text cursor of a CRT terminal: the system waiting for input, the machine alive but idle. In the Phantom Grid visual system it functions as a **presence signal** — proof that the terminal is running.

#### Construction Rules

- **Form:** A rectangular block character `█` or an underscore `_` placed immediately after text. Never an animated line, never a soft fade. The cursor is a hard-edged rectangle — zero border-radius, like everything else in the system.
- **Color:** `#CC2222` with full Neon Bloom — `text-shadow: 0 0 10px rgba(204, 34, 34, 0.7)`. The cursor glows. It does not merely blink — it burns on and fades to nothing.
- **Timing:** `step-end` animation only. No easing, no fade transition between states. On — then off — then on. A switch engaging, not a breath.
- **Interval:** 1.0–1.2 seconds. Slower than a nervous blink. The rhythm of a machine waiting, not a machine panicking.

```css
@keyframes blink {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0; }
}

.cursor {
  animation: blink 1.2s step-end infinite;
  color: #CC2222;
  text-shadow: 0 0 10px rgba(204, 34, 34, 0.7);
}
```

#### Usage Contexts

The cursor appears **only at the end of a text element** — never mid-word, never standalone. It attaches to:

- **Hero headlines** — after the final word of a display title, marking it as a live terminal output
- **Section labels and eyebrows** — `// LATEST_SIGNALS_` — the cursor signals the line is a system prompt, not an editorial header
- **Input fields** — in the active state of a terminal-style input, replacing the browser default caret where possible
- **Status readouts** — `SYSTEM_ONLINE_` — the cursor confirms the value is live, not static

#### What the Cursor Communicates

The cursor does not decorate. It shifts the register of the text it follows from **editorial** to **operational**. A headline with a blinking cursor is not a title — it is a command waiting to execute. A status label with a cursor is not a label — it is a live readout. This distinction is the entire point of the element.

Used correctly: once per screen section, attached to the most structurally significant text element in that zone.

Used incorrectly: on multiple elements simultaneously, or on body copy, or as ambient decoration. More than one blinking cursor on screen at a time is noise, not signal.

#### What the Cursor Is Not

- It does not fade in or out — `step-end` only
- It does not change size or weight
- It does not appear in a color other than `#CC2222`
- It does not appear without its bloom
- It is not a loading spinner
- It is never centered — it trails the last character of left-aligned text

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

### Vignette

Applied as a fixed overlay — dark edges, luminous center. Creates the impression of a screen with a physical boundary. The eye is drawn inward.

```css
.vignette {
  position: fixed; inset: 0;
  background: radial-gradient(
    ellipse at center,
    transparent 40%,
    rgba(0, 0, 0, 0.55) 100%
  );
  pointer-events: none;
  z-index: 98;
}
```

Always present on full-screen interfaces. Intensity (`0.55`) can be reduced for editorial layouts where content extends to the edges.

---

### CRT Sweep

A single translucent horizontal band that travels from top to bottom of the viewport, simulating the refresh line of a cathode-ray tube. Subtle — it reads as atmosphere, not animation.

```css
.crt-sweep {
  position: fixed;
  left: 0; right: 0;
  top: -10%;
  height: 8%;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(220, 220, 220, 0.025) 50%,
    transparent 100%
  );
  pointer-events: none;
  animation: crt-sweep 8s linear infinite;
}

@keyframes crt-sweep {
  0%   { top: -10%; }
  100% { top: 110%; }
}
```

Cycle time is 8s — slow enough that it reads as a technical phenomenon, not a decorative loop. Do not speed up.

---

### Phosphor Glow (White Text)

Large display type carries a warm white glow — the phosphor persistence of a CRT screen. Combined with the chromatic aberration from the VHS Glitch effect, this creates the full terminal light signature.

```css
text-shadow:
  2px 0 rgba(204, 34, 34, 0.6),       /* chromatic — red channel */
  -2px 0 rgba(0, 200, 255, 0.25),     /* chromatic — cyan channel */
  0 0 20px rgba(220, 220, 220, 0.12), /* phosphor — inner glow */
  0 0 60px rgba(220, 220, 220, 0.04); /* phosphor — outer bloom */
```

Applied to wordmarks and primary display type. The inner glow (`20px`) creates warmth. The outer bloom (`60px`) creates the sense that the light is bleeding into the surrounding dark.

---

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

### VHS Glitch — Signal Corruption Effect

Applied to primary typographic elements (wordmark, section headers) to simulate analog tape dropout and signal interference.

Two components:

**1. Chromatic aberration** — constant, subtle. Red/cyan channel separation on the text.

**2. Glitch pulse** — occasional, rhythmic. Horizontal displacement + opacity drop, simulating a frame tear or head clog on a VHS tape.

```css
.wordmark {
  animation: vhs-flicker 6s step-end infinite;
}

@keyframes vhs-flicker {
  0%, 100% {
    text-shadow: 2px 0 rgba(204, 34, 34, 0.6), -2px 0 rgba(0, 200, 255, 0.25);
    opacity: 1;
    transform: none;
  }
  88% {
    text-shadow: 2px 0 rgba(204, 34, 34, 0.6), -2px 0 rgba(0, 200, 255, 0.25);
    opacity: 1;
    transform: none;
  }
  89% {
    text-shadow: 5px 0 rgba(204, 34, 34, 0.9), -5px 0 rgba(0, 200, 255, 0.5);
    opacity: 0.75;
    transform: translateX(4px);
  }
  90% {
    text-shadow: -4px 0 rgba(204, 34, 34, 0.8), 4px 0 rgba(0, 200, 255, 0.4);
    opacity: 0.85;
    transform: translateX(-3px);
  }
  91% {
    text-shadow: 2px 0 rgba(204, 34, 34, 0.6), -2px 0 rgba(0, 200, 255, 0.25);
    opacity: 1;
    transform: none;
  }
  96%, 97.5% {
    opacity: 1;
    transform: none;
  }
  97% {
    opacity: 0.6;
    transform: translateX(2px);
  }
}
```

**Usage rules:**
- Applied to wordmarks and primary display type only — never to body copy or UI labels
- The animation cycle is 6s — long enough that the glitch reads as an event, not a loop
- Chromatic aberration (the constant `text-shadow`) is always present at low intensity; the displacement is occasional
- Do not apply to the LED array or cursor elements — those have their own animation logic

**Conceptual framing:** the glitch is not damage. It is evidence of transmission. The signal arrived. Something resisted it briefly. The text survived.

### Vector Accents

Raw SVG lines (0.1rem stroke width) connecting related information elements. Mimics circuit board trace routing or audio signal chains. Used deliberately, not decoratively.

---

### Post-Production — Video

The visual effect system is not limited to the web. The same atmospheric stack — scanlines, vignette, film grain, color grade — is available as a post-production filter for video assets.

**Tool:** `tools/phantom-grid-vhs.sh`

```bash
./tools/phantom-grid-vhs.sh input.mp4
```

Applies to any MP4: release teasers, social clips, live recordings, behind-the-scenes material. The output carries the same terminal glow signature as the web interface.

**Conceptual rule:** any video that represents Phantom Grid in public should pass through this filter. The aesthetic is not optional. It is the medium.

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

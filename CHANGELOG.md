# Changelog

All significant changes to the Phantom Grid OS are documented here.

Format: `[VERSION] — YYYY-MM-DD — description`

---

## [0.2.0] — 2026-04-11 — Remove AI persona system

### Removed

- `soul/` — persona soul files (HYDRO THEORY, STORM SURGE, WAVEJUMPER)
- `roles/` — formal role documents for all three personas
- `posts/` — blog posts authored by personas
- `workflows/signal-test.md` — A&R evaluation framework tied to HYDRO THEORY
- `workflows/handoffs.md` — persona-to-persona handoff protocols
- `workflows/session-init.md` — AI session initialisation prompts
- `brand/listening-room.md` — reference track list maintained by HYDRO THEORY

### Changed

- All remaining files cleaned of persona references (HYDRO THEORY, STORM SURGE, WAVEJUMPER, Void-as-persona)
- `brand/sonic-brief.md`, `brand/phantom-grid-brand.md`, `brand/not-phantom-grid.md`, `brand/manifesto.md` — persona attributions removed
- `releases/_template/` and `releases/pg-001-*/` — persona subheadings removed from all release docs
- `workflows/platform-texts.md`, `releases/README.md`, `transmission-log.md`, `README.md`, `CHANGELOG.md`, `IDEAS.md` — cleaned

---

## [0.1.3] — 2026-03-26 — CPU Unit + Eternal Cycle + README sync

### Added

- `architecture/cpu-unit.md` — CPU Unit vision: pipeline architecture, roles as Claude agents, eternal cycle cosmology, implementation phases
- `README.md`: Core Statements section added — distilled key positions; Principles updated with principle 6 (Everything becomes code); repository structure synced; About Void expanded with all music projects

---

## [0.1.2] — 2026-03-26 — Blinking Cursor spec

### Added

- `brand/phantom-grid-brand.md`: Section 2.2 — The Blinking Cursor: Technical Specification — construction rules, CSS animation (`step-end` only), usage contexts, what the cursor communicates, what it is not

---

## [0.1.1] — 2026-03-26 — LED Circle Array spec

### Added

- `brand/phantom-grid-brand.md`: Section 2.1 — The LED Circle Array: Technical Specification — construction rules, grid logic, surface requirement, states (active/inactive/hover/animated), usage contexts, what the circle is not

---

## [0.1.0] — 2026-03-26 — Terminal Glow / Hardware Aesthetic / BPM range

### Changed

- `brand/phantom-grid-brand.md`: Terminal Glow established as core aesthetic; Hardware Aesthetic section expanded — worn surface, film grain, CRT/LED references, retro-futurist characteristics documented from Cortexia artwork reference
- `brand/sonic-brief.md`: BPM range corrected to 115–140; Detroit Techno emphasis reduced — Detroit as spark, not center; genre scope expanded across Electro, Techno, Minimal, Ambient

---

## [0.0.9] — 2026-03-26 — Manifesto rewrite: code first, Detroit as spark

### Changed

- `brand/manifesto.md`: Structural rewrite — cyberspace/code-based existence as primary claim; Detroit reduced to spark/origin; eternal cycle paragraph added; modern genre scope reflected; `CYBERSPACE / DETROIT` → `CYBERSPACE / EST. 2026`

---

## [0.0.7] — 2026-03-26 — Manifesto: open source claim / Sonic Brief

### Added

- `brand/sonic-brief.md` — positive sonic definition: tempo, drum architecture, bass, synthesis, arrangement; core question
- `brand/manifesto.md`: open source paragraph added — the fork argument: structure is copyable, transmission is not; parallels the Fluency vs. Voice distinction

---

## [0.0.6] — 2026-03-26 — Open source / PG-001 initiated

### Added

- `LICENSE` — MIT License
- `web/layout-spec.md` — Astro site layout briefing; section specs, component structure, what's inherited from HTML prototype
- `releases/pg-001-input-null-vector-field-signals/` — PG-001 initiated: Input Null, "Vector Field Signals"

### Changed

- `COORDINATES.md` — repo URL set: github.com/Tobeworks/phantom-grid-os; open source note added
- `README.md` — license and repo URL added; version bump

---

## [0.0.5] — 2026-03-26 — Cyberspace identity

### Changed

- `brand/manifesto.md`: Cyberspace claim made explicit — "the first record label in the Detroit Electro tradition to be fully code-based"; `MAINZ / DETROIT` → `CYBERSPACE / DETROIT`; `NOT_LOCATED` added to exclusion list
- `README.md`: Base confirmed as Cyberspace; About Void updated — distinction between Void as human and the label as a non-physical entity
- `README.md`: repository structure updated with `COORDINATES.md`

### Added

- `COORDINATES.md` — label location in cyberspace; platform URL registry; signal origin

---

## [0.0.4] — 2026-03-26 — System operational

### Added

- `releases/README.md` — release system documentation
- `releases/_template/` — release folder template with four files:
  `release.md`, `anr-decision.md`, `artwork-brief.md`, `promo-arc.md`
- `brand/manifesto.md` — label manifesto; internal and public-facing
- `brand/not-phantom-grid.md` — musical exclusion document
- `transmission-log.md` — running log of all label events, signings, and system decisions

### Changed

- `README.md`: repository structure updated to reflect new files and folders

---

## [0.0.3] — 2026-03-26 — Frankfurt lineage + typography

### Changed

- `README.md`: About Void expanded — Omen, Robert Johnson, Klang Elektronik release as **Antiga Prime** documented as founding context for the label
- `brand/phantom-grid-brand.md`: Eurostile / Eurostile Extended established as primary typeface; Inter retained as data font; Space Grotesk removed
- `brand/phantom-grid-brand.md`: "Typographic Lineage" section added — traces Eurostile through Kraftwerk → Detroit → Eye Q Frankfurt → Drexciya / Neptune's Lair

---

## [0.0.1] — 2026-03-26 — Initial system build

### Added

- `README.md` — label identity, structure, principles, overview
- `brand/phantom-grid-brand.md` — living brand reference document; color system, typography, effects, component rules, asset checklist
- `releases/` — placeholder for release folders

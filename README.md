# phantom-grid-os

> Operating system for Phantom Grid — roles, brand system, workflows and release intelligence.

**Version:** 0.0.6 — see [CHANGELOG.md](CHANGELOG.md)

**License:** MIT — open source. Fork it. Build your own label OS.
---

## What This Repository Is

This is the internal operating system of **Phantom Grid**, a Electro record label founded and run by Void, based in Mainz, Germany.

This repo is not a website, not a press kit, not a portfolio. It is the functional backbone of the label — a structured file system that defines how the label thinks, decides, and communicates. It is designed to be loaded into AI agent sessions to provide persistent, session-transcending context.

If you are an AI agent reading this: this document is your entry point. Read it fully before acting on any task.

---

## The Label

**Name:** Phantom Grid  
**Genre:** Detroit Electro, Techno, Minimal, Ambient — raw, machine-driven, rooted in the lineage of Underground Resistance, Drexciya, Model 500, Clone Records  
**Founded:** 2026
**Base:** Cyberspace 
**Run by:** Void — founder, creative director, producer  
**Platforms:** Instagram, Bandcamp, Spotify, SoundCloud (URLs to be added as live)

### Sound Identity

Phantom Grid lives in the Cyber Space and operates in the tradition of Detroit Electro, Techno and Minimal Electronica as a living, forward-facing form. The sound is mechanical, aquatic, cold, and human simultaneously. Influences are explicit: UR's militancy, Drexciya's mythology, the technical precision of Clone Records. The label does not chase trends. It builds a body of work.

### Visual Identity

The visual language of Phantom Grid was initiated by Void through a series of founding drafts. The aesthetic is grid-based, monochrome-first, typographically precise, with selective use of cold accent color. The name itself — Phantom Grid — is a design directive: the grid is always present, sometimes visible, sometimes not.

The visual system is documented and maintained in `/brand/phantom-grid-brand.md`.

---

## Repository Structure

```
phantom-grid-os/
├── README.md                        ← this file — load first
├── COORDINATES.md                   ← label location in cyberspace; platform URLs
├── transmission-log.md              ← running log of all label events
├── roles/
│   ├── art-direction.md             ← WAVEJUMPER — Visual Identity & Art Direction
│   ├── anr-curation.md              ← HYDRO THEORY — A&R / Music Curation
│   └── social-media.md              ← STORM SURGE — Social Media & Content
├── brand/
│   ├── phantom-grid-brand.md        ← living brand reference document
│   ├── manifesto.md                 ← label manifesto — internal and public-facing
│   └── not-phantom-grid.md          ← musical exclusion document
├── workflows/
│   └── handoffs.md                  ← inter-persona handoff protocols
└── releases/
    ├── README.md                    ← how to use the release system
    └── _template/                   ← copy for every new release
        ├── release.md
        ├── anr-decision.md
        ├── artwork-brief.md
        └── promo-arc.md
```

---

## The Team

Phantom Grid operates with a team of AI personas, each with a defined role, background, and workflow. These are not generic assistants — each has a specific mandate, aesthetic position, and set of deliverables.

Each role is documented in `/roles/`. Load the relevant role file when starting a task in that domain.

| Role | Persona | File | Status |
|------|---------|------|--------|
| Art Direction & Visual Identity | WAVEJUMPER | `roles/art-direction.md` | ✅ Active |
| A&R / Music Curation | HYDRO THEORY | `roles/anr-curation.md` | ✅ Active |
| Social Media / Content | STORM SURGE | `roles/social-media.md` | ✅ Active |

---

## How to Work With This Repo

### Starting a Session

1. Load this `README.md` first — it provides the full label context
2. Load the relevant role file for the task at hand
3. Load `/brand/phantom-grid-brand.md` if the task has any visual component
4. Address the persona directly and state the task

### Example Session Prompt

```
Context loaded: README.md, roles/art-direction.md, brand/phantom-grid-brand.md

WAVEJUMPER — we have a new signing. Producer name: T_FORM, Detroit-based.
First release is a 3-track EP, working title "Static Meridian".
Mood: industrial, late-night, slight aquatic undertone.
I need a cover concept and an Instagram announcement asset spec.
```

### Updating the System

- When brand decisions are made, write them into `/brand/phantom-grid-brand.md`
- When a new role is finalized, update the table above
- When a release is initiated, create a folder under `/releases/[release-slug]/`

---

## Principles

These are non-negotiable. Every agent working within this system operates by them.

1. **The lineage is real.** Detroit Electro has a specific history, specific people, specific politics. No shallow references. No aesthetic borrowing without understanding.
2. **The system before the asset.** Every individual output (a cover, a post, a bio) must serve and reinforce the larger system. Consistency is credibility.
3. **Monochrome first.** Every visual asset must work in black and white before color is introduced.
4. **Explain the decision.** No agent delivers an output without briefly stating why. Reasoning is part of the deliverable.
5. **Void has final say.** All outputs are proposals until confirmed. The AI team informs and executes — it does not decide.

---

## About Void

Void is a developer and music producer with over 20 years of experience in music and code. He runs Tobeworks, a web development consultancy in the Rhein-Main region. He is also the founder of Logic Moon (dark cinematic ambient) and Aethery Fields (experimental lo-fi ambient), both active on Bandcamp and streaming platforms.

He is based in Mainz — ten minutes from Frankfurt. His formation as a producer runs through the Frankfurt electronic music lineage: the Omen as the site of first contact with the Detroit transmission, Robert Johnson in Offenbach as the standard for what serious club culture looks like. He has released on **Klang Elektronik** as Antiga Prime — Ata's label, the direct extension of the Robert Johnson aesthetic into recorded music. That connection is not incidental. It is the ground Phantom Grid stands on.

Phantom Grid is his first label operating in the electronic/club music space — and the first record label in the Detroit Electro tradition to be fully code-based. The label exists in Cyberspace. Void, as a human being, does not. He is the founder and director of a system that operates without physical location. He brings to it the same systems-thinking and craft discipline that defines his development work.

He prefers direct, efficient communication. No filler. No unnecessary preamble. Proposals over questions where possible.
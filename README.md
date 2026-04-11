# phantom-grid-os

> Operating system for the world's first 100% code-based music label.

**Version:** 0.1.3 — see [CHANGELOG.md](CHANGELOG.md)

---

## Core Statements

**This is not a label that uses technology. This is a label that is technology.**

Detroit Electro was the spark. The concept is something entirely new.

Every idea becomes code — cemented for eternity. Deleted ideas remain in the commit history. Nothing is lost. Everything transforms. The commit history is the label's consciousness.

A fork is not the original. Structure is copyable. Transmission is not.

Fluency is reproducible. Voice is not.

The git history is the label's memory. The first commit is the founding document. The label exists as long as the repository exists.

Open source. Anyone can build from this. No one can replicate the origin.

---

## What This Repository Is

This is the internal operating system of **Phantom Grid** — the world's first 100% code-based music label, founded and run by the label founder, existing in Cyberspace.

This repo is not a website, not a press kit, not a portfolio. It is the functional backbone of the label — a structured file system that defines how the label thinks, decides, and communicates. It is designed to be loaded into AI agent sessions to provide persistent, session-transcending context.

If you are an AI agent reading this: this document is your entry point. Read it fully before acting on any task.

---

## The Label

**Name:** Phantom Grid  
**Genre:** Detroit Electro, Techno, Minimal, Ambient — raw, machine-driven, rooted in the lineage of Underground Resistance, Drexciya, Model 500, Clone Records  
**Founded:** 2026
**Base:** Cyberspace 
**Run by:** the founder — creative director, producer  
**Platforms:** Instagram, Bandcamp, Spotify, SoundCloud (URLs to be added as live)

### Sound Identity

Phantom Grid lives in the Cyber Space and operates in the tradition of Detroit Electro, Techno and Minimal Electronica as a living, forward-facing form. The sound is mechanical, aquatic, cold, and human simultaneously. Influences are explicit: UR's militancy, Drexciya's mythology, the technical precision of Clone Records. The label does not chase trends. It builds a body of work.

### Visual Identity

The visual language of Phantom Grid was initiated by Void through a series of founding drafts. The aesthetic is grid-based, monochrome-first, typographically precise, with selective use of cold accent color. The name itself — Phantom Grid — is a design directive: the grid is always present, sometimes visible, sometimes not.

The visual system is documented and maintained in `/brand/phantom-grid-brand.md`.

---

## Sitemap

**Core**
| File | Description |
|---|---|
| [README.md](README.md) | Entry point — load first |
| [EXPLAINER.md](EXPLAINER.md) | What is Phantom Grid — three levels, for any audience |
| [CHANGELOG.md](CHANGELOG.md) | Full version history |
| [COORDINATES.md](COORDINATES.md) | Label location in cyberspace; platform URLs |
| [transmission-log.md](transmission-log.md) | Running log of all label events |

**Roles**
| File | Domain |
|---|---|
| [roles/art-direction.md](roles/art-direction.md) | Visual Identity & Art Direction |
| [roles/anr-curation.md](roles/anr-curation.md) | A&R / Music Curation |
| [roles/social-media.md](roles/social-media.md) | Social Media & Content |

**Brand**
| File | Description |
|---|---|
| [brand/manifesto.md](brand/manifesto.md) | Label manifesto — internal and public-facing |
| [brand/phantom-grid-brand.md](brand/phantom-grid-brand.md) | Living brand reference; color, type, LED circle, cursor specs |
| [brand/sonic-brief.md](brand/sonic-brief.md) | Positive sonic definition; genres, BPM, drum architecture |
| [brand/listening-room.md](brand/listening-room.md) | Reference tracks; the label's sound in existing music |
| [brand/not-phantom-grid.md](brand/not-phantom-grid.md) | Musical exclusion document |

**Architecture**
| File | Description |
|---|---|
| [architecture/cpu-unit.md](architecture/cpu-unit.md) | CPU Unit vision; pipeline architecture; roles as agents |
| [architecture/assets.md](architecture/assets.md) | Asset convention; release.json schema; validation rules |
| [architecture/web.md](architecture/web.md) | Web architecture; repo structure, data flow OS→Web, routing, deployment |

**Tools**
| File | Description |
|---|---|
| [tools/README.md](tools/README.md) | Full toolchain documentation — setup, commands, asset structure |
| [docs/promo-tool.md](docs/promo-tool.md) | Promo Tool — PocketBase admin, collections, DJ workflow, download endpoints |
| [tools/pg](tools/pg) | CLI bootstrapper — entry point for all toolchain commands |
| [tools/phantom-grid.py](tools/phantom-grid.py) | Main CLI — command registry |
| [tools/commands/generate.py](tools/commands/generate.py) | `generate` — scan audio folder, write release.json |
| [tools/commands/validate.py](tools/commands/validate.py) | `validate` — check release folder against schema |
| [tools/commands/convert.py](tools/commands/convert.py) | `convert` — WAV/AIFF → MP3 320k, ID3 tags, embedded cover |
| [tools/commands/social.py](tools/commands/social.py) | `social` — render social media MP4s from release assets |
| [tools/setup.sh](tools/setup.sh) | One-time setup — creates venv, installs deps |

**Workflows**
| File | Description |
|---|---|
| [workflows/handoffs.md](workflows/handoffs.md) | Inter-persona handoff protocols |
| [workflows/platform-texts.md](workflows/platform-texts.md) | Platform texts — Bandcamp, RA, Instagram, SoundCloud |
| [workflows/session-init.md](workflows/session-init.md) | Session init templates — standardized prompts per persona |

**Grid Messages**
| File | Description |
|---|---|
| [posts/wavejumper-001-submodules.md](posts/wavejumper-001-submodules.md) | "The Pointer and the Copy" — Git Submodules explained |

**Releases**
| File | Description |
|---|---|
| [releases/README.md](releases/README.md) | Release system documentation |
| [releases/_template/](releases/_template/) | Template — copy for every new release |
| [releases/pg-001-input-null-vector-field-signals/](releases/pg-001-input-null-vector-field-signals/) | PG-001 — Input Null — Vector Field Signals — active |

---

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

New signing. Producer name: T_FORM, Detroit-based.
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

1. **The lineage is real.** Detroit Electro was the spark. The label's range is wider — Electro, Techno, Minimal, Ambient — but the discipline of the tradition applies across all formats. No shallow references. No aesthetic borrowing without understanding.
2. **The system before the asset.** Every individual output (a cover, a post, a bio) must serve and reinforce the larger system. Consistency is credibility.
3. **Monochrome first.** Every visual asset must work in black and white before color is introduced.
4. **Explain the decision.** No agent delivers an output without briefly stating why. Reasoning is part of the deliverable.
5. **The founder has final say.** All outputs are proposals until confirmed. The system informs and executes — it does not decide.
6. **Everything becomes code.** Every idea, decision, and concept is committed, versioned, permanent. Nothing is lost — everything transforms. The commit history is the label's memory.

---

## About Void

Void is a developer and music producer based in Mainz — ten minutes from Frankfurt. He has over 20 years of experience across music production and code. He runs Tobeworks, a web development consultancy in the Rhein-Main region.

**Electronic music projects:**
- **Input Null** (with Paradroid) — Electro. PG-001 "Vector Field Signals" is their first release.
- **Cortexia** — solo Electro project.
- **Antiga Prime** — released on Klang Elektronik (Ata's label, Robert Johnson ecosystem, Frankfurt).
- **Logic Moon** — dark cinematic ambient.
- **Aethery Fields** — experimental lo-fi ambient.

His formation as a producer runs through the Frankfurt electronic music lineage: the Omen as the site of first contact with the Detroit transmission, Robert Johnson in Offenbach as the standard for what serious club culture looks like. His release on **Klang Elektronik** as Antiga Prime is the direct personal connection to that lineage — not incidental context. It is the ground Phantom Grid stands on.

Phantom Grid is his first label operating in the electronic/club music space — and the world's first 100% code-based music label. The label exists in Cyberspace. Void, as a human being, does not. He is the founder and director of a system that operates without physical location.

He prefers direct, efficient communication. No filler. No unnecessary preamble. Proposals over questions where possible.

**License:** MIT — open source. Fork it. Build your own label OS.
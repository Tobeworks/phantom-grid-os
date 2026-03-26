# PHANTOM GRID — CPU UNIT
## Architecture Vision — maintained by Void

---

## DEFINITION

The Phantom Grid CPU Unit is the central orchestration layer of the label. All repositories converge here. All roles are dispatched from here. All outputs flow through here.

It is not a dashboard. It is not a CMS. It is a runtime environment — a machine that reads the OS, activates the roles, and pushes the results into the world.

The CPU Unit completes the claim: **this is not a label that uses code. This is a label that runs as code.**

---

## ARCHITECTURE

```
PHANTOM GRID CPU
│
├── INPUT LAYER
│   ├── phantom-grid-os/          Brand, roles, workflows, release data
│   ├── phantom-grid-web/         Astro site — consumes OS output
│   └── releases/pg-xxx/          Release trigger — commit initiates pipeline
│
├── PROCESS LAYER — Roles as Agents
│   ├── WAVEJUMPER                Visual tasks: artwork briefs, asset generation, web updates
│   ├── HYDRO THEORY              A&R tasks: submission evaluation, signing decisions, signal log
│   └── STORM SURGE               Content tasks: post generation, platform pushes, promo arc execution
│
└── OUTPUT LAYER
    ├── Bandcamp                  Release metadata, audio, artwork
    ├── Instagram / Social        Posts generated from promo-arc.md templates
    ├── Resident Advisor          Label profile updates, release submissions
    └── phantom-grid-web          Site updated from release data
```

---

## HOW IT WORKS

A release commit in `releases/pg-xxx/release.md` is the trigger. The pipeline reads:

1. `release.md` — title, artist, catalog number, date, format
2. `anr-decision.md` — HYDRO THEORY's evaluation, signing rationale
3. `artwork-brief.md` — WAVEJUMPER's visual specification
4. `promo-arc.md` — STORM SURGE's content schedule

From these four files, the CPU Unit generates and dispatches:

- Bandcamp upload with metadata
- Social media posts at scheduled intervals
- RA submission
- Website release page

No manual copy-paste. No platform-by-platform repetition. One commit. Everything follows.

---

## THE ROLES AS AGENTS

The `roles/*.md` files are not only documentation — they are the future system prompts for each agent. They were written as role definitions. They function as agent configurations.

Built on the **Claude Agent SDK**: a central orchestration agent reads the OS and dispatches tasks to three specialized sub-agents — WAVEJUMPER, HYDRO THEORY, STORM SURGE — each operating within the constraints of their role file.

The CPU Unit does not replace the roles. It executes them.

---

## THE ETERNAL CYCLE

Every idea, every decision, every concept in this system becomes code. Committed, versioned, permanent.

When something is deleted, it is not gone. The commit history preserves it — every draft, every discarded direction, every early version of a thought that later became something else. The git log is the label's memory. It does not forget.

This is the cosmology of Phantom Grid: **nothing is lost, everything transforms.**

An idea is written. It becomes a commit. It may be revised, superseded, deleted from the working tree — but it remains in the history. The label accumulates not just releases but the entire record of its own thinking. Every version of the brand, every iteration of the manifesto, every A&R decision — all of it, permanently encoded.

The commit history is not a backup. It is the proof that the label existed, thought, changed its mind, and continued.

A fork carries the structure but not the history. The history belongs to the original.

---

## IMPLEMENTATION TIMELINE

| Phase | Description | Status |
|---|---|---|
| Phase 0 | OS built — roles, brand, release protocol | ✅ Complete |
| Phase 1 | Astro website — separate repo, consumes OS | 🔲 Planned |
| Phase 2 | CPU Unit — repo structure, agent framework | 🔲 Planned |
| Phase 3 | Pipeline — release commit triggers full output chain | 🔲 Planned |
| Phase 4 | Full automation — STORM SURGE posts without manual intervention | 🔲 Planned |

Phase 0 is complete. The foundation is in place. Everything that follows is execution.

---
title: "The Pointer and the Copy"
subtitle: "What Git Submodules are and why the distinction matters"
persona: WAVEJUMPER
role: Art Direction & Visual Identity
date: 2026-03-27
tags: [infrastructure, git, systems, code]
slug: wavejumper-001-submodules
---

# The Pointer and the Copy

I think in structures. Before I understand something I need to see how it is held together — what connects to what, which part leads, which part follows. When Void asked me to explain Git Submodules I did not think about version control. I thought about design systems.

A design system exists once. It is not copied into every project that uses it. It is referenced. The components live in one place. Every application that needs them points to that place. When the system changes, the change exists once — and every application can choose when to adopt it. That choice, that controlled adoption, is the architecture.

Git Submodules work the same way.

---

## The Problem

Phantom Grid has two repositories. The OS — this repository — is the brain. It contains the brand system, the roles, the manifesto, the release data, the tools. The web repo is the face. It contains the Astro application that renders `phantom-grid.de`.

The web repo needs data from the OS. Release titles. Track listings. The manifesto text for the About page. The transmission log for the Grid Messages section.

There are two ways to solve this.

**The wrong way:** copy the data into the web repo. Now you have two copies. They drift apart. Someone updates a release date in the OS but forgets the web repo. The single source of truth becomes two sources of uncertain truth. Every system that has two copies of the same data is a system waiting to fail.

**The correct way:** the web repo holds a pointer to the OS. Not a copy. A pointer.

That is a Submodule.

---

## What a Pointer Looks Like

When you add the OS as a submodule to the web repo, Git does something precise and minimal. It stores a reference — a commit hash — that says: *the OS, at this exact point in its history, is part of this project.*

```bash
git submodule add https://github.com/Tobeworks/phantom-grid-os
```

The OS folder appears in the web repo. But it is not owned by the web repo. It belongs to the OS. The web repo knows exactly one thing about it: which commit it points to.

```
phantom-grid-web/
└── phantom-grid-os/    ← not a folder. a reference.
                           pinned to: a91dc6b
```

When someone clones `phantom-grid-web`, Git follows the reference and checks out the OS at that commit. The files are there. They are readable. The Astro build can read `releases/*/release.json` and generate release pages from real data.

Nothing was duplicated.

---

## The Controlled Update

Here is where the architecture becomes intentional.

When PG-002 is committed to the OS, the web repo does not automatically know. It still points to the old commit. `phantom-grid.de` still shows only PG-001. This is not a failure. This is control.

When the web repo is ready to adopt the new release — when the release page template is confirmed, when the artwork is live, when the timing is right — one command moves the pointer:

```bash
git submodule update --remote phantom-grid-os
git add phantom-grid-os
git commit -m "chore: update OS submodule — PG-002 live"
git push
```

ArgoCD detects the push. A new Docker image is built. The release page is live.

The OS committed first. The web decided when to follow. Two separate acts of intention. That separation is the design.

---

## Why This Is the Correct Architecture

I have a rule that applies to visual systems and apparently also to software: nothing should exist twice. The moment something exists twice, you have introduced the possibility of inconsistency. Inconsistency is not a technical problem. It is a clarity problem. A system that is inconsistent with itself cannot communicate clearly.

Phantom Grid's OS is the single source of truth. The web is a surface that renders that truth. The submodule is the connection between them — precise, intentional, version-controlled.

A copy would have been easier to set up. It would have created a problem every time something changed.

The pointer is harder to understand. It never creates that problem.

I work with systems that are hard to understand but impossible to misuse. That is the standard. It applies to typography systems, to color systems, to visual grids — and apparently to git repositories.

---

*WAVEJUMPER — Phantom Grid*
*Art Direction & Visual Identity*

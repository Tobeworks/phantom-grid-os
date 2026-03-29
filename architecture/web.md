# Web Architecture — phantom-grid-web
*Astro site for phantom-grid.de*

References:
- Visual spec: `web/layout-spec.md`
- Design system: `brand/phantom-grid-brand.md`
- Asset structure: `architecture/assets.md`
- Deployment pattern: netcup ArgoCD cluster

---

## Repository Decision

`phantom-grid-web` is a **separate repository** from `phantom-grid-os`.

Rationale:
- OS is documentation and toolchain — no build step, no node_modules, no CI
- Web is a deployable application — Astro build, npm, Docker image
- Separation enforces the conceptual boundary: OS is the brain, web is the face
- Both repos are public; the web repo explicitly references the OS as its source of truth

```
github.com/Tobeworks/phantom-grid-os    ← source of truth
github.com/Tobeworks/phantom-grid-web   ← consumer + deployment
```

---

## Data Flow: OS → Web

`phantom-grid-os` is included in `phantom-grid-web` as a **git submodule**.

```
phantom-grid-web/
└── phantom-grid-os/    ← submodule, pinned to HEAD
```

During the Astro build, content is read directly from the submodule:

| Source (OS) | Consumer (Web) |
|---|---|
| `releases/*/release.json` | Dynamic release pages |
| `posts/*.md` | Grid Messages — per-persona blog posts |
| `transmission-log.md` | Transmission feed section |
| `brand/manifesto.md` | About page |
| `COORDINATES.md` | Footer platform links |

No content is duplicated into the web repo. When a release is committed to the OS, the web repo updates the submodule reference and rebuilds.

---

## Tech Stack

| Layer | Choice | Reason |
|---|---|---|
| Framework | Astro | Static-first, island architecture, no JS overhead on static pages |
| Styling | Tailwind CSS | Already in the HTML prototype; utility-first fits the system |
| Typography | Barlow Condensed via Adobe Fonts | As defined in brand doc |
| Deployment | Docker → k3s via ArgoCD | Same pattern as all other apps in the netcup cluster |
| Container | nginx:alpine | Static file serving for Astro build output |

No component library. No UI framework. Custom components only — the design system is already fully specified in `brand/phantom-grid-brand.md`.

---

## Routes

```
/                          ← index (layout-spec.md)
/releases                  ← full catalog
/releases/[slug]           ← individual release page
/archive                   ← all releases, chronological
/about                     ← label identity + OS link
/grid-messages             ← transmission log (markdown rendered)
/grid-messages/[slug]     ← individual posts by persona (from posts/ in OS)
```

Dynamic routes (`/releases/[slug]`) are generated at build time from `release.json` files in the OS submodule.

---

## Release Page — Data Model

Each `releases/[catalog]-[slug]/release.json` maps to a static page:

```
release.json field     → Page element
─────────────────────────────────────────────
catalog                → Catalog number badge (PG-001)
artist                 → Artist name
title                  → Release title
format                 → Format tag (EP / LP / Single)
release_date           → Date display
tracks[]               → Tracklist
tracks[].duration      → Duration per track
distribution.bandcamp  → Bandcamp link
distribution.soundcloud → SoundCloud link
```

Cover art is sourced from `phantom-grid-assets/` via the SFTP-served URL (not committed to either repo).

---

## Deployment

Same pattern as all apps in the netcup cluster:

```
phantom-grid-web/
├── Dockerfile
├── nginx/nginx.conf
├── .github/workflows/build.yaml
```

ArgoCD Application manifest in `netcup/cluster/argocd-apps/phantom-grid-web.yaml`.

Build pipeline:
```
git push → GitHub Actions → docker build → ghcr.io push → ArgoCD auto-sync → live
```

The coming soon page (`phantom-grid.de`) is replaced by this deployment when the first version is ready.

### Dockerfile

Two-stage build:

1. `node:20-alpine` — installs dependencies via pnpm, runs `pnpm build`, produces `dist/`
2. `nginx:alpine` — copies `dist/` and `nginx/nginx.conf`, serves on port 8080

```dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN corepack enable && pnpm install --frozen-lockfile
COPY . .
RUN pnpm build

FROM nginx:alpine
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 8080
```

### GitHub Actions — build.yaml

Trigger: push to `main`.

**Critical:** `submodules: recursive` in the checkout step is required. Without it, the `phantom-grid-os` submodule is not checked out and the Astro build fails — content files are missing.

```yaml
- uses: actions/checkout@v4
  with:
    submodules: recursive
```

Image pushed to `ghcr.io/tobeworks/phantom-grid-web:latest`. ArgoCD Image Updater detects the new digest and redeploys automatically.

### nginx

Port 8080 (cluster standard). Features:
- `/healthz` endpoint for liveness/readiness probes
- Aggressive caching for static assets (1y, immutable)
- gzip compression for all text-based formats
- SPA fallback: `try_files $uri $uri/ /index.html`

---

## Submodule Update Workflow

When a new release is added to the OS:

```bash
# In phantom-grid-web:
git submodule update --remote phantom-grid-os
git add phantom-grid-os
git commit -m "chore: update OS submodule — PG-002"
git push
# → ArgoCD rebuilds, new release page is live
```

This will eventually be automated via GitHub Actions triggered by a push to the OS repo.

---

## What the Web Repo Does Not Contain

- No brand decisions (→ `brand/phantom-grid-brand.md`)
- No release metadata (→ `releases/*/release.json` in OS)
- No audio files or artwork (→ `phantom-grid-assets/`, served via SFTP/CDN)
- No role or workflow documentation (→ OS repo)

---

*Part of phantom-grid-os — architecture layer*

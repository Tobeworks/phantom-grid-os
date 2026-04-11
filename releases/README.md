# RELEASES

Each release lives in its own folder: `pg-[NNN]-[artist-slug]-[title-slug]/`

```
releases/
├── _template/          ← copy this for every new release
├── pg-001-[...]/
├── pg-002-[...]/
└── ...
```

## Starting a release

1. Copy `_template/` — rename to `pg-[NNN]-[artist]-[title]`
2. Fill in `release.md` first — this is the master record
3. Label uses `anr-decision.md` for the A&R evaluation
4. Label uses `artwork-brief.md` for the visual brief
5. Label uses `promo-arc.md` for the campaign

Status moves: `DEVELOPMENT → APPROVED → IN_PRODUCTION → RELEASED`

# Promo Tool

Token-geschützte Listening Pages für DJs und Journalisten.
Kein Account, kein Login — nur ein Link mit Token.

---

## Workflow

```
Label legt Promo an (PocketBase Admin)
  → generiert Link: phantom-grid.de/promo/pg-001?t=TOKEN
  → schickt Link per Mail an DJ
  → DJ öffnet Link: hört Release, lädt Tracks, gibt Feedback
  → Label liest Feedback in PocketBase Admin
```

---

## Admin UI

**Production:**
```
https://pb.phantom-grid.de/_/
```

**Lokal:**
```
http://localhost:8090/_/
```

Login mit dem Superuser-Account (beim ersten Start angelegt).
Falls Passwort vergessen:

```bash
kubectl exec -n phantom-grid-web deployment/pocketbase -- \
  /pb/pocketbase superuser upsert admin@phantom-grid.de NeuesPasswort123!
```

---

## Promo anlegen

1. PocketBase Admin öffnen → **Collections → promos → New record**
2. Felder ausfüllen:

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `token` | ✅ | Einzigartiger Zugangscode, z.B. `PG001-DJ-KOOL-X7K` |
| `release_slug` | ✅ | Catalog-ID lowercase, z.B. `pg-001` |
| `recipient_name` | ✅ | Name des DJs — wird auf der Seite angezeigt |
| `recipient_email` | — | Nur zur internen Referenz |
| `notes` | — | Interne Notizen (nicht sichtbar für DJ) |
| `expires_at` | — | Ablaufdatum — danach zeigt die Seite "EXPIRED" |

3. Speichern → Link zusammenbauen:

```
https://phantom-grid.de/promo/[release_slug]?t=[token]
```

**Beispiel:**
```
https://phantom-grid.de/promo/pg-001?t=PG001-DJ-KOOL-X7K
```

---

## URL-Format

```
/promo/[release-slug]?t=[TOKEN]
```

- `release-slug` = `catalog`-Feld aus `releases.json`, lowercase (z.B. `pg-001`)
- `t` = Token aus dem PocketBase Promo-Record

---

## Was der DJ sieht

- Release-Info (Cover, Titel, Artist, Format, Genre)
- Empfängername: `FOR: DJ KOOL`
- Ablaufdatum (falls gesetzt)
- AudioPlayer mit 128k Streaming
- Download-Buttons: Einzeltracks (128K / 320K) + ZIP aller Tracks
- Feedback-Formular (Name, Email, Freitext)
- Alle bisherigen Feedbacks zu diesem Release

---

## Collections

### `promos`

Jede Promo = ein DJ-Zugang für ein Release.

| Feld | Typ | Regel |
|---|---|---|
| `token` | Text, Unique | — |
| `release_slug` | Text | — |
| `recipient_name` | Text | — |
| `recipient_email` | Email | optional |
| `notes` | Text | optional, intern |
| `expires_at` | Date | optional |

**API Rules:** List/View öffentlich (leerer String) — Astro liest ohne Auth-Token.

### `feedback`

Ein Eintrag pro DJ-Feedback. Relation zu `promos`.

| Feld | Typ |
|---|---|
| `promo` | Relation → promos |
| `name` | Text |
| `email` | Email |
| `comment` | Text |
| `user_agent` | Text (auto) |
| `ip` | Text (auto) |

**API Rules:** List/View/Create öffentlich — DJs schreiben direkt, Label liest in Admin.

### `download_events`

Automatisch geloggt bei jedem Download. Nur in Admin sichtbar.

| Feld | Typ |
|---|---|
| `promo` | Relation → promos |
| `quality` | Select: `128` / `320` |
| `user_agent` | Text |
| `ip` | Text |

---

## Download-Endpoints

### Einzeltrack

```
GET /api/promo/download?t=TOKEN&q=128&track=1
```

Antwortet mit MP3-Datei direkt (Content-Disposition: attachment).

### ZIP alle Tracks

```
GET /api/promo/download?t=TOKEN&q=320
```

Streamt ZIP-Archiv aller Tracks in der gewählten Qualität.
Filename-Format: `pg-001_input_null_320k.zip`

---

## Sicherheit

- Token wird serverseitig gegen PocketBase validiert (nie im Client)
- `release_slug` im URL muss mit dem `release_slug` im Promo-Record übereinstimmen
- Abgelaufene Promos zeigen 410-Fehlerseite
- PocketBase ist intern (ClusterIP) — nur über Ingress `pb.phantom-grid.de` erreichbar
- Download-Events werden geloggt (IP + User-Agent)

---

## Migrations

Liegen in `tools/pocketbase/pb_migrations/` und werden beim PocketBase-Start automatisch angewendet:

| Datei | Beschreibung |
|---|---|
| `1_create_promos.js` | promos Collection |
| `2_create_feedback.js` | feedback Collection |
| `3_create_download_events.js` | download_events Collection |

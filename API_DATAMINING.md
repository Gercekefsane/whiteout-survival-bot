# Whiteout Survival — API Change Timeline

![log append-only](https://img.shields.io/badge/log-append--only-57606a?style=flat-square)
![last change 21/07/2026](https://img.shields.io/badge/last%20change-21%2F07%2F2026-cf222e?style=flat-square)

An **append-only** record of every change we observe in Whiteout Survival's gift-code API. Entries are only ever added — nothing is edited or deleted — so a removed endpoint or a retired payload shape keeps its row here permanently. Newest first.

> [!IMPORTANT]
> **Append-only guarantee.** No row is ever removed from this log. When the backend drops an endpoint or the frontend changes a payload, we add a new line; we never rewrite history. The git commit trail of this file is itself part of the record.

**Change types** — ![added](https://img.shields.io/badge/added-2ea44f?style=flat-square) new endpoint or parameter &nbsp;·&nbsp; ![changed](https://img.shields.io/badge/changed-bf8700?style=flat-square) method or payload changed &nbsp;·&nbsp; ![removed](https://img.shields.io/badge/removed-cf222e?style=flat-square) backend stopped answering (404)

---

| Date (UTC) | Endpoint | Change | Detail |
|---|---|:--:|---|
| 21/07/2026 11:00 | `/player` | ![removed](https://img.shields.io/badge/removed-cf222e?style=flat-square) | backend returns 404 — Century Games API change (dropped from the redeem flow) |
| 21/07/2026 10:59 | `/captcha` | ![removed](https://img.shields.io/badge/removed-cf222e?style=flat-square) | backend returns 404 — Century Games API change (dropped from the redeem flow) |

<sub>The oldest rows are the **seeded baseline** — the known state captured when scanning began (the backend had already dropped these paths in a Century Games API change). Every row after the baseline is appended automatically by the daily scan.</sub>

## Notes

> [!NOTE]
> Payload changes are detected against a **per-bundle key set**, not per endpoint: minification hides which key belongs to which endpoint, so a payload delta reflects the whole chunk. Backend removals are recorded even though the affected paths remain **referenced by the frontend** — that gap is exactly what this log exists to make visible.

See the current surface, encrypt key and signature scheme in **[API_ENDPOINTS.md](API_ENDPOINTS.md)**.

<sub>Datamined from Century Games' public gift-code client · Whiteout Survival · read-only, append-only.</sub>
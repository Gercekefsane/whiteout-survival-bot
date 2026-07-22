# Whiteout Survival — Live API Surface

![endpoints 4](https://img.shields.io/badge/endpoints-4-57606a?style=flat-square)
![live 2](https://img.shields.io/badge/live-2-2ea44f?style=flat-square)
![removed 2](https://img.shields.io/badge/removed-2-cf222e?style=flat-square)
![scan read-only](https://img.shields.io/badge/scan-read--only-57606a?style=flat-square)

<sub>Backend `wos-giftcode-api.centurygame.com/api` &nbsp;·&nbsp; frontend `wos-giftcode.centurygame.com` &nbsp;·&nbsp; bundle `app.6ca559b45b5fb0de.js` &nbsp;·&nbsp; last scanned 22/07/2026 13:35 UTC</sub>

This document mirrors the gift-code API of **Whiteout Survival** exactly as the game's own public web client describes it — the endpoints its frontend calls, which of them the backend still answers, the request parameters, the encrypt key, and the signature scheme. It is produced by an automated scan that only reads Century Games' public JavaScript and probes their public API. We observe; we never modify the game's API, and never touch our own redemption keys.

---

## Endpoints

| Endpoint | Method | Backend | Payload keys[¹](#reading-the-payload-keys) |
|---|:--:|:--:|---|
| `/gift_code` | `POST` | ![live](https://img.shields.io/badge/live-2ea44f?style=flat-square) | `captcha_code` `cdk` `code` `fid` `init` `kid` `lang` `sign` `time` |
| `/gift_code_config` | `POST` | ![live](https://img.shields.io/badge/live-2ea44f?style=flat-square) | — |
| `/captcha` | `GET` | ![removed](https://img.shields.io/badge/removed-cf222e?style=flat-square) | `captcha_code` `cdk` `code` `fid` `init` `kid` `lang` `sign` `time` |
| `/player` | `POST` | ![removed](https://img.shields.io/badge/removed-cf222e?style=flat-square) | `captcha_code` `cdk` `code` `fid` `init` `kid` `lang` `sign` `time` |

<sub>**Backend** is probed with a deliberately invalid, side-effect-free body and classified purely on HTTP status — `live` = the host answered (any 2xx/4xx other than 404), `removed` = the host returns 404. The **Method** column is the verb the frontend uses; the liveness probe always POSTs, and a 404 comes back regardless of verb, so it cleanly proves removal.</sub>

> [!IMPORTANT]
> **Every `removed` path above is still shipped in the frontend bundle.** Century Games dropped the server route but left the calling code in the web client, so the path keeps being referenced even though the backend answers 404. Each removal is dated in the [change timeline](API_DATAMINING.md).

<details>
<summary><b>Verify it yourself</b> — read-only, one status probe per path</summary>

The body redeems nothing (invalid `fid`/`time`); only the HTTP status is read.

```bash
for p in gift_code gift_code_config captcha player; do
  code=$(curl -s -o /dev/null -w '%{http_code}' \
    -X POST "https://wos-giftcode-api.centurygame.com/api/$p" -d 'fid=0&time=0')
  echo "$code  /$p"
done
# expect: 200 /gift_code · 200 /gift_code_config · 404 /captcha · 404 /player
```

</details>

---

## Signature scheme

```
sign = MD5("cdk={cdk}&fid={fid}&kid={kid}&time={time}" + ENCRYPT_KEY)
params alphabetical; time in unix SECONDS; kid required; no captcha_code. (Century Games' own scheme, visible in their public JS.)
```

The formula cannot be lifted reliably from minified JavaScript, so it is maintained by hand and re-verified on each contract change **(last verified 21/07/2026)**. It is Century Games' own scheme, reproduced here for transparency only.

---

## Encrypt key

```
tB87#kPtkxqOS2
```

This is the `ENCRYPT_KEY` appended before the MD5 hash above. It belongs to Century Games and ships in their public web client; we surface it for transparency, we do not own it, and the scanner never writes it back into our redemption config.

---

## Reading the payload keys

Payload keys are extracted as **one set per bundle chunk, not per endpoint**. The client is minified, which erases the link between a request parameter and the exact endpoint that sends it. We therefore report the chunk-wide key set and attach it to every signing endpoint — the table does **not** claim that `/player` sends precisely these keys, only that they occur in the same chunk. Read-only config reads (`/gift_code_config`) carry no signed payload and show `—`. Methods are inferred from the bundle by a substring heuristic and re-checked on change.

---

## Error codes

![codes 17](https://img.shields.io/badge/codes-17-57606a?style=flat-square)
![flow signed v2](https://img.shields.io/badge/flow-signed%20v2-2ea44f?style=flat-square)
![source observed](https://img.shields.io/badge/source-observed-57606a?style=flat-square)

How **Whiteout Survival**'s gift-code backend replies, and what our redeemer does with each reply. These are **our own observations** of Century Games' `err_code` values — read off our redemption handler, **not** produced by the scanner — so this table is hand-maintained. `terminal` = we stop; `auto-retry` = transient, we back off and try again; `needs review` = we stop and never delete anything, a human corrects it.

| `err_code` | Our label | Handling | What it means |
|---|---|:--:|---|
| `20000` | SUCCESS | ![success](https://img.shields.io/badge/success-2ea44f?style=flat-square) | Code redeemed for this player. We mark the player's kingdom verified and stop. |
| `40008` | ALREADY_USED | ![terminal](https://img.shields.io/badge/terminal-57606a?style=flat-square) | This player has already claimed this code. Treated as done, not an error. |
| `40005` | LIMIT_REACHED | ![terminal](https://img.shields.io/badge/terminal-57606a?style=flat-square) | The code's global redemption cap is exhausted; we mark the code `limit_reached`. |
| `40007` | TIME_ERROR | ![terminal](https://img.shields.io/badge/terminal-57606a?style=flat-square) | The code has expired; we mark the code `expired`. |
| `40014` | CDK_NOT_FOUND | ![terminal](https://img.shields.io/badge/terminal-57606a?style=flat-square) | The code does not exist / is invalid; we mark the code `invalid`. |
| `40006` | USAGE_LIMIT · TOO_SMALL_SPEND_MORE | ![terminal](https://img.shields.io/badge/terminal-57606a?style=flat-square) | Usage limit for this player — or, when the message mentions STOVE, a spend-more gate. |
| `40010` | TOO_SMALL_SPEND_MORE | ![terminal](https://img.shields.io/badge/terminal-57606a?style=flat-square) | Player level / spend too low to redeem this code. |
| `40011` | SAME_TYPE_EXCHANGE | ![terminal](https://img.shields.io/badge/terminal-57606a?style=flat-square) | Player already received a reward of the same type. |
| `40020` | KID_MISMATCH | ![needs review](https://img.shields.io/badge/needs%20review-cf222e?style=flat-square) | The kingdom id we sent does not match this player's real kingdom (they transferred), OR the player id does not exist — the API cannot tell those apart. We never retry it and never delete the player; a human corrects the kingdom. |
| `40019` | — (per-FID throttle) | ![auto-retry](https://img.shields.io/badge/auto--retry-bf8700?style=flat-square) | Century Games' OWN per-player throttle: this FID redeemed too frequently. Game-enforced, not ours. We wait 5 s and retry (in the active flow). Must never be read as `40020`. |

> [!IMPORTANT]
> **`40019` is the game's own per-FID throttle, not our pacing.** It means one player redeemed too frequently; Century Games — not us — pushes back. We wait 5 s and retry. It must never be confused with `40020` (`KID_MISMATCH`): reading a throttle as a kingdom mismatch would wrongly flag healthy players. See [Rate limits](#rate-limits).

<details>
<summary><b>Legacy captcha-flow codes</b> — only when the captcha fallback is enabled (`GIFTCODE_REDEEM_V2=False`)</summary>

The active flow is the signed single-call API (no login, no captcha). Century Games' 2026-07-21 change removed `/player` and `/captcha`, so the codes below are reachable only in the preserved captcha fallback, kept for revival. In the current live flow you will not see them.

| `err_code` | Our label | Handling | What it means |
|---|---|:--:|---|
| `40001` | ROLE_NOT_EXIST | ![terminal](https://img.shields.io/badge/terminal-57606a?style=flat-square) | Login step: this player's role does not exist. Permanent — no retry. |
| `40009` | — (session expired) | ![auto-retry](https://img.shields.io/badge/auto--retry-bf8700?style=flat-square) | Session/login expired; we get a fresh session and retry. |
| `40004` | — (captcha wrong) | ![auto-retry](https://img.shields.io/badge/auto--retry-bf8700?style=flat-square) | Captcha solved wrong; we fetch a fresh captcha and retry. |
| `40102` | — (captcha expired) | ![auto-retry](https://img.shields.io/badge/auto--retry-bf8700?style=flat-square) | Captcha expired before submit; new captcha, retry. |
| `40103` | — (captcha error) | ![auto-retry](https://img.shields.io/badge/auto--retry-bf8700?style=flat-square) | Captcha rejected; new captcha, retry. |
| `40100` | — (captcha rate limit) | ![auto-retry](https://img.shields.io/badge/auto--retry-bf8700?style=flat-square) | Captcha endpoint rate-limited; we rotate to a new proxy/session and retry. |
| `40101` | — (rate limited) | ![auto-retry](https://img.shields.io/badge/auto--retry-bf8700?style=flat-square) | Rate-limited; rotate proxy/session and retry. |

</details>

<sub>Handling is what **our** redeemer does; the `err_code` numbers and their meanings belong to Century Games. We observe and react — we never change the game's responses. A note on `40019` retry: the active signed flow retries it after 5 s; the legacy KS captcha branch does not (it surfaces `ERROR_40019` instead).</sub>

---

## Rate limits

![game throttle per-FID 40019](https://img.shields.io/badge/game%20throttle-per--FID%2040019-bf8700?style=flat-square)
![our pacing concurrency + backoff](https://img.shields.io/badge/our%20pacing-concurrency%20+%20backoff-57606a?style=flat-square)
![fixed rps none](https://img.shields.io/badge/fixed%20rps-none-57606a?style=flat-square)

The game enforces exactly one limit on us: err `40019`, a per-FID (per-player) throttle. It is unaffected by how many DIFFERENT players we process at once, so our concurrency ceiling is our proxy pool, not the game. Every request also exits through a **rotating proxy pool** (a different IP per call), so we are not hammering the API from one address, and there is **no fixed requests-per-second limiter** in the redeem path.

| Control | Value | What it bounds | Side |
|---|:--:|---|:--:|
| Concurrency ceiling | `200` | Max simultaneous game-API calls, system-wide (semaphore). | ![our pacing](https://img.shields.io/badge/our%20pacing-57606a?style=flat-square) |
| Per-batch fan-out | `100` | Redemptions dispatched at once per alliance batch. | ![our pacing](https://img.shields.io/badge/our%20pacing-57606a?style=flat-square) |
| API redeem jobs | `25` | Concurrent website/API redeem jobs. | ![our pacing](https://img.shields.io/badge/our%20pacing-57606a?style=flat-square) |
| Retry attempts | `3` | Attempts per redemption before we give up. | ![our pacing](https://img.shields.io/badge/our%20pacing-57606a?style=flat-square) |
| Retry backoff | `5 s / 2 s` | Wait between attempts: 5 s after a `40019` throttle, 2 s otherwise. | ![our pacing](https://img.shields.io/badge/our%20pacing-57606a?style=flat-square) |
| Job-dispatch pacing | `0.5 s` | Gap between picking successive queued jobs off the API queue. | ![our pacing](https://img.shields.io/badge/our%20pacing-57606a?style=flat-square) |
| Scheduler yield | `0.1 s` | Cooperative yield between players in a web batch (not a rate limit). | ![our pacing](https://img.shields.io/badge/our%20pacing-57606a?style=flat-square) |
| Per-FID throttle | `err 40019` | Century Games caps how often ONE player FID may redeem. | ![game-enforced](https://img.shields.io/badge/game--enforced-bf8700?style=flat-square) |

> [!NOTE]
> **One game limit, the rest is ours.** The only throttle Century Games imposes is the per-FID `40019` above; every other row is our own concurrency budget or a cooperative delay, tuned to the proxy pool (~250 concurrent exits) rather than to the game.

<sub>A separate background **auto-retry** loop for failed codes uses a longer `15 s → 30 s → 60 s` backoff; that is a housekeeping sweep, not the live redeem path (which uses the 5 s / 2 s backoff above). Two older `GIFTCODE_RATE_LIMIT_*` settings still sit in the config file but are **dead** — nothing reads them — so they are deliberately omitted here.</sub>

---

## Scope

The scanner is read-and-report only. It writes to two database tables and to these public documents — never to `api_keys.json`, `config.py`, or the redeem path. The full change history lives in the append-only [change timeline](API_DATAMINING.md).

<sub>Generated from Century Games' public gift-code client · Whiteout Survival · scan is read-only.</sub>
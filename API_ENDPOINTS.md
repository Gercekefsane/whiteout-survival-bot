# Whiteout Survival — Live API Surface

![endpoints 4](https://img.shields.io/badge/endpoints-4-57606a?style=flat-square)
![live 2](https://img.shields.io/badge/live-2-2ea44f?style=flat-square)
![removed 2](https://img.shields.io/badge/removed-2-cf222e?style=flat-square)
![scan read-only](https://img.shields.io/badge/scan-read--only-57606a?style=flat-square)

<sub>Backend `wos-giftcode-api.centurygame.com/api` &nbsp;·&nbsp; frontend `wos-giftcode.centurygame.com` &nbsp;·&nbsp; bundle `app.6ca559b45b5fb0de.js` &nbsp;·&nbsp; last scanned 22/07/2026 13:02 UTC</sub>

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

## Scope

The scanner is read-and-report only. It writes to two database tables and to these public documents — never to `api_keys.json`, `config.py`, or the redeem path. The full change history lives in the append-only [change timeline](API_DATAMINING.md).

<sub>Generated from Century Games' public gift-code client · Whiteout Survival · scan is read-only.</sub>
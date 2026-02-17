---
title: WhiteOut Survival Bot Technical Architecture - Python, PostgreSQL, Telegram, Discord
description: Technical documentation for WhiteOut Survival Bot covering system architecture, tech stack, module design, database schema, and API integration
keywords: whiteout survival bot architecture, python telegram bot, discord bot, postgresql, async python, gift code api, wos bot tech stack, dual bot architecture, multi-language bot
---

# ❄️ WhiteOut Survival Bot — Technical Architecture

## System Overview

```
┌───────────────────────────────────────────────────────────────┐
│                      WhiteBot Server                          │
│                                                               │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────────┐ │
│  │  Telegram    │  │   Discord    │  │   Background Tasks   │ │
│  │  Bot API     │  │   Bot API   │  │                      │ │
│  │  (PTB v21)   │  │  (dpy v2)   │  │  • Gift Code Loop   │ │
│  │              │  │              │  │  • Control Loop      │ │
│  │  Commands    │  │  Slash Cmds  │  │  • Retry Queue       │ │
│  │  Callbacks   │  │  Events     │  │  • Event Scheduler   │ │
│  └──────┬───────┘  └──────┬──────┘  └──────────┬───────────┘ │
│         │                 │                     │             │
│         └────────────┬────┴─────────────────────┘             │
│                      │                                        │
│              ┌───────▼────────┐                               │
│              │   PostgreSQL   │                               │
│              │   Database     │                               │
│              │                │                               │
│              │  • users       │                               │
│              │  • alliance_list│                              │
│              │  • gift_codes  │                               │
│              │  • user_giftcodes│                             │
│              │  • alliancesettings│                           │
│              │  • botsettings │                               │
│              └────────────────┘                               │
└───────────────────────────────────────────────────────────────┘
```

## Core Technologies

### Python 3.11+
- **Async/await** throughout the entire codebase
- Type hints for better code quality
- f-string formatting for message templates
- `asyncio` for concurrent task management

### python-telegram-bot v21
- Async-native Telegram Bot API wrapper
- `ConversationHandler` for multi-step flows (e.g., setupalliance)
- `InlineKeyboardMarkup` for interactive menus
- `CallbackQueryHandler` for button interactions
- HTML parse mode for rich message formatting

### discord.py v2.x
- Slash command integration (`app_commands`)
- `discord.Embed` for rich message display
- `discord.ui.View` for interactive components
- Cross-thread communication with `run_coroutine_threadsafe`

### PostgreSQL 15+
- Primary data store for all bot data
- Connection pooling with `psycopg2`
- Composite primary keys for multi-game support: `(fid, game_type)`
- `ON CONFLICT` upserts for idempotent operations
- Indexed queries for fast member lookups

### aiohttp
- Async HTTP client for game API calls
- Concurrent API requests with `asyncio.gather`
- Timeout handling for unreliable endpoints
- Session management for connection reuse

### cloudscraper
- Cloudflare bypass for protected endpoints
- TLS fingerprint mimicking
- Used for Kingshot gift code API access

## Module Architecture

```
whitebot/
├── bot.py                  # Main entry point, handlers, dual-bot startup
├── config.py               # API keys, tokens, URLs
├── shared_state.py         # Cross-module bot references
├── setup_db.py             # Database schema creation
├── modules/
│   ├── common.py           # Shared utilities, API functions, game configs
│   ├── registration.py     # /register command, user registration logic
│   ├── members.py          # /addmember, /removemember, /bulkadd, /profile
│   ├── alliance.py         # /setupalliance, alliance CRUD
│   ├── giftcode.py         # Gift code discovery, validation, redemption
│   ├── control.py          # Member monitoring, change detection
│   ├── idchannel.py        # ID channel auto-registration
│   └── member_tracking.py  # Premium tracking, rate limiting
├── locales/
│   ├── en.json             # English strings
│   ├── tr.json             # Turkish strings
│   └── ru.json             # Russian strings
└── db/
    └── migrate_game_type.py # Database migration scripts
```

## Key Design Decisions

### Single Process, Dual Bot
Both Telegram and Discord bots run in the **same Python process**:
- Telegram uses `asyncio` event loop
- Discord runs in a **separate thread** with its own event loop
- `shared_state.py` provides cross-module access to both bot instances
- `asyncio.run_coroutine_threadsafe` bridges between event loops

### Game-Type Aware Database
Every table that stores user or code data includes a `game_type` column:
- Allows a single database to serve both WhiteOut Survival and Kingshot
- Composite primary keys prevent FID collisions between games
- Queries are always scoped by `game_type` for data isolation

### Locale System
- JSON-based locale files (one per language)
- `get_text(key, lang)` function for string retrieval
- Per-group language setting stored in `alliancesettings`
- Fallback to English if key is missing in target language

### Connection Pooling
- PostgreSQL connections are pooled at startup
- Synchronous `db.execute()` / `db.fetchone()` / `db.fetchall()` wrappers
- Thread-safe for cross-bot access

## External APIs

| API | Purpose | Auth |
|-----|---------|------|
| WhiteOut Survival Player API | Player info lookup | Sign + FID |
| WhiteOut Survival Gift Code API | Code redemption | Sign + CAPTCHA |
| Kingshot Player API | Player info lookup | Encrypt key + FID |
| Kingshot Gift Code API | Code redemption | Encrypt key |
| kingshot.net | Gift code list (KS) | cloudscraper |
| Official Game Channels | Gift code list (WOS) | aiohttp |
| Custom Solver | CAPTCHA solving | API key |

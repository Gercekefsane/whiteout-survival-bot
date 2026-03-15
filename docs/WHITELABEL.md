# 🏷️ WhiteLabel System — Design Document

## 📋 Overview

The WhiteLabel system allows third-party users (customers) to run their own branded instances of WhiteBot using **their own Discord and Telegram bot tokens**. Each WhiteLabel instance shares the same codebase and database but operates under a separate bot identity.

This enables:
- **Custom bot names & avatars** — customers see their own brand
- **Isolated token management** — each customer provides their own tokens
- **Centralized control** — the main owner controls all WhiteLabel bots from a single dashboard
- **Revenue model** — WhiteLabel is a premium-tier offering

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────┐
│                   WhiteBot Core                       │
│  (Shared codebase, modules, database, API layer)     │
├──────────────────────────────────────────────────────┤
│                                                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │
│  │  Main Bot   │  │ WL Bot #1   │  │ WL Bot #2   │  │
│  │ (Owner)     │  │ (Customer A)│  │ (Customer B)│  │
│  │             │  │             │  │             │  │
│  │ TG Token: X │  │ TG Token: Y │  │ TG Token: Z │  │
│  │ DC Token: X │  │ DC Token: Y │  │ DC Token: Z │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  │
│        │                │                │            │
│        └────────────────┼────────────────┘            │
│                         │                             │
│              ┌──────────▼──────────┐                  │
│              │  PostgreSQL (shared) │                  │
│              │  whitelabel_bots     │                  │
│              │  whitelabel_config   │                  │
│              │  alliance_list       │                  │
│              │  users, gift_codes   │                  │
│              └─────────────────────┘                  │
└──────────────────────────────────────────────────────┘
```

---

## 📦 Database Schema

### `whitelabel_bots` — Bot instances

| Column | Type | Description |
|--------|------|-------------|
| `id` | SERIAL PK | Unique WhiteLabel ID |
| `owner_user_id` | BIGINT | Telegram user ID of the WL customer |
| `label` | VARCHAR(64) | Display name (e.g. "MyAllianceBot") |
| `telegram_token` | TEXT (encrypted) | Customer's Telegram bot token |
| `discord_token` | TEXT (encrypted) | Customer's Discord bot token |
| `telegram_username` | VARCHAR(64) | Resolved TG bot username |
| `discord_username` | VARCHAR(64) | Resolved DC bot username |
| `status` | VARCHAR(16) | `pending` / `active` / `suspended` / `stopped` |
| `plan_id` | INT FK | Premium plan assigned |
| `max_alliances` | INT | Max alliances allowed (from plan) |
| `max_members_per_alliance` | INT | Max members per alliance |
| `features` | JSONB | Feature flags (gift codes, events, map, etc.) |
| `branding` | JSONB | Custom branding (welcome message, logo URL, etc.) |
| `created_at` | TIMESTAMP | Creation date |
| `last_heartbeat` | TIMESTAMP | Last health check timestamp |
| `error_log` | TEXT | Last error message (if crashed) |

### `whitelabel_config` — Per-bot configuration overrides

| Column | Type | Description |
|--------|------|-------------|
| `bot_id` | INT FK → whitelabel_bots | Bot instance |
| `key` | VARCHAR(64) | Config key (e.g. "welcome_message") |
| `value` | TEXT | Config value |

### `whitelabel_audit_log` — Activity tracking

| Column | Type | Description |
|--------|------|-------------|
| `id` | SERIAL PK | Log ID |
| `bot_id` | INT FK | Bot instance |
| `action` | VARCHAR(32) | `start`, `stop`, `restart`, `error`, `token_change` |
| `details` | TEXT | Additional info |
| `timestamp` | TIMESTAMP | When it happened |

---

## 🔐 Security

### Token Encryption
- All tokens are encrypted at rest using **AES-256-GCM**
- Encryption key stored in environment variable `WL_ENCRYPTION_KEY`
- Tokens are only decrypted in memory when starting a bot instance
- Tokens are **never** logged or displayed in full (masked: `MTQ2...***`)

### Token Validation
Before accepting a token, the system:
1. Calls the Telegram `getMe` API / Discord gateway to verify the token is valid
2. Checks the bot username is not already in use by another WL instance
3. Stores the resolved username for display purposes
4. Verifies the bot has necessary permissions (send messages, manage webhooks, etc.)

### Isolation
- Each WL bot runs in its own **asyncio task group** (not a separate process)
- Database queries are scoped by `bot_id` to prevent data leaks
- Rate limits are per-bot to prevent abuse

---

## 🚀 Bot Lifecycle

### 1. Registration Flow
```
Customer → /whitelabel create "MyBot"
         → Bot asks for Telegram token
         → Customer sends token
         → System validates via getMe API
         → Bot asks for Discord token
         → Customer sends token  
         → System validates via Discord API
         → WhiteLabel instance created (status: pending)
         → Owner approves → status: active
         → Bot starts automatically
```

### 2. Runtime Architecture
```python
class WhiteLabelManager:
    """Manages all WL bot instances within the main process"""
    
    def __init__(self):
        self.instances: dict[int, WhiteLabelInstance] = {}
    
    async def start_instance(self, bot_id: int):
        """Start a WL bot in a new task group"""
        config = db.fetchone("SELECT * FROM whitelabel_bots WHERE id=%s", (bot_id,))
        instance = WhiteLabelInstance(config)
        self.instances[bot_id] = instance
        asyncio.create_task(instance.run())
    
    async def stop_instance(self, bot_id: int):
        """Gracefully stop a WL bot"""
        if bot_id in self.instances:
            await self.instances[bot_id].shutdown()
            del self.instances[bot_id]
    
    async def health_check_loop(self):
        """Monitor all instances, restart crashed ones"""
        while True:
            for bot_id, instance in list(self.instances.items()):
                if not instance.is_alive():
                    await self.restart_instance(bot_id)
                instance.update_heartbeat()
            await asyncio.sleep(60)
```

### 3. Instance Startup
Each WhiteLabel instance:
1. Decrypts tokens from database
2. Validates tokens (getMe / Discord gateway)
3. Registers command handlers (shared module code)
4. Starts Telegram polling + Discord client
5. Reports status to main bot
6. Begins heartbeat loop

### 4. Graceful Shutdown
- Stop accepting new commands
- Finish in-progress gift code redemptions
- Disconnect from Telegram/Discord
- Update status in DB

---

## 🎛️ Owner Commands

| Command | Description |
|---------|-------------|
| `/wl list` | List all WhiteLabel instances with status |
| `/wl create` | Start the creation wizard |
| `/wl start [id]` | Start a stopped instance |
| `/wl stop [id]` | Stop a running instance |
| `/wl restart [id]` | Restart an instance |
| `/wl delete [id]` | Delete an instance permanently |
| `/wl status [id]` | Detailed status (uptime, errors, alliances, members) |
| `/wl logs [id]` | View recent audit log |
| `/wl config [id] [key] [value]` | Override config for an instance |
| `/wl approve [id]` | Approve a pending instance |
| `/wl suspend [id]` | Suspend a misbehaving instance |
| `/wl token [id] [tg/dc] [new_token]` | Update a token |

---

## 👤 Customer Commands

Customers interact with the **main bot** to manage their WL instance:

| Command | Description |
|---------|-------------|
| `/mybot` | View your WhiteLabel bot status |
| `/mybot token tg [token]` | Update your Telegram token |
| `/mybot token dc [token]` | Update your Discord token |
| `/mybot branding [key] [value]` | Customize welcome message, etc. |
| `/mybot restart` | Request a restart |
| `/mybot stats` | View usage statistics |

---

## 💰 Pricing Integration

WhiteLabel is a premium tier in the existing subscription system:

| Feature | Free | Premium | WhiteLabel |
|---------|------|---------|------------|
| Alliances | 1 | 5 | 10+ |
| Members/Alliance | 200 | 500 | 1000+ |
| Gift Code Auto-Redeem | ✅ | ✅ | ✅ |
| Custom Bot Name | ❌ | ❌ | ✅ |
| Custom Bot Avatar | ❌ | ❌ | ✅ |
| Custom Welcome Message | ❌ | ❌ | ✅ |
| Priority Support | ❌ | ✅ | ✅ |
| Dedicated Bot Process | ❌ | ❌ | ✅ |

---

## 📊 Monitoring Dashboard

The owner can view a real-time dashboard via `/wl dashboard`:

```
╔══════════════════════════════════════════╗
║        WhiteLabel Dashboard              ║
╠══════════════════════════════════════════╣
║                                          ║
║  Total Instances: 5                      ║
║  Active: 3  |  Stopped: 1  |  Error: 1  ║
║                                          ║
║  #1 MyAllianceBot    ✅ Active  2d 5h    ║
║     TG: @MyAllianceBot  DC: MyAlliance   ║
║     Alliances: 3  Members: 450           ║
║                                          ║
║  #2 ProGuildBot      ✅ Active  1d 12h   ║
║     TG: @ProGuildBot    DC: ProGuild     ║
║     Alliances: 5  Members: 890           ║
║                                          ║
║  #3 RU_WOS_Bot       ⛔ Error   0h       ║
║     Error: Token expired                 ║
║                                          ║
╚══════════════════════════════════════════╝
```

---

## 🔄 Feature Flags (per instance)

Each WL instance can have features enabled/disabled via JSONB `features` column:

```json
{
    "gift_codes": true,
    "auto_redeem": true,
    "bear_trap_notifications": true,
    "crazy_joe_calculator": true,
    "hero_guide": true,
    "interactive_map": false,
    "wiki_tracker": false,
    "transfer_tracker": false,
    "announcements": true,
    "control_loop": true,
    "max_concurrent_redeems": 10
}
```

---

## 🛠️ Implementation Phases

### Phase 1 — Foundation (MVP)
- [ ] DB migration: `whitelabel_bots`, `whitelabel_config`, `whitelabel_audit_log`
- [ ] Token encryption/decryption utilities
- [ ] Token validation (getMe + Discord gateway check)
- [ ] `WhiteLabelManager` class with start/stop/restart
- [ ] `/wl create` wizard (owner only)
- [ ] `/wl list`, `/wl status`, `/wl start`, `/wl stop`
- [ ] Basic health check loop with auto-restart

### Phase 2 — Customer Self-Service
- [ ] `/mybot` command for customers
- [ ] Token update flow with validation
- [ ] Branding customization (welcome message, commands prefix)
- [ ] Usage statistics per instance

### Phase 3 — Advanced Features
- [ ] Feature flags per instance
- [ ] Per-instance rate limiting
- [ ] Stripe integration for WhiteLabel tier
- [ ] Auto-suspension on payment failure
- [ ] Dashboard command with rich formatting

### Phase 4 — Scale & Reliability
- [ ] Multi-process architecture (optional: separate processes per WL bot)
- [ ] Redis-based inter-process communication
- [ ] Centralized logging (ELK or similar)
- [ ] Automated backup of WL configs
- [ ] API endpoint for external management

---

## 📁 File Structure

```
whitebot/
├── modules/
│   ├── whitelabel/
│   │   ├── __init__.py          # Module exports
│   │   ├── manager.py           # WhiteLabelManager class
│   │   ├── instance.py          # WhiteLabelInstance class
│   │   ├── crypto.py            # Token encryption/decryption
│   │   ├── validation.py        # Token validation (TG/DC APIs)
│   │   ├── commands.py          # /wl owner commands
│   │   ├── customer.py          # /mybot customer commands
│   │   └── health.py            # Health check & monitoring
│   └── ...
├── db/
│   └── migrate_whitelabel.py    # DB migration script
├── docs/
│   └── WHITELABEL.md            # This document
└── ...
```

---

## ⚡ Quick Start (for developers)

```python
# In bot.py post_init:
from modules.whitelabel.manager import WhiteLabelManager

wl_manager = WhiteLabelManager()
await wl_manager.load_active_instances()  # Load all active WL bots from DB
asyncio.create_task(wl_manager.health_check_loop())
print(f"✅ WhiteLabel: {len(wl_manager.instances)} active instances")
```

---

## 🔮 Future Considerations

- **WebSocket Dashboard** — Real-time monitoring via woscontrol.com
- **API Access** — REST API for programmatic WL management
- **Custom Domains** — Each WL bot could have its own webhook domain
- **Plugin System** — Allow WL customers to write custom command plugins
- **White-label Web Map** — Custom map.{domain}.com per instance
- **Multi-region** — Deploy WL bots in different regions for lower latency
- **Reseller Program** — Allow WL customers to resell to sub-customers

---

*Document Version: 1.0 — Created: 2026-03-14*
*Author: WhiteBot Development Team*

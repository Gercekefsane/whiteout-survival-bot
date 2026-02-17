<div align="center">

# ❄️ WhiteOut Survival Bot

### The Ultimate Gift Code & Alliance Management Bot for WhiteOut Survival

<br>

[![Add to Telegram](https://img.shields.io/badge/Telegram-Add%20Bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/WhiteoutGuildBot)
[![Add to Discord](https://img.shields.io/badge/Discord-Add%20Bot-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/oauth2/authorize?client_id=1462815590141132905&permissions=8&scope=bot%20applications.commands)
[![Contact Admin](https://img.shields.io/badge/Contact-Admin-E4405F?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/woscoupon)
[![Free Trial](https://img.shields.io/badge/Try-Free%20Trial-00C853?style=for-the-badge&logo=checkmarx&logoColor=white)](https://t.me/woscoupon)

<br>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?style=flat-square&logo=postgresql&logoColor=white)]()
[![Platform](https://img.shields.io/badge/Platform-Telegram%20%2B%20Discord-blue?style=flat-square)]()
[![Languages](https://img.shields.io/badge/Languages-EN%20%7C%20TR%20%7C%20RU-orange?style=flat-square)]()
[![Uptime](https://img.shields.io/badge/Uptime-24%2F7-brightgreen?style=flat-square)]()
[![Server](https://img.shields.io/badge/Hosting-Dedicated%20Server-critical?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Gercekefsane/whiteout-survival-bot?style=flat-square)]()

<br>

**Automatically discovers and redeems gift codes • Tracks alliance members in real-time**
**Sends furnace, nickname & state change notifications • Works on Telegram and Discord**

<br>

[✨ Features](#-features) · [⚙️ How It Works](#%EF%B8%8F-how-it-works) · [📋 Commands](#-commands) · [🚀 Get Started](#-get-started) · [🛠 Tech Stack](#-tech-stack) · [📖 Guides](#-guides) · [❓ FAQ](#-faq)

---

</div>

## ⭐ Source Code Release

> **We're planning to open-source this project!**
> The full source code will be released when this repository reaches **100 ⭐ stars**.
>
> ⭐ **Star this repo** to show your interest and help us reach the goal!
>
> Current progress: ![GitHub stars](https://img.shields.io/github/stars/Gercekefsane/whiteout-survival-bot?style=social)

---

## 🎯 What Is This?

**WhiteOut Survival Bot** is a fully automated, production-grade management bot designed specifically for **WhiteOut Survival** alliance leaders and members. It runs **24/7 on a dedicated server**, monitoring official game channels for new gift codes and redeeming them instantly for every registered member in your alliance.

The bot operates on both **Telegram** and **Discord** simultaneously, with a shared database ensuring full cross-platform synchronization. Everything from gift code redemption to member tracking is completely automated — no manual intervention required.

> 💡 **No more missed gift codes.** The bot scans official game sources every **60 minutes**, discovers new codes, validates them, and redeems them for your entire alliance automatically.

---

## ✨ Features

### 🎁 Automatic Gift Code Redemption
The bot continuously monitors official WhiteOut Survival channels and trusted community sources for newly released gift codes. When a new code is discovered, it is validated against the game's official API and automatically redeemed for **every registered member** in your alliance.

- **Automatic scanning** of official game channels every **60 minutes** (configurable)
- **Instant validation** against the official WhiteOut Survival API
- **Batch redemption** for all alliance members with **20 concurrent requests** per batch
- **Built-in CAPTCHA solver** — fully automated, no human interaction needed
- **Smart retry system** with exponential backoff for failed redemptions
- **Per-member tracking** — see exactly which codes succeeded, failed, or were already used
- **Notifications** — new code alerts are sent and **pinned** in your group automatically

### 👥 Alliance Member Management
Manage your alliance members effortlessly across Telegram and Discord. Multiple registration methods make onboarding fast and simple for both leaders and members.

- **Quick registration** — members type `/register [FID]` and they're in
- **ID Channel mode** — set a dedicated channel where members simply type their FID to auto-register
- **Bulk operations** — add or remove dozens of members at once with `/bulkadd` and `/bulkremove`
- **Cross-game detection** — the bot automatically identifies which game (WOS/Kingshot) a player belongs to
- **Alliance transfer** — members moving between alliances are handled seamlessly
- **Member export** — export your full member list as a file for external use

### 📊 Real-Time Player Monitoring
The bot checks every registered member's live game data at configurable intervals (default: **every 20 minutes**) and sends instant notifications when changes are detected.

- **🔥 Furnace level changes** — know when members upgrade their furnace (FC 1 → FC 30+)
- **📝 Nickname changes** — track when members change their in-game name
- **🌍 State migrations** — detect when members move to a different state
- **📜 Change history** — view a member's complete change log with `/playerhistory`
- **Batch processing** — monitors **10 players concurrently** per cycle for efficient API usage

### 🐻 Event Management & Bear Trap
Schedule and track in-game events, including the popular Bear Trap event. Set timers, configure reminders, and keep your alliance organized.

- **Bear Trap timer** with configurable reminders
- **Custom event scheduling** for your alliance
- **Attendance tracking** for events
- **Multi-channel alerts** — notifications in both Telegram and Discord

### 👔 Minister Scheduling System
Organize minister rotations within your alliance with automated scheduling, reminders, and conflict prevention.

### 🧮 Game Calculators
Built-in calculators for key game mechanics:
- **Troop training & promotion** (T1–T11)
- **Chief Gear upgrades** (Green to Pink, 0–5 stars)
- **Charm upgrades** (Level 0–16)
- **Hero Gear enhancement & mastery** forging

### 🌐 Multi-Platform & Multi-Language
- **Telegram + Discord** — full feature parity, shared database
- **English, Turkish, Russian** — per-group language configuration
- **Cross-platform sync** — register on Telegram, see data on Discord (and vice versa)
- **🆕 Want to add your language?** See our [Contributing Guide](CONTRIBUTING.md) — translation files are in [`/languages/`](languages/)

### 👑 Premium & Subscription System
Tiered subscription plans with configurable limits per alliance:
- Member limits, registration limits, alliance limits
- Stripe payment integration (optional)
- Usage dashboards and upgrade prompts

---

## ⚙️ How It Works

### System Architecture

```
┌───────────────────────────────────────────────────────────────────┐
│                    Dedicated Server (24/7)                         │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│   📡 Gift Code Scanner            🔄 Member Control Loop          │
│   ┌─────────────────────┐         ┌────────────────────────────┐  │
│   │ Scans official game │         │ Checks every 20 min        │  │
│   │ channels every 60min│         │ 10 players/batch           │  │
│   │ Validates via API   │         │ Detects furnace/name/state │  │
│   │ Auto-redeems codes  │         │ Sends change notifications │  │
│   │ 20 concurrent/batch │         │ Updates database           │  │
│   └─────────┬───────────┘         └─────────────┬──────────────┘  │
│             │                                   │                 │
│   ┌─────────▼───────────────────────────────────▼──────────────┐  │
│   │                    PostgreSQL Database                      │  │
│   │  users · alliance_list · gift_codes · user_giftcodes       │  │
│   │  alliancesettings · nickname_changes · furnace_changes     │  │
│   └─────────┬───────────────────────────────────┬──────────────┘  │
│             │                                   │                 │
│   ┌─────────▼───────────┐         ┌─────────────▼──────────────┐  │
│   │   Telegram Bot      │         │     Discord Bot            │  │
│   │   python-telegram-  │         │     discord.py v2          │  │
│   │   bot v21 (async)   │         │     Slash commands         │  │
│   └─────────────────────┘         └────────────────────────────┘  │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

### Gift Code Redemption Flow

```
  Official game channels scanned
              │
              ▼
     ┌─────────────────┐
     │  New code found  │
     │  & validated     │
     └────────┬────────┘
              │
     ┌────────▼────────┐
     │  Notify all      │──── 📌 Message pinned in group
     │  alliance groups │
     └────────┬────────┘
              │
     ┌────────▼────────┐
     │  Redeem for all  │──── 20 concurrent redemptions/batch
     │  members         │──── Built-in CAPTCHA solver
     └────────┬────────┘
              │
       ┌──────┴──────┐
       ▼             ▼
  ┌─────────┐  ┌──────────┐
  │✅ Success│  │❌ Failed  │
  │ Tracked │  │ Queued   │
  │ in DB   │  │ for retry│
  └─────────┘  └──────────┘
```

---

## 📋 Commands

### 👤 Player Commands
| Command | Description |
|---------|-------------|
| `/start` | 🚀 Start the bot and see overview |
| `/help` | ❓ Help and command reference |
| `/register [FID]` | 📝 Register your game account with your FID |
| `/profile` | 👤 View your player profile and stats |
| `/checkuser [FID]` | 🔍 Look up any player by their FID |
| `/codes` | 🎁 View all known gift codes and their status |
| `/language` | 🌐 Change your personal language preference |
| `/calc` | 🧮 Open game calculators (troops, gear, charms) |
| `/premium` | 👑 View subscription plan and usage limits |
| `/support` | 💬 Contact support |

### 🏰 Alliance Management
| Command | Description |
|---------|-------------|
| `/setupalliance` | 🏗️ Create a new alliance (interactive guided setup) |
| `/alliance` | 🏰 View alliance information |
| `/alliancetag [NEW]` | 🏷️ Change your alliance tag |
| `/alliancename [NEW]` | ✏️ Change your alliance name |
| `/setgroup` | 🔗 Link current Telegram group to an alliance |
| `/getlinkcode` | 🔑 Get code to link Discord server |
| `/unlinkdiscord` | 🔓 Remove Discord link |
| `/settings` | ⚙️ Alliance settings panel |

### 👥 Member Operations
| Command | Description |
|---------|-------------|
| `/addmember [FID] [TAG]` | ➕ Add a member to your alliance |
| `/removemember [FID] [TAG]` | ➖ Remove a member from your alliance |
| `/members [TAG]` | 👥 View all members in an alliance |
| `/bulkadd [FIDs] [TAG]` | 📥 Bulk add multiple members at once |
| `/bulkremove [FIDs] [TAG]` | 📤 Bulk remove multiple members |

### 📊 Monitoring & Tracking
| Command | Description |
|---------|-------------|
| `/startcontrol` | ▶️ Start automatic member monitoring |
| `/stopcontrol` | ⏹️ Stop automatic monitoring |
| `/setinterval [MIN]` | ⏱️ Set monitoring check interval (minutes) |
| `/changes` | 📝 View recent member changes |
| `/playerhistory [FID]` | 🕵️ View a player's full change history |

### 📅 Events
| Command | Description |
|---------|-------------|
| `/events` | 📅 View scheduled events |
| `/addevent` | 📆 Add a new event |
| `/attendance` | 📋 Track event attendance |

### 🛡️ Admin Tools
| Command | Description |
|---------|-------------|
| `/admins` | 🛡️ Manage alliance admins |
| `/setgrouplang` | 🌍 Change group language |
| `/usecode [CODE]` | 🎫 Manually use a gift code for your alliance |
| `/addcode [CODE]` | 📌 Manually add a gift code |

---

## 🚀 Get Started

### Quick Setup (5 minutes)

**1.** Add the bot to your Telegram group or Discord server
**2.** Run `/setupalliance` and follow the guided setup
**3.** Have your members type `/register [FID]` (or set up an ID channel)
**4.** Enable auto-monitoring with `/startcontrol`
**5.** Gift codes are redeemed automatically — sit back and relax! 🎉

### Add to Telegram

[![Add to Telegram](https://img.shields.io/badge/Add%20to%20Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/WhiteoutGuildBot)

> Search for `@WhiteoutGuildBot` in Telegram, or click the button above. Add the bot to your alliance group and run `/start`.

### Add to Discord

[![Add to Discord](https://img.shields.io/badge/Add%20to%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/oauth2/authorize?client_id=1462815590141132905&permissions=8&scope=bot%20applications.commands)

> Click the button above to invite the bot with administrator permissions. Use `/start` in your server to begin.

### 🆓 Free Trial

Want to try before committing? Contact us for a **free trial** with full access to all features:

[![Request Free Trial](https://img.shields.io/badge/Request%20Free%20Trial-00C853?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/woscoupon)

---

## 📖 Guides

### How to Find Your FID

Your **FID (Fighter ID)** is your unique player identifier in WhiteOut Survival.

1. Open **WhiteOut Survival**
2. Tap your **avatar** in the top-left corner
3. Your **FID** is displayed below your nickname

<!-- TODO: Add screenshot image -->
<!-- ![How to find FID](docs/images/how-to-find-fid.png) -->

> 💡 Your FID is a number like `123456789`. Copy it and use `/register 123456789` to register with the bot.

📖 **More Guides:**
- [Detailed Feature Documentation](docs/FEATURES.md) — in-depth explanation of all features
- [Technical Architecture](docs/TECH_STACK.md) — how the bot is built under the hood
- [How to Find Your FID](docs/HOW_TO_FIND_FID.md) — step-by-step visual guide
- [🌐 Add a New Language](CONTRIBUTING.md) — contribute translations to the bot

---

## 🛠 Tech Stack

| Component | Technology | Details |
|-----------|-----------|---------|
| **Language** | Python 3.11+ | Fully async/await architecture |
| **Telegram API** | python-telegram-bot v21 | Async-native, conversation handlers |
| **Discord API** | discord.py v2.x | Slash commands, embeds, views |
| **Database** | PostgreSQL 15+ | Connection pooling, composite keys |
| **HTTP Client** | aiohttp | Async API calls, session management |
| **Cloudflare Bypass** | cloudscraper | TLS fingerprint mimicking |
| **CAPTCHA Solver** | 2captcha integration | Automated image CAPTCHA solving |
| **Proxy** | Webshare rotating proxies | Rate limit avoidance |
| **Hosting** | Dedicated Server | 24/7 uptime, Windows Server |
| **Payments** | Stripe (optional) | Subscription management |

### Performance Configuration

| Parameter | Value | Description |
|-----------|-------|-------------|
| Gift Code Scan Interval | **60 minutes** | How often new codes are checked |
| Member Check Interval | **20 minutes** | Default alliance monitoring interval |
| Control Loop Frequency | **60 seconds** | Main loop tick rate |
| API Batch Size | **10 concurrent** | Player data fetch parallelism |
| Gift Code Batch Size | **20 concurrent** | Code redemption parallelism |

### Architecture Highlights
- **Single-process dual-bot** — Telegram and Discord run concurrently in one process
- **Shared PostgreSQL database** — full cross-platform data consistency
- **Modular design** — separate modules for registration, gift codes, control, alliance, events, premium
- **Multi-language locale system** — JSON-based, per-group language settings (EN/TR/RU)
- **Game-type awareness** — all operations scoped by game type for multi-game support
- **Rate limiting** — respectful API usage with configurable batch sizes and delays
- **Rotating proxies** — distributed requests to avoid IP-based rate limits

---

## 📊 Bot Statistics

| Metric | Value |
|--------|-------|
| 👥 Registered Players | **210+** |
| 🏰 Active Alliances | **6** |
| 💬 Telegram Groups | **4** |
| 🎮 Discord Servers | **1** |
| ⏱ Uptime | **24/7** |
| 🖥 Infrastructure | **Dedicated Server** |

---

## ❓ FAQ

<details>
<summary><b>How do I find my FID (Fighter ID)?</b></summary>

Open WhiteOut Survival → Tap your avatar (top-left corner) → Your FID is displayed below your nickname. It's a number like `123456789`.

See our [visual guide](docs/HOW_TO_FIND_FID.md) for step-by-step instructions with screenshots.
</details>

<details>
<summary><b>Is this bot safe to use?</b></summary>

Absolutely. The bot uses the **official gift code redemption API** — the exact same API that the game's own website uses. It does **not** access your game account, modify your game data, or require your password. Your FID is a public identifier, not a login credential.
</details>

<details>
<summary><b>How often does the bot check for new gift codes?</b></summary>

The bot scans official game channels every **60 minutes** by default. When a new code is discovered, it is validated and redeemed for all registered members within minutes. The scan interval is configurable by the bot administrator.
</details>

<details>
<summary><b>Can I use this bot for multiple alliances?</b></summary>

Yes! You can manage multiple alliances from a single bot. Each alliance has its own configuration, member list, monitoring interval, language setting, and notification channels. Premium plans allow managing even more alliances with higher member limits.
</details>

<details>
<summary><b>What languages are supported?</b></summary>

The bot currently supports **English**, **Turkish** (Türkçe), and **Russian** (Русский). Each group or user can independently set their preferred language. All messages, buttons, and notifications are fully localized.
</details>

<details>
<summary><b>Does this bot work on both Telegram and Discord?</b></summary>

Yes! The bot runs on both platforms simultaneously with a shared database. You can register on Telegram and your data will be available on Discord too. Alliance settings, member lists, and gift code tracking are fully synchronized.
</details>

<details>
<summary><b>How does the member monitoring work?</b></summary>

Once you enable monitoring with `/startcontrol`, the bot checks each registered member's live game data every **20 minutes** (configurable with `/setinterval`). When it detects a change in furnace level, nickname, or state, it sends an instant notification to your alliance's Telegram/Discord channel.
</details>

<details>
<summary><b>How do I get started?</b></summary>

1. Add the bot to your group (Telegram) or server (Discord)
2. Run `/setupalliance` to create your alliance
3. Have members register with `/register [FID]`
4. Enable monitoring with `/startcontrol`
5. Gift codes are handled automatically!

Need help? [Contact us](https://t.me/woscoupon)
</details>

---

## 📞 Contact & Support

[![Contact Admin](https://img.shields.io/badge/Contact%20Admin-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/woscoupon)

- **Support Channel**: [t.me/woscoupon](https://t.me/woscoupon)
- **Bot**: [@WhiteoutGuildBot](https://t.me/WhiteoutGuildBot)
- **Free Trial**: [Request here](https://t.me/woscoupon)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❄️ for the WhiteOut Survival community**

<br>

[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-2CA5E0?style=flat-square&logo=telegram)](https://t.me/WhiteoutGuildBot)
[![Discord Bot](https://img.shields.io/badge/Discord-Bot-5865F2?style=flat-square&logo=discord)](https://discord.com/oauth2/authorize?client_id=1462815590141132905&permissions=8&scope=bot%20applications.commands)
[![Contact](https://img.shields.io/badge/Contact-Admin-E4405F?style=flat-square&logo=telegram)](https://t.me/woscoupon)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

<br>

**WhiteOut Survival** · **WOS Bot** · **Gift Code Bot** · **Alliance Management** · **Auto Redeem**
**Telegram Bot** · **Discord Bot** · **Free Gift Codes** · **Furnace Tracker** · **WOS Helper**

</div>

<div align="center">

<a href="https://woscontrol.com">
<h1>🌐 woscontrol.com</h1>
<h3>Whiteout Survival & Kingshot Bot Platform</h3>
</a>

<br>

<a href="https://woscontrol.com">
<img src="https://img.shields.io/badge/🌐_VISIT-woscontrol%2Ecom-FF6600?style=for-the-badge&labelColor=000000&logoColor=white" alt="woscontrol.com" height="60">
</a>

<br><br>

# ❄️ WhiteOut Survival Bot

### The Ultimate Gift Code & Alliance Management Bot for WhiteOut Survival

<br>

[![Add to Telegram](https://img.shields.io/badge/Telegram-Add%20Bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/WhiteoutGuildBot)
[![Add to Discord](https://img.shields.io/badge/Discord-Add%20Bot-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/oauth2/authorize?client_id=1462815590141132905&permissions=8&scope=bot%20applications.commands)
[![Contact Admin](https://img.shields.io/badge/Contact-Admin-E4405F?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/btuncsiper)
[![Free Trial](https://img.shields.io/badge/Try-Free%20Trial-00C853?style=for-the-badge&logo=checkmarx&logoColor=white)](https://t.me/btuncsiper)

<br>

[![Version](https://img.shields.io/badge/version-v1.11.0-brightgreen?style=flat-square)]()
[![Changelog](https://img.shields.io/badge/changelog-v1.11.0-blue?style=flat-square)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?style=flat-square&logo=postgresql&logoColor=white)]()
[![Platform](https://img.shields.io/badge/Platform-Telegram%20%2B%20Discord-blue?style=flat-square)]()
[![Languages](https://img.shields.io/badge/Languages-EN%20%7C%20KO%20%7C%20RU%20%7C%20TR-orange?style=flat-square)](locales/)
[![Uptime](https://img.shields.io/badge/Uptime-24%2F7-brightgreen?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Gercekefsane/whiteout-survival-bot?style=flat-square)]()

<br>

**Automatically discovers and redeems gift codes • Tracks alliance members in real-time**
**Sends furnace, nickname & state change notifications • Works on Telegram and Discord**

<br>

[✨ Features](#-features) · [⚙️ How It Works](#%EF%B8%8F-how-it-works) · [📋 Commands](#-commands) · [🔄 Transfer](#-kingdom-transfer-system) · [🤪 Crazy Joe](#-crazy-joe-event-guide) · [🚀 Get Started](#-get-started) · [📋 Changelog](CHANGELOG.md) · [❓ FAQ](#-faq)

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

## 🔢 Latest Version: v1.11.0

> **Released:** 2026-03-15

  - **Alliance Leaderboard**: /leaderboard — Furnace rankings, top growers, alliance overview stats
  - **Inactive Member Detection**: /inactive [days] — Find members with no activity in last N days
  - **Gift Code Statistics**: /codestats — Detailed redemption stats per code
  - **WhiteLabel System**: Full bot management with /wl commands and /mybot customer view

> 📋 **[Full Changelog →](CHANGELOG.md)**

---

## 🎯 What Is This?
**WhiteOut Survival Bot** is a fully automated, production-grade management bot designed specifically for **WhiteOut Survival** alliance leaders and members. It runs **24/7 on a dedicated server**, monitoring official game channels for new gift codes and redeeming them instantly for every registered member in your alliance.

The bot operates on both **Telegram** and **Discord** simultaneously, with a shared database ensuring full cross-platform synchronization. Everything from gift code redemption to member tracking is completely automated — no manual intervention required.

> 💡 **No more missed gift codes.** The bot scans official game sources every **5 minutes**, discovers new codes, validates them, and redeems them for your entire alliance automatically.

---

## ✨ Features

### 🎁 Automatic Gift Code Redemption
- **Automatic scanning** of official game channels every **5 minutes**
- **Instant validation** against the official WhiteOut Survival API
- **Batch redemption** for all alliance members with **20 concurrent requests** per batch
- **Built-in CAPTCHA solver** — custom ONNX model with **~98% accuracy** (~3.5ms per solve)
- **Smart retry system** with exponential backoff for failed redemptions
- **Per-member tracking** — see exactly which codes succeeded, failed, or were already used
- **Notifications** — new code alerts sent and **pinned** in your group automatically

### 👥 Alliance Member Management
- **Quick registration** — members type `/register [FID]` and they're in
- **DM confirmation** — automatic DM verification for secure registration
- **Cross-game detection** — automatically identifies which game (WOS/Kingshot) a player belongs to
- **Member export** — export your full member list as a file

### 📊 Real-Time Player Monitoring
- **🔥 Furnace level changes** — know when members upgrade their furnace
- **📝 Nickname changes** — track when members change their in-game name
- **🌍 State migrations** — detect when members move to a different state
- **📜 Change history** — view a member's complete change log with `/history`
- **Batch processing** — monitors **10 players concurrently** per cycle

### 🔄 Kingdom Transfer System
- **Power limits** — current caps by generation and furnace level
- **Transfer schedule** — upcoming windows with exact dates
- **Neighborhood groups** — which states can transfer to each other
- **Cost calculator** — estimated transfer cost and alliance store prices
- **Requirements** — all conditions needed to transfer (cooldown, power cap, FC level)

### 🤪 Crazy Joe Event Guide
- **Interactive wave guide** — all 20 waves for difficulty levels 1-11
- **Button navigation** — no typing needed, everything is clickable
- **Point calculator** — compare total points across all difficulties
- **Difficulty recommendation** — based on your alliance's average furnace level
- **Critical wave alerts** — online waves (7, 14, 17) and HQ waves (10, 20)

### 🐻 Event Management & Bear Trap
- **Bear Trap timer** with configurable reminders
- **Custom event scheduling** for your alliance
- **Multi-channel alerts** — notifications in both Telegram and Discord

### 🧮 Game Calculators
- **Troop training & promotion** (T1–T11)
- **Chief Gear upgrades** (Green to Pink, 0–5 stars)
- **Charm upgrades** (Level 0–16)
- **Hero Gear enhancement & mastery** forging

### 🌐 Multi-Platform & Multi-Language
- **Telegram + Discord** — full feature parity, shared database
- **English, Turkish, Russian** — per-group language configuration
- **Cross-platform sync** — register on Telegram, see data on Discord (and vice versa)
- **🆕 Want to add your language?** Translation files are in [`/locales/`](locales/)

### 👑 Premium & Subscription System
- Tiered plans with configurable member limits
- Subscription expiry warnings (7, 3, 1 day)
- Grace period after expiry (3 days full access)
- Stripe payment integration (optional)

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
│   │ channels every 5min │         │ 10 players/batch           │  │
│   │ Validates via API   │         │ Detects furnace/name/state │  │
│   │ Auto-redeems codes  │         │ Sends change notifications │  │
│   │ ONNX captcha solver │         │ Updates database           │  │
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
  Official game channels scanned (every 5 min)
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
     │  members         │──── ONNX CAPTCHA solver (~98%)
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
| `/language` | 🌐 Change your language preference |
| `/calc` | 🧮 Open game calculators (troops, gear, charms) |
| `/hero` | 🦸 Hero guide, tier list & Bear Trap recommendations |
| `/premium` | 👑 View subscription plan and usage limits |
| `/changelog` | 📋 View bot version history |
| `/support` | 💬 Contact support |

### 🏰 Alliance Management
| Command | Description |
|---------|-------------|
| `/setupalliance` | 🏗️ Create a new alliance (interactive guided setup) |
| `/alliance` | 🏰 View alliance information |
| `/setgroup` | 🔗 Link current group to an alliance |
| `/members [TAG]` | 👥 View all members in an alliance |
| `/export` | 📄 Export member list |

### 👥 Member Operations
| Command | Description |
|---------|-------------|
| `/addmember [FID] [TAG]` | ➕ Add a member to your alliance |
| `/removemember [FID] [TAG]` | ➖ Remove a member |
| `/history [FID]` | 🕵️ View a player's full change history |
| `/delete` | 🗑️ Delete your own account |

### 📅 Events & Tools
| Command | Description |
|---------|-------------|
| `/crazyjoe` | 🤪 Crazy Joe interactive wave guide & calculator |
| `/transfer` | 🔄 Kingdom transfer info, schedule & costs |
| `/beartrap` | 🐻 Bear trap event timer & alerts |
| `/statetimeline` | 🌍 State timeline, generation & events |
| `/announcements` | 📢 Game announcements |

### 🛡️ Admin Tools
| Command | Description |
|---------|-------------|
| `/admins` | 🛡️ Manage alliance admins |
| `/panel` | ⚙️ Alliance control panel |
| `/usecode [CODE]` | 🎫 Manually use a gift code for your alliance |
| `/addcode [CODE]` | 📌 Manually add a gift code |
| `/stats` | 📊 Bot statistics |
| `/broadcast` | 📢 Send announcement to all groups |
| `/managemembers` | 👥 View member gift code eligibility |

---

## 🔄 Kingdom Transfer System

The `/transfer` command provides comprehensive transfer information:

### What It Shows
- **Power Limits** — current caps by generation and furnace level
- **Transfer Schedule** — upcoming windows with exact dates
- **Neighborhood Groups** — which states can transfer to each other
- **Cost Calculator** — estimated transfer cost (Alliance Store, passes)
- **Requirements** — all conditions (cooldown, power cap, FC level, no alliance)

### Transfer Phases
1. **Pre-Transfer (3 days)** — Power caps are set
2. **Invitational Transfer (2 days)** — President sends invites
3. **Open Transfer (2 days)** — Everyone can transfer freely

### Example Output
```
🔄 Kingdom Transfer Info
━━━━━━━━━━━━━━━━━━━━
🌍 State: S1234
📊 Generation: Gen 5 | FC 3

⚡ Power Limits:
  Ordinary: 150,000,000
  Leading: 300,000,000

📅 Next Transfer Windows:
  📌 Mar 15 - Mar 22 (Open)
  📌 Apr 12 - Apr 19 (Invitational)

💰 Transfer Cost:
  Score 0-2M: Free
  Score 2M-5M: 500-2,000 gems
  Score 5M+: 2,000-10,000 gems
```

### What You Lose After Transfer
- Removed from all group chats
- Unsecured resources lost (inventory stays)
- Arena points reset to 1,000
- Pack purchase limits reset

---

## 🤪 Crazy Joe Event Guide

Interactive event guide accessible via `/crazyjoe` with button navigation — **no typing needed**.

### Features
- **📊 Wave Guide** — all 20 waves for each difficulty level (Lv.1-11)
- **📈 Point Calculator** — compare total points across all difficulties with % increase
- **🏆 Difficulty Recommendation** — based on your alliance's average furnace level & member count
- **⚡ Quick Jump** — instant access to critical waves (W7, W10, W14, W17, W20)

### Critical Waves
| Wave | Type | Alert |
|------|------|-------|
| **7, 14, 17** | 🟢 Online Members | All members must be online! |
| **10, 20** | 🏰 HQ Defense | Send reinforcements — no self-defense points |

### Data Coverage
- **11 difficulty levels** with exact troop counts, tier composition, and point values
- **Enemy tier progression**: T1-T2 (Wave 1) → T9-T10 (Wave 20)
- **~11.8% troop increase** per difficulty level
- **~5% point increase** per difficulty level

---

## 🚀 Get Started

### Quick Setup (5 minutes)
**1.** Add the bot to your Telegram group or Discord server
**2.** Run `/setupalliance` and follow the guided setup
**3.** Have your members type `/register [FID]`
**4.** Gift codes are redeemed automatically — sit back and relax! 🎉

### Add to Telegram
[![Add to Telegram](https://img.shields.io/badge/Add%20to%20Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/WhiteoutGuildBot)

> Search for `@WhiteoutGuildBot` in Telegram, add the bot to your alliance group and run `/start`.

### Add to Discord
[![Add to Discord](https://img.shields.io/badge/Add%20to%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/oauth2/authorize?client_id=1462815590141132905&permissions=8&scope=bot%20applications.commands)

> Click the button above to invite the bot. Use `/start` in your server to begin.

### 🆓 Free Trial
Contact us for a **free trial** with full access to all features:

[![Request Free Trial](https://img.shields.io/badge/Request%20Free%20Trial-00C853?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/btuncsiper)

---

## 📖 Guides

### How to Find Your FID
Your **FID (Fighter ID)** is your unique player identifier in WhiteOut Survival.

1. Open **WhiteOut Survival**
2. Tap your **avatar** in the top-left corner
3. Your **FID** is displayed below your nickname

> 💡 Your FID is a number like `123456789`. Copy it and use `/register 123456789` to register with the bot.

---

## 🛠 Tech Stack

| Component | Technology | Details |
|-----------|-----------|---------|
| **Language** | Python 3.13+ | Fully async/await architecture |
| **Telegram API** | python-telegram-bot v21 | Async-native, conversation handlers |
| **Discord API** | discord.py v2.x | Slash commands, embeds, views |
| **Database** | PostgreSQL 15+ | Connection pooling, composite keys |
| **HTTP Client** | aiohttp | Async API calls, session management |
| **CAPTCHA Solver** | ONNX Runtime (local) | Custom model, ~98% accuracy, ~3.5ms |
| **Proxy** | Residental rotating proxies | Rate limit avoidance |
| **Hosting** | Dedicated Server | 24/7 uptime, Windows Server |
| **Payments** | Stripe (optional) | Subscription management |

### Performance Configuration
| Parameter | Value | Description |
|-----------|-------|-------------|
| Gift Code Scan Interval | **5 minutes** | How often new codes are checked |
| Member Check Interval | **20 minutes** | Default alliance monitoring interval |
| API Batch Size | **10 concurrent** | Player data fetch parallelism |
| Gift Code Batch Size | **20 concurrent** | Code redemption parallelism |
| CAPTCHA Solve Time | **~3.5ms** | Local ONNX model inference |

### Architecture Highlights
- **Single-process dual-bot** — Telegram and Discord run concurrently in one process
- **Shared PostgreSQL database** — full cross-platform data consistency
- **Modular design** — separate modules for registration, gift codes, control, alliance, events, premium
- **Multi-language locale system** — JSON-based, per-group language settings (EN/TR/RU)
- **Game-type awareness** — all operations scoped by game type for multi-game support
- **Auto GitHub sync** — README, changelog, and locales auto-pushed on version change

---

## 🌐 Supported Languages

| Language | Code | Status |
|----------|------|--------|
| 🇬🇧 English | `en` | ✅ Full |
| 🇰🇷 한국어 | `ko` | ✅ Full |
| 🇷🇺 Русский | `ru` | ✅ Full |
| 🇹🇷 Türkçe | `tr` | ✅ Full |

Language files are in the [`locales/`](locales/) directory.

> 🆕 **Want to add your language?** Fork the repo, copy `locales/en.json`, translate it, and submit a PR!

---

## ❓ FAQ
<details>
<summary><b>How do I find my FID (Fighter ID)?</b></summary>

Open WhiteOut Survival → Tap your avatar (top-left corner) → Your FID is displayed below your nickname. It's a number like `123456789`.
</details>

<details>
<summary><b>Is this bot safe to use?</b></summary>

Absolutely. The bot uses the **official gift code redemption API** — the exact same API that the game's own website uses. It does **not** access your game account, modify your game data, or require your password.
</details>

<details>
<summary><b>How often does the bot check for new gift codes?</b></summary>

Every **5 minutes**. When a new code is discovered, it is validated and redeemed for all registered members within minutes.
</details>

<details>
<summary><b>Can I use this bot for multiple alliances?</b></summary>

Yes! Each alliance has its own configuration, member list, monitoring interval, language setting, and notification channels. Premium plans allow managing more alliances with higher member limits.
</details>

<details>
<summary><b>What languages are supported?</b></summary>

**English**, **Turkish** (Türkçe), and **Russian** (Русский). Each group can independently set their preferred language.
</details>

<details>
<summary><b>Does this bot work on both Telegram and Discord?</b></summary>

Yes! The bot runs on both platforms simultaneously with a shared database. Register on Telegram and your data is available on Discord too.
</details>

---

## 📞 Contact & Support
[![Contact Admin](https://img.shields.io/badge/Contact%20Admin-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/btuncsiper)

- **Support**: [t.me/btuncsiper](https://t.me/btuncsiper)
- **Bot**: [@WhiteoutGuildBot](https://t.me/WhiteoutGuildBot)
- **Free Trial**: [Request here](https://t.me/btuncsiper)

---

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<a href="https://woscontrol.com">
<img src="https://img.shields.io/badge/🌐_WEBSITE-woscontrol%2Ecom-FF6600?style=for-the-badge&labelColor=222222" alt="woscontrol.com" height="45">
</a>

<br><br>

**v1.11.0** · Last updated: 2026-03-15

<br>

[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-2CA5E0?style=flat-square&logo=telegram)](https://t.me/WhiteoutGuildBot)
[![Discord Bot](https://img.shields.io/badge/Discord-Bot-5865F2?style=flat-square&logo=discord)](https://discord.com/oauth2/authorize?client_id=1462815590141132905&permissions=8&scope=bot%20applications.commands)
[![Contact](https://img.shields.io/badge/Contact-Admin-E4405F?style=flat-square&logo=telegram)](https://t.me/btuncsiper)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

<br>

**WhiteOut Survival** · **WOS Bot** · **Gift Code Bot** · **Alliance Management** · **Auto Redeem**
**Telegram Bot** · **Discord Bot** · **Free Gift Codes** · **Furnace Tracker** · **WOS Helper**

</div>

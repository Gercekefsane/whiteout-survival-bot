<div align="center">

# ❄️ WhiteBot — WhiteOut Survival Bot

**v1.8.1** • [📋 Changelog](CHANGELOG.md) • [🌐 Languages](locales/)

All-in-one Telegram & Discord bot for WhiteOut Survival and Kingshot

[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)](https://t.me/WhiteOutSurvival_Bot)
[![Version](https://img.shields.io/badge/version-v1.8.1-green)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()

</div>

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 🎁 **Auto Gift Codes** | Automatically detects and redeems gift codes for all members |
| 👥 **Alliance Management** | Register members, track furnace levels, manage multiple alliances |
| 🐻 **Bear Trap Alerts** | Automated bear trap event notifications |
| 🤪 **Crazy Joe Guide** | Interactive wave guide with difficulty calculator |
| 🔄 **Kingdom Transfer** | Transfer info, power limits, schedule & cost calculator |
| 📊 **Calculators** | Troop, chief gear, hero gear, charms calculators |
| 🌍 **State Timeline** | Server age, generation, upcoming events |
| 💎 **Premium System** | Subscription plans with member limits |
| 📢 **Game Announcements** | Auto-fetched game news & updates |
| 🌐 **Multi-Language** | Turkish, English, Russian support |
| 🤖 **Dual Platform** | Works on both Telegram and Discord |

---

## 📋 Commands

### 🏰 Alliance
`/addalliance` — Create a new alliance
`/alliance` — View alliance info
`/deletealliance` — Delete an alliance
`/members` — List alliance members
`/setgroup` — Link a Telegram/Discord group

### 👥 Members
`/addmember` — Add a member to alliance
`/bulkadd` — Bulk add members
`/checkuser` — Look up a player by FID
`/history` — View player change history
`/profile` — View your profile & stats
`/removemember` — Remove a member from alliance

### 🎁 Gift Codes
`/addcode` — Manually add a gift code
`/codes` — List active gift codes
`/deletecode` — Remove a gift code
`/usecode` — Use a gift code for all members

### 🎮 Events & Tools
`/crazyjoe` — Crazy Joe event guide & calculator

### ℹ️ Info
`/announcements` — Game announcements
`/help` — Show all commands
`/premium` — View premium plans & subscription
`/start` — Start the bot
`/support` — Contact support

### ⚙️ Settings
`/language` — Change bot language
`/panel` — Alliance control panel
`/setlogchannel` — Set log channel

### 🔑 Admin
`/addadmin` — Add a bot admin
`/admins` — List bot admins
`/assignplan` — Assign premium plan to alliance
`/deleteplan` — Delete a premium plan
`/editplan` — Edit a premium plan
`/managemembers` — View member gift code eligibility
`/plans` — List premium plans
`/removeadmin` — Remove a bot admin
`/setcontact` — Set owner contact info
`/setpremium` — Toggle premium visibility
`/stats` — Bot statistics
`/togglestripe` — Toggle Stripe payments

---

## 🔄 Kingdom Transfer System

The `/transfer` command provides comprehensive transfer information:

- **Power Limits** — Current power caps by generation and furnace level
- **Transfer Schedule** — Upcoming transfer windows with dates
- **Neighborhood Groups** — Which states can transfer to each other
- **Cost Calculator** — Estimated transfer cost based on your score
- **Requirements** — All conditions needed to transfer

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
```

---

## 🤪 Crazy Joe Event Guide

Interactive event guide with button navigation:

- **Wave Guide** — All 20 waves for each difficulty (Lv.1-11)
- **Point Calculator** — Compare total points across difficulties
- **Difficulty Recommendation** — Based on alliance furnace average
- **Quick Jump** — Direct access to critical waves (W7, W10, W14, W17, W20)

Special wave alerts:
- 🟢 **Online Waves (7, 14, 17)** — All members must be online
- 🏰 **HQ Waves (10, 20)** — Send reinforcements, no self-defense points

---

## 🌐 Supported Languages

| Language | Code | Status |
|----------|------|--------|
| 🇹🇷 Turkish | `tr` | ✅ Full |
| 🇬🇧 English | `en` | ✅ Full |
| 🇷🇺 Russian | `ru` | ✅ Full |

Language files are in the [`locales/`](locales/) directory.

---

## 📊 Tech Stack

- **Python 3.13+**
- **python-telegram-bot** — Telegram bot framework
- **discord.py** — Discord bot framework
- **PostgreSQL** — Database
- **ONNX Runtime** — Local captcha solving (~98% accuracy)

---

## 📞 Contact

- **Telegram**: [btuncsiper](https://t.me/btuncsiper)
- **Bot**: [WhiteOutSurvival_Bot](https://t.me/WhiteOutSurvival_Bot)

---

<div align="center">

**v1.8.1** — Last updated: 2026-03-10

</div>

---
title: WhiteOut Survival Bot Features - Gift Code Redemption, Alliance Management, Member Tracking
description: Complete feature documentation for WhiteOut Survival Bot including automatic gift code redemption, alliance member management, real-time monitoring, and event scheduling
keywords: whiteout survival bot features, wos gift code bot, automatic gift code redemption, alliance management bot, member tracking, furnace tracker, whiteout survival telegram bot, whiteout survival discord bot
---

# ❄️ WhiteOut Survival Bot — Feature Details

## 🎁 Gift Code System

### How Auto-Discovery Works
1. The bot scans **official game channels** every 60 minutes (configurable)
2. Active codes are identified from trusted community sources
3. New codes are stored in PostgreSQL with `pending` status
4. Codes are validated against the game's official API
5. Validated codes are automatically redeemed for **every registered member**

### Code Lifecycle
```
Discovered → Pending → Validated → Auto-Used → Expired/Invalid
```

### CAPTCHA Handling
The WhiteOut Survival gift code API requires CAPTCHA verification. The bot:
- Fetches CAPTCHA image from the game API
- Sends to Custom Solver service for solving
- Submits solution with the gift code request
- Retries with new CAPTCHA on failure

### Smart Retry System
- Failed redemptions are queued for retry
- Exponential backoff prevents rate limiting
- Maximum retry attempts configurable
- Detailed error tracking per member per code

---

## 👥 Member Management

### Registration Methods
1. **Command**: `/register 123456789` — direct FID registration
2. **ID Channel**: Set a channel where typing any FID auto-registers the member
3. **Bulk Add**: `/bulkadd 111 222 333 TAG` — add multiple FIDs at once
4. **Admin Add**: `/addmember 123456789 TAG` — admin registers on behalf

### What Gets Tracked
| Field | Description | Change Notification |
|-------|-------------|-------------------|
| **Nickname** | In-game display name | ✅ Yes |
| **Furnace Level** | FC level (e.g., FC 30) | ✅ Yes |
| **State** | Server/state number | ✅ Yes |
| **Alliance** | Current in-game alliance | ✅ Yes |

### ID Channel System
- Admin sets a channel as "ID Channel" with `/setchannel`
- Any message containing a valid FID is automatically processed
- Bot replies with registration confirmation including player info
- Non-FID messages are silently ignored

---

## 📊 Monitoring & Control

### Control Loop
The control loop runs at configurable intervals (default: 60 minutes):
1. Fetches live data for each registered member from the game API
2. Compares with stored data in the database
3. Detects changes in nickname, furnace level, or state
4. Sends formatted notifications to the alliance's Telegram/Discord channel
5. Updates the database with new values

### Notification Examples
```
🔥 Furnace Level Up!
Player: JohnDoe
FC 29 → FC 30
Alliance: [ABC] My Alliance

📝 Nickname Changed!
Old: OldName
New: NewName
FID: 123456789
```

---

## 🌐 Multi-Language Support

### Supported Languages
| Language | Code | Coverage |
|----------|------|----------|
| English | `en` | 100% |
| Turkish | `tr` | 100% |
| Russian | `ru` | 100% |

### How It Works
- Each group/user can set their preferred language
- All bot messages, buttons, and notifications are localized
- Language can be changed with `/language` or `/setlang`
- New languages can be added by creating a locale JSON file

---

## 🔄 Cross-Platform

### Telegram Features
- Inline keyboards for navigation
- HTML-formatted messages
- Group and private chat support
- Message pinning for important notifications
- ID Channel for auto-registration

### Discord Features
- Slash commands (`/register`, `/help`, etc.)
- Embed messages with rich formatting
- Server and channel-based alliance linking
- Role-based permission checks
- Message pinning for gift code alerts

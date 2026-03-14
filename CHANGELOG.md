# Changelog

All notable changes to this project are documented here.

## v1.10.0 — 2026-03-14

### ✨ Added
- **Interactive Map Commands (Discord)**: /map, /mapimage, /setcoord, /place, /placemember slash commands
- **Auto Hive Formation Types**: 4 placement patterns — Diamond, Square, Cross, Compact (bot + web)
- **Setcoord Interactive Flow**: Building type selection: City, HQ, Trap, Flag, Farm, Mine, Water, Mountain
- **Hero Guide**: /hero command with 60+ heroes, tier list, Bear Trap recommendations, wiki links
- **Discord Event Image Grouping**: Wiki event images sent as grouped embeds (up to 10 per message)
- **Map Setup Callback**: /start command now has Map Manager button linking to /mapsetup

### 🔧 Fixed
- **Flag Placement**: Exactly 4 flags at trap diagonal corners
- **Map Image Crash**: Fixed send_map_image_with_actions bot=None parameter crash
- **Announcements SQL Error**: Fixed 14-value vs 13-column mismatch in game_announcements INSERT
- **Turkish Translations**: Added missing /register command locale keys

### 🔄 Changed
- **Bulkadd Removed**: Deprecated /bulkadd command removed from both TG and Discord
- **Web Map Editor**: Auto-place split button with formation type dropdown
- **State Notifications**: Verified Discord channel delivery
- **GitHub Auto-Sync**: Integrated watcher thread into bot process, website URL in README

---

## v1.9.0 — 2026-03-11

### ✨ Added
- **Transfer Tracker**: Auto-monitors wiki for new transfer schedules, AI image analysis, Google Sheets update
- **Wiki Items Tracker**: Monitors new game items from wiki, AI translation, broadcast to groups
- **Wiki Events Tracker**: Monitors game events (official + Korean leaks), multi-image albums
- **Beautiful Bear Trap Notifications**: Competitor-quality design with hero recommendations (P2W/F2P)
- **Bulkadd Simplified**: No TAG needed, auto-detect alliance, premium limit enforcement
- **/checktransfer**: Manual trigger for transfer sneak peek checking
- **/checkwiki & /testwiki**: Manual wiki content checking and testing
- **Config Toggles**: Enable/disable items/events tracking, pin, broadcast per type

### 🔧 Fixed
- **Event Notifications Language**: All event commands now respect group language settings
- **Registration DM Error**: Fixed ON CONFLICT error on user_dm_status table
- **Wiki Content Scraper**: Fixed content-section div selector and title cleanup
- **Image Scraper**: Fixed generic wiki icon appearing for all items
- **Translation Artifacts**: Fixed literal \n in AI translations

### 🔄 Changed
- **Bear Trap Notifications**: Beautiful design with alliance tag, hero recommendations, tips
- **Transfer Announcements**: Now pinned in groups, sent to Discord
- **Event Type Names**: Fully localized in TR/EN/RU via locale keys
- **First-Run Protection**: Wiki tracker seeds DB without broadcasting on startup

---

## v1.8.1 — 2026-03-10

### ✨ Added
- **Subscription Expiry Warnings**: 7/3/1 day warnings before plan expires
- **Grace Period**: 3-day grace period after expiry, all members keep access
- **Member Priority System**: Hybrid: admin override + first-registered priority
- **/managemembers**: View and manage member priorities when over limit
- **/promotemember & /demotemember**: Admin can adjust member gift code priority
- **Changelog History**: Browse previous versions with /changelog [version]

### 🔧 Fixed
- **DM Confirmation**: Fixed unique constraint error on telegram_id
- **Registration Blocking**: Reduced message updates during gift code processing

### 🔄 Changed
- **Gift Code Eligibility**: Over-limit members filtered by hybrid priority
- **Expiry Loop**: Multi-level warnings with detailed impact info

---

## v1.8.0 — 2026-03-10

### ✨ Added
- **Contributors Display**: Transfer command shows contributors in messages
- **Live Updates**: Registration group messages update in real-time
- **State Validation**: Transfer validates kingdom numbers
- **Future Gen Calculation**: Power limits based on expected generation

### 🔧 Fixed
- **Profile Stats**: Gift code stats now show correctly (game_type filter)
- **Registration Updates**: Group message updates after DM confirmation
- **Transfer Power**: Dynamic generation calculation for future dates

### 🔄 Changed
- **Localization**: Contributors text moved to locale files (TR/EN/RU)
- **Gift Code Progress**: Gift code processing shows live progress
- **DM Flow**: DM confirmation immediately updates group status

---

## v1.7.0 — 2026-03-01

### ✨ Added
- **Premium System**: Subscription plans with Stripe integration
- **Calculator Module**: Troop, chief gear, charms, hero gear calculators
- **Kingshot Support**: Dual-game support for WOS and Kingshot
- **ONNX Captcha Solver**: Local ML-based captcha solving (~98% accuracy)

### 🔧 Fixed
- **Discord Sync**: Fixed cross-thread Discord API calls
- **Bear Trap**: Scheduling improvements for bear trap notifications

### 🔄 Changed
- **Database**: Unified PostgreSQL for both Telegram and Discord
- **Gift Codes**: Dual-game gift code processing (WOS + KS)

---


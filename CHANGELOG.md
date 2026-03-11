# Changelog

All notable changes to this project are documented here.

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


# Changelog

All notable changes to this project are documented here.

## v3.3.0 — 2026-03-23

### ✨ Added
- **Social Media Form Tracker**: Automatic detection and processing of Google Forms shared on official game social media accounts — monitors configured accounts every 15 minutes
- **Smart AI Filtering**: Advanced AI analysis determines whether a detected form is a genuine reward survey before processing — eliminates irrelevant posts and design events automatically
- **Auto Form Registration**: Newly discovered forms are instantly analyzed, registered to the database, and submitted to all alliance members without any manual intervention
- **Configurable Account List**: Easily add or remove monitored social media accounts via config — supports multiple accounts simultaneously
- **Reward Detection from Posts**: AI extracts reward hints directly from post text — icon rewards, resource packs, gift codes all detected and stored
- **Deduplication System**: Intelligent deduplication prevents the same form from being processed twice even when shared with different URL parameters
- **Session Health Monitoring**: Automatic detection of authentication expiry — owner receives immediate Telegram notification with step-by-step re-authentication instructions
- **/checkxforms Command**: Owner command to manually trigger social media form scanning across all configured accounts
- **/xlogin Command**: Secure cookie-based authentication setup for social media monitoring — tokens auto-deleted from chat after entry for security
- **Form Reward Translations**: Detected reward text is automatically translated to all 4 languages (EN/TR/RU/KO) and stored for multi-language website display
- **Google Forms Page**: New /forms page on woscontrol.com — browse all active Google Forms with reward info, expiry countdown, and success rate per form
- **Forms API Endpoint**: /api/forms — Serves active form configs with reward type, translated reward text, expiry, and submission statistics
- **Reward Type Display**: Forms page shows reward type badges: Gift Code, Resources, Raffle, Item — each with distinct icon and color
- **Multi-language Reward Display**: Reward descriptions shown in user's selected language on the forms page

### 🔧 Fixed
- **Duplicate Form Notifications**: Same form URL with different query parameters (e.g. ?usp=send_form) no longer triggers multiple notifications
- **Authentication Verification**: Login verification now uses a lightweight public profile lookup instead of a self-profile endpoint that returned 404
- **ClientTransaction Key Error**: Resolved a server-side JavaScript obfuscation change that caused all API calls to fail with a cryptographic key index error — patched transparently without requiring library updates
- **Form Submission After Auto-Registration**: Newly auto-registered forms now correctly trigger mass submission to all alliances — previously only inserted to DB without submitting

### 🔄 Changed
- **X Tracker Config**: Added X_FORM_TRACKER_ENABLED, X_FORM_TRACKER_INTERVAL_MINUTES, X_FORM_TRACKER_ACCOUNTS, X_FORM_TRACKER_AUTO_APPROVE, X_FORM_TRACKER_NOTIFY_OWNER, X_FORM_TRACKER_MAX_TWEETS, X_FORM_TRACKER_LOOKBACK_DAYS to config
- **/help owner**: Trackers section updated with /checkxforms and /xlogin — Forms section updated with /reanalyzeform, /submitform, /formhistory
- **Version Bump**: 3.2.0 → 3.3.0

---

## v3.2.0 — 2026-03-19

### ✨ Added
- **GitHub Star Bonus System**: Full GitHub integration — OAuth Device Flow account linking, star tracking, automatic bonus calculation per user
- **Individual Register Bonus**: GitHub star bonus now applies per-user on max_registers instead of alliance-wide max_members
- **Sponsor/YouTube Kingdom Limit**: Sponsor and YouTube plans enforce same-kingdom member limits based on free plan cap
- **/github Command**: Connect your GitHub account via Device Flow — Telegram and Discord
- **/mystars Command**: View your linked GitHub account and star status across all tracked repos
- **/addrepo & /removerepo**: Owner commands to manage tracked GitHub repositories
- **/starstats**: Owner command to view all repos, star counts, and bonus totals
- **/captchastats**: Captcha solver performance statistics — session, daily, weekly, all-time with visual charts
- **/codeimage**: Upload gift code content images for the website — reply, caption, or two-step flow
- **Star Notifications**: Real-time star/unstar notifications to alliance groups on both Telegram and Discord
- **Korean GitHub Locale**: All github_* locale keys added to Korean (ko.json)
- **Kingdom Limit Locale Keys**: kingdom_limit_title/desc/hint and star_bonus_hint in all 4 languages

### 🔧 Fixed
- **GitHub Auto-Sync Version**: BOT_VERSION stale reference after importlib.reload — now properly re-binds global
- **Premium Display Consistency**: All 4 Discord plan_text displays now show individual GitHub bonus on registers

### 🔄 Changed
- **Premium Limit Messages**: Show GitHub bonus hint when user hits register limit without star bonus
- **Star Notifications Wording**: Removed explicit GitHub branding — now uses neutral 'Star Bonus' wording
- **GitHub Locale Filtering**: Auto-changelog filters github_ prefixed keys from public GitHub locale pushes
- **Version Bump**: 3.0.0 → 3.2.0

---

## v3.0.0 — 2026-03-17

### ✨ Added
- **Hero Database (Dynamic)**: Heroes page now fetches data from PostgreSQL instead of static embedded data — auto-updates when wiki scraper detects new heroes
- **Hero Detail Modal**: Click any hero to see full story, skills, charm abilities, and portrait image — all translated per user language
- **Hero Wiki Scraper (Korean)**: Added Korean (ko) to auto-translation pipeline — all heroes now translated to EN/TR/RU/KO via OpenAI
- **Heroes API Endpoint**: /api/heroes?lang=xx serves hero data from DB with translation overlay for any supported language
- **Announcements Page**: /announcements — Browse game announcements with game filter (WOS/KS), search, expandable cards, load more pagination
- **Announcements API**: /api/announcements — Fetches from game_announcements DB table with language/game filtering and pagination
- **Player Search Page**: /player-search — Search any player by FID, view profile card with furnace level, kingdom, alliance, gift code history, change history
- **Player Search API**: /api/player-search — Internal endpoint with game API + DB fallback, gift codes, change history
- **Alliance Dashboard**: /dashboard — Auth-gated dashboard with alliance stats, searchable member table, code history, export/settings
- **Website Navigation**: Added Announcements, Player Search, Dashboard links to navbar with full localization
- **Locale Keys (80+)**: Added 80+ translation keys across all 4 languages for announcements, player search, and dashboard pages

### 🔧 Fixed
- **Gift Code Limit Distinction**: Properly separate 40005 (LIMIT_REACHED) vs 40008 (ALREADY_USED) — 4-column progress grid, per-item icons, limit badges
- **Heroes Static Data**: Replaced hardcoded hero list with DB-powered dynamic data — new heroes auto-appear after wiki scan

### 🔄 Changed
- **Hero Page Architecture**: Moved from client-side static data to API-driven architecture with PostgreSQL backend
- **Hero Cards**: Now show hero portrait images from wiki, clickable for full detail modal
- **Version Bump**: 2.0.0 → 3.0.0

---

## v2.0.0 — 2026-03-15

### ✨ Added
- **Website i18n System**: Full 4-language support (EN/TR/RU/KO) with 500+ translation keys across all pages
- **Korean Language**: Complete Korean locale added for both bot and website
- **Gift Code Web Redemption**: Job-based redemption system — website creates DB jobs, bot processes them with captcha solving
- **Alliance Directory**: woscontrol.com/alliances — Alliance listing with member counts, kingdom info, game types, platform badges
- **Alliance Detail Modal**: Leaderboard (top 10 players), gift code stats, game distribution, FC level mapping
- **Alliance Join System**: Bot-powered join via DM invite — login → select platform → bot sends invite link
- **YouTuber System**: YouTube Data API v3 integration — auto-fetch channel info, banners, subscriber/view counts
- **YouTuber Promotion Videos**: Auto-detect woscontrol videos via RSS, show in Tanıtım modal on each card
- **YouTuber Auto-Feature**: Auto-promote YouTubers with woscontrol videos in last 7 days to Featured
- **YouTuber Notifications**: Bot sends thank you DM to YouTubers when promotion video detected
- **YouTuber Welcome DM**: /addyoutuber sends welcome DM to verify bot can reach the YouTuber
- **FOMO Widget**: Social proof notifications — member joins, code redeems, new codes, new YouTubers, alliance web joins
- **Golden CTA Banner**: Animated gift code banner on homepage with sparkle effects
- **Profile Alliance Info**: Show alliance, plan, member count/limit, gift code stats on profile page
- **SEO Improvements**: sitemap.xml, hreflang tags, structured metadata
- **Browser Fingerprint**: Anti-abuse fingerprint system with localStorage persistence for gift code rate limiting
- **Auto Alliance Info Refresh**: Bot refreshes group names and invite links hourly
- **YouTube Auto-Refresh**: 15-minute refresh interval for YouTuber data from config

### 🔧 Fixed
- **Telegram Auth**: Use actual TelegramLogin widget everywhere, strip non-TG params from hash verification
- **Premium Table Error**: Fixed 'premium nesnesi mevcut değil' — use alliance_subscriptions + premium_plans
- **FC Level Display**: Show FC3-4 instead of raw 49 using LEVEL_MAPPING
- **Discord Join**: Fixed 'Timeout context manager' error with run_coroutine_threadsafe
- **Mobile Responsive**: Global overflow-x hidden, responsive FOMO widget, alliance cards
- **Wrong Telegram Links**: Fixed 4 WhiteOutSurvival_Bot → WhiteoutGuildBot
- **Login Redirect**: Discord OAuth returns to originating page (alliances/profile) instead of /codes

### 🔄 Changed
- **Bot Messages Localized**: Web join notifications, YouTuber messages use get_text() from locales/*.json
- **Country Flags**: Flag emojis only — no text codes like TR/US
- **/addyoutuber**: Rewritten — YouTube API auto-fetch, promo video check, welcome DM verification
- **Alliance Join Modal**: Platform-matching login buttons, proper join context text
- **YouTuber Cards**: Redesigned with banners, view counts, country flags, action buttons

---

## v1.11.0 — 2026-03-15

### ✨ Added
- **Alliance Leaderboard**: /leaderboard — Furnace rankings, top growers, alliance overview stats
- **Inactive Member Detection**: /inactive [days] — Find members with no activity in last N days
- **Gift Code Statistics**: /codestats — Detailed redemption stats per code
- **WhiteLabel System**: Full bot management with /wl commands and /mybot customer view
- **WhiteLabel Expiry**: Auto-suspend expired bots, expiry date management, audit logging
- **Hero Wiki Scraper**: Auto-scrapes wiki every 6h, extracts skills/story/abilities
- **Hero AI Translation**: OpenAI auto-translates hero data to TR/RU
- **Hero Detail View**: Inline skills, special abilities, story from DB

### 🔧 Fixed
- **Chat Not Found Spam**: Bear trap notifications auto-disable on unreachable chat
- **Hero Wiki Scraper**: Fixed content-hero CSS selector, ASCII-only slug filter
- **Website Links**: Fixed Discord invite + Telegram username on woscontrol.com

### 🔄 Changed
- **GitHub README**: WOSCONTROL.COM as H1 at the very top
- **GitHub Auto-Push**: WhiteLabel promo docs + docs/ folder tracked
- **Bot Username Check**: Auto-verify TG/Discord usernames on startup

---

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


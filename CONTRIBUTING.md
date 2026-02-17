---
title: Contributing to WhiteOut Survival Bot - Add New Languages
description: Guide for developers and translators to contribute new language translations to the WhiteOut Survival Bot
keywords: whiteout survival bot translation, add language, contribute, localization, i18n, telegram bot translation, discord bot translation
---

# 🌐 Contributing — Add a New Language

Thank you for your interest in contributing to the WhiteOut Survival Bot! One of the easiest and most impactful ways to contribute is by **adding a new language translation**.

The bot currently supports:

| Language | Code | File | Status |
|----------|------|------|--------|
| 🇬🇧 English | `en` | [`languages/en.json`](languages/en.json) | ✅ Complete |
| 🇹🇷 Turkish | `tr` | [`languages/tr.json`](languages/tr.json) | ✅ Complete |
| 🇷🇺 Russian | `ru` | [`languages/ru.json`](languages/ru.json) | ✅ Complete |

---

## 📋 How to Add a New Language

### Step 1: Fork & Clone

```bash
git clone https://github.com/YOUR_USERNAME/whiteout-survival-bot.git
cd whiteout-survival-bot
```

### Step 2: Copy the English Base

Copy `languages/en.json` as your starting template — English is always the most up-to-date:

```bash
cp languages/en.json languages/XX.json
```

Replace `XX` with the [ISO 639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for your language:

| Language | Code |
|----------|------|
| Spanish | `es` |
| Portuguese | `pt` |
| French | `fr` |
| German | `de` |
| Arabic | `ar` |
| Chinese | `zh` |
| Japanese | `ja` |
| Korean | `ko` |
| Indonesian | `id` |
| Vietnamese | `vi` |
| Thai | `th` |
| Hindi | `hi` |

### Step 3: Edit the File

Open `languages/XX.json` and translate **every value** (right side of `:`) while keeping **every key** (left side of `:`) unchanged.

#### ✅ Correct Example (Spanish):
```json
{
  "name": "Español",
  "flag": "🇪🇸",
  
  "welcome_title": "🎮 <b>WhiteBot - Whiteout Survival Bot</b>",
  "hello": "Hola",
  "bot_added_group": "Bot ha sido añadido a este grupo. 👋",
  "group_info": "📋 Información del grupo:",
  "group_name": "Nombre del grupo",
  ...
}
```

#### ❌ Wrong — Do NOT change the keys:
```json
{
  "nombre": "Español",
  "bandera": "🇪🇸"
}
```

### Step 4: Important Rules

1. **Keep ALL keys exactly as they are** — only translate the values
2. **Keep HTML tags** like `<b>`, `<code>`, `<a href="...">` intact
3. **Keep placeholders** like `{user}`, `{count}`, `{tag}`, `{name}` unchanged
4. **Keep emojis** in the values — they are part of the UI
5. **Keep special characters** like `\n` (newline) in multiline strings
6. **Update `"name"`** to your language's native name (e.g., `"Español"`)
7. **Update `"flag"`** to your country's flag emoji (e.g., `"🇪🇸"`)

### Step 5: Validate Your JSON

Make sure your JSON is valid before submitting. You can use:

```bash
python -c "import json; json.load(open('languages/XX.json', encoding='utf-8')); print('✅ Valid JSON')"
```

Or use an online validator like [jsonlint.com](https://jsonlint.com).

### Step 6: Submit a Pull Request

```bash
git checkout -b add-language-XX
git add languages/XX.json
git commit -m "Add XX language translation"
git push origin add-language-XX
```

Then open a Pull Request on GitHub with:
- **Title**: `Add [Language Name] translation`
- **Description**: Mention if the translation is complete or partial

---

## 📂 File Structure

```
languages/
├── en.json          ← English (base/reference)
├── tr.json          ← Turkish (Türkçe)
├── ru.json          ← Russian (Русский)
└── XX.json          ← Your new language!
```

Each JSON file contains **700+ translation keys** organized by feature:

| Section | Keys | Description |
|---------|------|-------------|
| General UI | `hello`, `welcome_title`, `btn_*` | Buttons, titles, greetings |
| Alliance | `alliance_*`, `setgroup_*` | Alliance management messages |
| Members | `member_*`, `bulk_*` | Member operations |
| Gift Codes | `giftcode_*`, `codes_*` | Gift code system messages |
| Control | `control_*`, `changes_*` | Monitoring notifications |
| Events | `event_*`, `bear_trap_*` | Event scheduling |
| Minister | `minister_*` | Minister rotation system |
| Registration | `register_*`, `registration_*` | Player registration flow |
| Premium | `premium_*` | Subscription system |
| Errors | `error_*`, `invalid_*` | Error messages |
| Weekdays | `weekday_*` | Day names |

---

## 🔍 Translation Tips

### Context Matters
- `"member"` = a single member → `"üye"` (TR), `"участник"` (RU)
- `"members"` = plural/count context → `"üye"` (TR), `"участников"` (RU)
- `"alliance"` = in-game alliance → keep as "Alliance" or translate naturally

### Game-Specific Terms
Some terms are commonly kept in English even in other languages:
- **FID** — always keep as "FID"
- **Gift Code** — can be translated or kept
- **Furnace** — translate to your language's in-game term
- **Bear Trap** — translate to your language's in-game event name

### HTML Tags
The bot uses Telegram's HTML parse mode. Keep all HTML formatting:
```json
"user_info_title": "👤 <b>User Information</b>"
```
→ Translate "User Information" but keep `<b>` tags.

### Multiline Strings
Some values contain `\n` for line breaks. Keep them:
```json
"features_list": "🏰 <b>Alliance Management</b>\n• Create alliances\n• Multi-alliance support"
```

---

## 🤝 Partial Translations

Can't translate everything? That's okay! Submit what you have — partial translations are welcome. The bot falls back to English for any missing keys, so untranslated strings will just appear in English.

Priority keys to translate first:
1. `name`, `flag` (language identity)
2. `hello`, `welcome_title`, `btn_*` (basic UI)
3. `register_*`, `member_*` (core user flow)
4. `giftcode_*` (gift code messages)
5. Everything else

---

## 📞 Questions?

Need help with your translation or have questions about context?

[![Contact Admin](https://img.shields.io/badge/Contact%20Admin-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/woscoupon)

---

**Keywords**: WhiteOut Survival translation, add language, contribute, localization, i18n, multilingual bot, telegram bot translation, discord bot translation, open source contribution

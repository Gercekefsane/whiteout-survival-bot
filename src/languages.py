# Multi-language support for WhiteBot
# Loads translations from JSON files in languages/ directory

import json
import os

# Get the directory where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCALES_DIR = os.path.join(BASE_DIR, "..", "languages")

# Default language
DEFAULT_LANGUAGE = "en"

# Cache for loaded languages
LANGUAGES = {}


def load_language(lang_code: str) -> dict:
    """Load a language from JSON file"""
    if lang_code in LANGUAGES:
        return LANGUAGES[lang_code]
    
    file_path = os.path.join(LOCALES_DIR, f"{lang_code}.json")
    
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                LANGUAGES[lang_code] = json.load(f)
                return LANGUAGES[lang_code]
        except Exception as e:
            print(f"Error loading language {lang_code}: {e}")
    
    # Fallback to English
    if lang_code != DEFAULT_LANGUAGE:
        return load_language(DEFAULT_LANGUAGE)
    
    return {}


def get_text(key: str, lang: str = "en") -> str:
    """Get text in specified language, fallback to English"""
    lang_data = load_language(lang)
    
    if key in lang_data:
        return lang_data[key]
    
    # Fallback to English
    if lang != DEFAULT_LANGUAGE:
        en_data = load_language(DEFAULT_LANGUAGE)
        if key in en_data:
            return en_data[key]
    
    return key


def get_available_languages() -> dict:
    """Get list of available languages with their native names and flags"""
    languages = {}
    
    if os.path.exists(LOCALES_DIR):
        for filename in os.listdir(LOCALES_DIR):
            if filename.endswith('.json'):
                lang_code = filename[:-5]
                lang_data = load_language(lang_code)
                languages[lang_code] = {
                    "name": lang_data.get("name", lang_code),
                    "flag": lang_data.get("flag", "🏳️")
                }
    
    return languages


def reload_languages():
    """Reload all language files (useful for hot-reloading)"""
    global LANGUAGES
    LANGUAGES = {}

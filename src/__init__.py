"""WhiteOut Survival Bot — Source Preview

This package contains preview modules from the WhiteOut Survival Bot.
Full source code will be released when the repository reaches 100 ⭐ stars.

Modules:
    languages    - Multi-language support (JSON-based, 3 languages, 700+ keys)
    models       - Data models, game constants, API signing utilities
    calculators  - Game calculators (troops, gear, charms, hero gear)
"""

from .languages import get_text, get_available_languages, load_language
from .models import (
    GAME_WOS, GAME_KS, GAME_NAMES, GAME_ICONS,
    GiftCodeStatus, RedemptionResult,
    PlayerInfo, GiftCode, Alliance, RedemptionReport,
    generate_sign, build_player_request, get_furnace_display,
)
from .calculators import (
    TroopsCalculator, ChiefGearCalculator,
    CharmsCalculator, HeroGearCalculator,
)

__version__ = "1.0.0"
__author__ = "Gercekefsane"

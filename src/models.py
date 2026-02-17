"""Data models and constants for WhiteOut Survival Bot"""

import hashlib
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


# ============================================
# GAME TYPE CONSTANTS
# ============================================

GAME_WOS = 'wos'
GAME_KS = 'ks'
GAME_CHOICES = [GAME_WOS, GAME_KS]
GAME_NAMES = {GAME_WOS: 'WhiteOut Survival', GAME_KS: 'Kingshot'}
GAME_ICONS = {GAME_WOS: '❄️', GAME_KS: '👑'}


class GiftCodeStatus(Enum):
    """Gift code validation states"""
    PENDING = 0
    VALIDATED = 1
    INVALID = 2
    EXPIRED = 3


class RedemptionResult(Enum):
    """Result of a gift code redemption attempt"""
    SUCCESS = "success"
    ALREADY_USED = "already_used"
    EXPIRED = "expired"
    INVALID = "invalid"
    FURNACE_LOW = "furnace_low"
    VIP_LOW = "vip_low"
    LOGIN_FAILED = "login_failed"
    CAPTCHA_FAILED = "captcha_failed"
    RATE_LIMITED = "rate_limited"
    TIMEOUT = "timeout"
    CONNECTION_ERROR = "connection_error"
    UNKNOWN = "unknown"


@dataclass
class PlayerInfo:
    """Player information from game API"""
    fid: int
    nickname: str
    furnace_level: int
    furnace_display: str
    kid: int  # state/kingdom ID
    avatar_id: Optional[int] = None
    game_type: str = GAME_WOS

    @property
    def state_display(self) -> str:
        return f"#{self.kid}" if self.kid else "Unknown"


@dataclass
class GiftCode:
    """Gift code data model"""
    code: str
    game_type: str = GAME_WOS
    status: GiftCodeStatus = GiftCodeStatus.PENDING
    discovered_at: Optional[str] = None
    validated_at: Optional[str] = None


@dataclass
class Alliance:
    """Alliance data model"""
    alliance_id: int
    tag: str
    name: str
    game_type: str = GAME_WOS
    owner_id: Optional[int] = None
    chat_id: Optional[int] = None
    suspended: bool = False
    priority: int = 0


@dataclass
class RedemptionReport:
    """Report for a gift code redemption batch"""
    code: str
    alliance_tag: str
    total: int = 0
    success: int = 0
    already_used: int = 0
    failed: int = 0
    errors: dict = field(default_factory=dict)

    @property
    def success_rate(self) -> float:
        return (self.success / self.total * 100) if self.total > 0 else 0.0


# ============================================
# FURNACE LEVEL MAPPING
# ============================================

LEVEL_MAPPING = {
    31: "30-1", 32: "30-2", 33: "30-3", 34: "30-4",
    35: "FC 1", 36: "FC 1-1", 37: "FC 1-2", 38: "FC 1-3", 39: "FC 1-4",
    40: "FC 2", 41: "FC 2-1", 42: "FC 2-2", 43: "FC 2-3", 44: "FC 2-4",
    45: "FC 3", 46: "FC 3-1", 47: "FC 3-2", 48: "FC 3-3", 49: "FC 3-4",
    50: "FC 4", 51: "FC 4-1", 52: "FC 4-2", 53: "FC 4-3", 54: "FC 4-4",
    55: "FC 5", 56: "FC 5-1", 57: "FC 5-2", 58: "FC 5-3", 59: "FC 5-4",
    60: "FC 6", 61: "FC 6-1", 62: "FC 6-2", 63: "FC 6-3", 64: "FC 6-4",
    65: "FC 7", 66: "FC 7-1", 67: "FC 7-2", 68: "FC 7-3", 69: "FC 7-4",
    70: "FC 8", 71: "FC 8-1", 72: "FC 8-2", 73: "FC 8-3", 74: "FC 8-4",
    75: "FC 9", 76: "FC 9-1", 77: "FC 9-2", 78: "FC 9-3", 79: "FC 9-4",
    80: "FC 10", 81: "FC 10-1", 82: "FC 10-2", 83: "FC 10-3", 84: "FC 10-4",
}


def get_furnace_display(level: int) -> str:
    """Convert raw furnace level to display string"""
    if level in LEVEL_MAPPING:
        return LEVEL_MAPPING[level]
    return str(level)


# ============================================
# API REQUEST SIGNING
# ============================================

def generate_sign(params: str, encrypt_key: str) -> str:
    """Generate MD5 signature for game API requests
    
    Args:
        params: URL-encoded form parameters (e.g., 'fid=123&time=1234567890')
        encrypt_key: Game-specific encryption key
    
    Returns:
        MD5 hex digest string
    """
    return hashlib.md5(
        (params + encrypt_key).encode('utf-8')
    ).hexdigest()


def build_player_request(fid: int, encrypt_key: str) -> tuple[str, str]:
    """Build signed request data for player info lookup
    
    Returns:
        Tuple of (form_data_string, sign_string)
    """
    current_time = int(time.time() * 1000)
    form = f"fid={fid}&time={current_time}"
    sign = generate_sign(form, encrypt_key)
    return f"sign={sign}&{form}", sign

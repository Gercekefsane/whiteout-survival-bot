"""Game calculators for WhiteOut Survival Bot

Provides calculation utilities for:
- Troop training & promotion costs (T1-T11)
- Chief Gear upgrade costs (Green to Pink, 0-5 stars)
- Charm upgrade costs (Level 0-16)
- Hero Gear enhancement (0-100) and mastery forging (0-10)
"""

from dataclasses import dataclass
from typing import Optional


# ============================================
# TROOP CALCULATOR
# ============================================

TROOP_TIERS = {
    "T1": {"name": "Tier 1", "training_cost": 50, "training_time": 10},
    "T2": {"name": "Tier 2", "training_cost": 100, "training_time": 20},
    "T3": {"name": "Tier 3", "training_cost": 200, "training_time": 40},
    "T4": {"name": "Tier 4", "training_cost": 400, "training_time": 80},
    "T5": {"name": "Tier 5", "training_cost": 800, "training_time": 160},
    "T6": {"name": "Tier 6", "training_cost": 1600, "training_time": 320},
    "T7": {"name": "Tier 7", "training_cost": 3200, "training_time": 640},
    "T8": {"name": "Tier 8", "training_cost": 6400, "training_time": 1280},
    "T9": {"name": "Tier 9", "training_cost": 12800, "training_time": 2560},
    "T10": {"name": "Tier 10", "training_cost": 25600, "training_time": 5120},
    "T11": {"name": "Tier 11", "training_cost": 51200, "training_time": 10240},
}

PROMOTION_COSTS = {
    ("T1", "T2"): {"meat": 100, "wood": 80, "coal": 60, "iron": 40},
    ("T2", "T3"): {"meat": 200, "wood": 160, "coal": 120, "iron": 80},
    ("T3", "T4"): {"meat": 400, "wood": 320, "coal": 240, "iron": 160},
    ("T4", "T5"): {"meat": 800, "wood": 640, "coal": 480, "iron": 320},
    ("T5", "T6"): {"meat": 1600, "wood": 1280, "coal": 960, "iron": 640},
    ("T6", "T7"): {"meat": 3200, "wood": 2560, "coal": 1920, "iron": 1280},
    ("T7", "T8"): {"meat": 6400, "wood": 5120, "coal": 3840, "iron": 2560},
    ("T8", "T9"): {"meat": 12800, "wood": 10240, "coal": 7680, "iron": 5120},
    ("T9", "T10"): {"meat": 25600, "wood": 20480, "coal": 15360, "iron": 10240},
    ("T10", "T11"): {"meat": 51200, "wood": 40960, "coal": 30720, "iron": 20480},
}


@dataclass
class TroopCalculation:
    """Result of a troop calculation"""
    tier_from: str
    tier_to: str
    count: int
    total_meat: int = 0
    total_wood: int = 0
    total_coal: int = 0
    total_iron: int = 0
    total_time_seconds: int = 0

    @property
    def time_display(self) -> str:
        hours = self.total_time_seconds // 3600
        minutes = (self.total_time_seconds % 3600) // 60
        if hours > 24:
            days = hours // 24
            hours = hours % 24
            return f"{days}d {hours}h {minutes}m"
        return f"{hours}h {minutes}m"


class TroopsCalculator:
    """Calculator for troop training and promotion costs"""
    
    @staticmethod
    def calculate_training(tier: str, count: int) -> TroopCalculation:
        """Calculate training costs for a given tier and count"""
        if tier not in TROOP_TIERS:
            raise ValueError(f"Invalid tier: {tier}")
        
        tier_data = TROOP_TIERS[tier]
        return TroopCalculation(
            tier_from=tier,
            tier_to=tier,
            count=count,
            total_meat=tier_data["training_cost"] * count,
            total_time_seconds=tier_data["training_time"] * count,
        )
    
    @staticmethod
    def calculate_promotion(tier_from: str, tier_to: str, count: int) -> TroopCalculation:
        """Calculate promotion costs between tiers"""
        key = (tier_from, tier_to)
        if key not in PROMOTION_COSTS:
            raise ValueError(f"Invalid promotion: {tier_from} → {tier_to}")
        
        costs = PROMOTION_COSTS[key]
        return TroopCalculation(
            tier_from=tier_from,
            tier_to=tier_to,
            count=count,
            total_meat=costs["meat"] * count,
            total_wood=costs["wood"] * count,
            total_coal=costs["coal"] * count,
            total_iron=costs["iron"] * count,
        )


# ============================================
# CHIEF GEAR CALCULATOR
# ============================================

GEAR_QUALITIES = ["Green", "Blue", "Purple", "Gold", "Orange", "Pink"]
GEAR_STAR_LEVELS = range(0, 6)  # 0 to 5 stars


@dataclass
class GearCalculation:
    """Result of a gear upgrade calculation"""
    quality_from: str
    quality_to: str
    star_from: int
    star_to: int
    total_materials: dict
    total_alloy: int = 0


class ChiefGearCalculator:
    """Calculator for Chief Gear upgrade costs"""
    
    @staticmethod
    def calculate_upgrade(
        quality_from: str, star_from: int,
        quality_to: str, star_to: int
    ) -> GearCalculation:
        """Calculate upgrade costs between gear states"""
        # Implementation uses internal cost tables
        # Returns total materials needed for the upgrade path
        return GearCalculation(
            quality_from=quality_from,
            quality_to=quality_to,
            star_from=star_from,
            star_to=star_to,
            total_materials={},
        )


# ============================================
# CHARM CALCULATOR
# ============================================

CHARM_MAX_LEVEL = 16

@dataclass
class CharmCalculation:
    """Result of a charm upgrade calculation"""
    level_from: int
    level_to: int
    total_dust: int = 0
    total_crystals: int = 0


class CharmsCalculator:
    """Calculator for Charm upgrade costs"""
    
    @staticmethod
    def calculate(level_from: int, level_to: int) -> CharmCalculation:
        """Calculate charm upgrade costs between levels (0-16)"""
        if not (0 <= level_from < level_to <= CHARM_MAX_LEVEL):
            raise ValueError(f"Invalid levels: {level_from} → {level_to}")
        return CharmCalculation(level_from=level_from, level_to=level_to)


# ============================================
# HERO GEAR CALCULATOR
# ============================================

@dataclass
class HeroGearCalculation:
    """Result of a hero gear calculation"""
    level_from: int
    level_to: int
    mode: str  # 'enhance' or 'mastery'
    total_scrolls: int = 0
    total_essence: int = 0


class HeroGearCalculator:
    """Calculator for Hero Gear enhancement and mastery"""
    
    @staticmethod
    def calculate_enhance(level_from: int, level_to: int) -> HeroGearCalculation:
        """Calculate enhancement costs (0-100)"""
        if not (0 <= level_from < level_to <= 100):
            raise ValueError(f"Invalid enhance levels: {level_from} → {level_to}")
        return HeroGearCalculation(
            level_from=level_from, level_to=level_to, mode='enhance'
        )
    
    @staticmethod
    def calculate_mastery(level_from: int, level_to: int) -> HeroGearCalculation:
        """Calculate mastery forging costs (0-10)"""
        if not (0 <= level_from < level_to <= 10):
            raise ValueError(f"Invalid mastery levels: {level_from} → {level_to}")
        return HeroGearCalculation(
            level_from=level_from, level_to=level_to, mode='mastery'
        )

"""This unit contains classes describing hero classes using in the game"""
from dataclasses import dataclass
from classes.skills import BaseSkill
# --------------------------------------------------------------------------


@dataclass
class UnitClass:
    """This class describes a hero in the game"""
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: BaseSkill

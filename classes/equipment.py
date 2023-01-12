"""This unit contains classes describing equipment using in the
game"""
from dataclasses import dataclass
from random import uniform
from typing import List
from marshmallow import EXCLUDE
# ----------------------------------------------------------------------


@dataclass
class Weapon:
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    def get_damage(self) -> float:
        """The method serves to calculate certain damage

        Returns:
            The calculated damage
        """
        return uniform(self.min_damage, self.max_damage)

    class Meta:
        unknown = EXCLUDE


@dataclass
class Armor:
    name: str
    defence: float
    stamina_per_turn: float

    class Meta:
        unknown = EXCLUDE


@dataclass
class EquipmentData:
    weapons: List[Weapon]
    armors: List[Armor]


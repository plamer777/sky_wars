"""This unit contains classes describing units using in the game"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randint
from typing import Any
from classes.equipment import Armor, Weapon
from classes.hero_classes import UnitClass
# -------------------------------------------------------------------------


class Unit(ABC):

    @abstractmethod
    def _calc_hit_damage(self) -> float:
        pass

    @abstractmethod
    def get_total_damage(self, attacker: Any, damage: float) -> str:
        pass

    @abstractmethod
    def use_skill(self, target: Any) -> str:
        pass
# ------------------------------------------------------------------------->


@dataclass
class BaseUnit(Unit):

    name: str
    unit_class: UnitClass
    health: float
    stamina: float
    armor: Armor
    weapon: Weapon
    skill_used = False

    def _calc_hit_damage(self) -> float:
        damage = self.weapon.get_damage() * self.unit_class.attack
        return damage

    def add_stamina(self, stamina: float) -> None:

        self.stamina += stamina
        if self.stamina > self.unit_class.max_stamina:
            self.stamina = self.unit_class.max_stamina

    def get_total_damage(self, attacker: Any, damage: float) -> str:

        if self.stamina >= self.armor.stamina_per_turn:
            self.stamina -= self.armor.stamina_per_turn
            total_defence = self.armor.defence * self.unit_class.armor

        else:
            total_defence = 0

        if damage > total_defence:
            total_damage = damage - total_defence
            self.health -= total_damage
            return f"{attacker.name}, используя {attacker.weapon.name}, " \
                   f"пробивает {self.armor.name} соперника и наносит " \
                   f"{total_damage} урона."

        else:
            return f"{attacker.name}, использует {attacker.weapon.name}," \
                   f" но {self.armor.name} соперника стойко выдерживает удар"

    def use_skill(self, target: Unit) -> str:
        if self.skill_used:
            return "Навык уже использован, не надо читерить!"

        self.skill_used = True
        return self.unit_class.skill.use(self, target)

    def hit(self, target: Unit) -> str:

        if self.stamina >= self.weapon.stamina_per_hit:
            self.stamina -= self.weapon.stamina_per_hit
            damage = self._calc_hit_damage()
            return target.get_total_damage(self, damage)

        return f"{self.name} попытался использовать {self.weapon.name}, " \
               f"но у него не хватило выносливости."
# -------------------------------------------------------------------------


class UserUnit(BaseUnit):
    pass


class EnemyUnit(BaseUnit):

    def hit(self, target: Unit) -> str:

        if randint(0, 10) == 1 and not self.skill_used:
            return self.use_skill(target)

        else:
            return super().hit(target)

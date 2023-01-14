"""This unit contains classes describing units using in the game"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randint
from typing import Any
from classes.equipment import Armor, Weapon
from classes.hero_classes import UnitClass
# -------------------------------------------------------------------------


class Unit(ABC):
    """This is an abstractive class to be inherited by another classes"""
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
    """The BaseUnit class is a base class to create classes for player and
    computer unit"""
    name: str
    unit_class: UnitClass
    health: float
    stamina: float
    armor: Armor
    weapon: Weapon
    skill_used = False

    def _calc_hit_damage(self) -> float:
        """This method calculates a total damage

        :return: The total damage
        """
        damage = self.weapon.get_damage() * self.unit_class.attack
        return damage

    def add_stamina(self, stamina: float) -> None:
        """This method serves to increase a stamina amount

        :param stamina: a stamina value to add
        """
        self.stamina += stamina
        if self.stamina > self.unit_class.max_stamina:
            self.stamina = self.unit_class.max_stamina

    def get_total_damage(self, attacker: Any, damage: float) -> str:
        """This method serves to decrease a health amount calculating received
        damage considering defence level

        :param attacker: the striking player (an instance of BaseUnit class)
        :param damage: the amount of damage received by attacked player
        without defence

        :return: the string with the result of action (success or not)
        """
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
                   f"{total_damage:.2f} урона!"

        else:

            return f"{attacker.name}, использует {attacker.weapon.name}," \
                   f" но {self.armor.name} соперника стойко выдерживает удар!"

    def use_skill(self, target: Unit) -> str:
        """This method allows unit to use his skill but just once for a game

        :param target: the player that the skill is applied to

        :return - a string containing a result of the skill applying
        """
        if self.skill_used:
            return "Навык уже использован, не надо читерить!"

        self.skill_used = True
        return self.unit_class.skill.use(self, target)

    def hit(self, target: Unit) -> str:
        """This method allows unit to hit his opponent

        :param target: the attacked player (an instance of Unit class)

        :return - a string containing a result of the attack
        """
        if self.stamina >= self.weapon.stamina_per_hit:
            self.stamina -= self.weapon.stamina_per_hit
            damage = self._calc_hit_damage()

            return target.get_total_damage(self, damage)

        return f"{self.name} попытался использовать {self.weapon.name}, " \
               f"но у него не хватило выносливости:("
# -------------------------------------------------------------------------


class UserUnit(BaseUnit):
    """This class represents a player"""
    pass


class EnemyUnit(BaseUnit):
    """This class represents an opponent"""
    def hit(self, target: Unit) -> str:
        """This method allows unit to hit a player. Method was changed to
        use a skill randomly

        :param target: the attacked unit (an instance of Unit class)
        """
        if randint(0, 10) == 1 and not self.skill_used:
            return self.use_skill(target)

        else:
            return super().hit(target)

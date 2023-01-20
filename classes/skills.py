"""This unit contains classes describing skills using in the game"""
import dataclasses
from abc import ABC, abstractmethod
from typing import Any
# --------------------------------------------------------------------------


class Skill(ABC):
    """This class describes an interface of all skills using in the game"""
    @abstractmethod
    def skill_effect(self, user: Any) -> str:
        pass

    @abstractmethod
    def use(self, user: Any, target: Any) -> str:
        pass


@dataclasses.dataclass
class BaseSkill(Skill):
    """The BaseSkill class represents a special skill to use once for a game"""
    name: str
    damage: float
    stamina_required: float

    def skill_effect(self, unit: Any) -> str:
        """This method returns a string representing an effect of the skill

        :param unit: an instance of BaseUnit class representing user's or
        computer's unit

        :return: a string representing an effect of the using skill
        """
        return f"{unit.name} использует {self.name} и наносит {self.damage} "\
               f"урона сопернику!"

    def use(self, user: Any, target: Any) -> str:
        """This method returns a string with the result of using the skill
        and also calculates damage received by the opponent

        :param user: an instance of BaseUnit class representing a striker
        :param target: an instance of BaseUnit class representing an attacked
        unit

        :return: a string with the result of using the skill
        """
        if user.stamina >= self.stamina_required:
            target.health -= self.damage
            user.stamina -= self.stamina_required
            target.health = round(target.health, 2)

            return self.skill_effect(user)

        else:
            return f"{user.name} попытался использовать {self.name} но " \
                   f"выносливости не хватило и пупок развязался! "

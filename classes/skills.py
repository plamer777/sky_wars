"""This unit contains classes describing skills using in the game"""
import dataclasses
from abc import ABC, abstractmethod
from typing import Any
# --------------------------------------------------------------------------


class Skill(ABC):
    """This class describes an interface of all skills using in the game"""

    @abstractmethod
    def skill_effect(self, user: Any, damage: float) -> str:
        pass

    @abstractmethod
    def use(self, user: Any, target: Any) -> str:
        pass


@dataclasses.dataclass
class BaseSkill(Skill):

    name: str
    damage: float
    stamina_required: float

    def skill_effect(self, user: Any, damage: float) -> str:

        return f"{user.name} использует {self.name} и наносит {damage} " \
               f"урона сопернику."

    def use(self, user: Any, target: Any) -> str:
        if user.stamina >= self.stamina_required:
            target.health -= self.damage
            return self.skill_effect(user, self.damage)
        else:
            return f"{user.name} попытался использовать {self.name} но " \
                   f"выносливости не хватило и пупок развязался"

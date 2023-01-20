"""This unit contains classes describing a game arena"""
from typing import Optional, Dict, Any
from classes.unit import UserUnit, EnemyUnit
# --------------------------------------------------------------------------


class BaseArena:
    """The base class representing a singleton pattern"""
    _instance = None

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Arena(BaseArena):
    """This class represents an arena for players with necessary logic"""
    def __init__(self) -> None:
        """Initialization of the Arena class
        """
        self._recovery: int = 1
        self._player: Optional[UserUnit] = None
        self._enemy: Optional[EnemyUnit] = None
        self._game_started: bool = False
        self._battle_result: str = ''

    def start_game(self, player: UserUnit, enemy: EnemyUnit) -> None:
        """This method prepares the arena for the given players

        :param player: an instance of a UserUnit
        :param enemy: an instance of a EnemyUnit
        """
        self._player = player
        self._enemy = enemy
        self._game_started = True

    def next_step(self) -> Dict[str, str]:
        """This method serves to skip a turn and to process a computer's
        player actions

        :return: a dictionary with game logs
        """
        if not self._game_started:
            return {'result': '', 'battle_result': 'Игра завершена'}

        if self._enemy:
            result = self._enemy.hit(self._player)  # type: ignore

        else:
            result = 'Данные не загружены'

        if self.check_health():
            self.recover_stamina()

        else:
            self._battle_result = self.finish_game()

        return {'result': result, 'battle_result': self._battle_result}

    def recover_stamina(self) -> None:
        """This method serves to recover stamina after the actions of both
        players"""
        if self._player and self._enemy:
            self._player.add_stamina(
                self._player.unit_class.stamina * self._recovery)
            self._enemy.add_stamina(
                self._enemy.unit_class.stamina * self._recovery)

    def check_health(self) -> bool:
        """This method serves to check health of both players

        :return: a boolean indicating if health is above zero
        """
        if not self._player or not self._enemy:
            return False

        if self._player.health < 0 or self._enemy.health < 0:
            return False

        return True

    def hit_rival(self) -> Dict[str, str]:
        """This method allows user's player to hit an opponent

        :return: a dictionary containing game logs
        """
        if not self._game_started:
            return {'result': '', 'battle_result': 'Игра завершена'}

        if self._player:
            result = self._player.hit(self._enemy)  # type: ignore
            full_result = self.next_step()
            full_result['result'] = result + ' ' + full_result['result']
        else:
            full_result = {'result': '', 'battle_result': 'Нет данных'}

        return full_result

    def use_skill(self) -> Dict[str, str]:
        """This method allows user's player to use a special skill

        :return: a dictionary containing game logs
        """
        if not self._game_started:
            return {'result': '', 'battle_result': 'Игра завершена'}

        if self._player:
            result = self._player.use_skill(self._enemy)  # type: ignore
            full_result = self.next_step()
            full_result['result'] = result + ' ' + full_result['result']
        else:
            full_result = {'result': '', 'battle_result': 'Нет данных'}

        return full_result

    def finish_game(self) -> str:
        """This method used to finish the game and return the final result
        of the battle

        :return: a string containing the final result of the game
        """
        self._game_started = False

        result = "{0} наносит сокрушительный удар по {1} одерживая победу"

        if not self._player or not self._enemy:
            return "Данные игрока или противника не загружены"

        if self._player.health < 0 and self._enemy.health < 0:
            return f"{self._player.name} и {self._enemy.name} держались " \
                   f"одинаково хорошо, бой закончился в ничью"

        elif self._player.health > self._enemy.health:
            return result.format(self._player.name, self._enemy.name)

        elif self._enemy.health > self._player.health:
            return result.format(self._enemy.name, self._player.name)

        else:
            return "Не можем определить победителя"

    def clean(self) -> None:
        """This method is required to clean the arena for the next game"""
        self._player = None
        self._enemy = None
        self._battle_result = ''
        self._game_started = False

from typing import Optional
from unit import UserUnit, EnemyUnit
# --------------------------------------------------------------------------


class BaseArena:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Arena(BaseArena):

    def __init__(self):

        self.recovery = 2
        self.player: Optional[UserUnit] = None
        self.enemy: Optional[EnemyUnit] = None
        self.game_started = False

    def start_game(self, player: UserUnit, enemy: EnemyUnit):

        self.player = player
        self.enemy = enemy
        self.game_started = True

    def next_step(self):

        if self.check_health():
            self.recover_stamina()

        else:
            self.finish_game()

    def recover_stamina(self):
        self.player.add_stamina(self.player.unit_class.stamina * self.recovery)
        self.enemy.add_stamina(self.enemy.unit_class.stamina * self.recovery)

    def check_health(self):

        if self.player.health <= 0 or self.enemy.health <= 0:
            return False

        return True

    def hit_rival(self):

        result = self.player.hit(self.enemy)
        self.next_step()

        return result

    def use_skill(self):

        result = self.player.use_skill(self.enemy)
        self.next_step()

        return result

    def finish_game(self):

        result = "{0} наносит сокрушительный удар по {1} одерживая победу"

        if self.player.health > 0:
            return result.format(self.player.name, self.enemy.name)

        elif self.enemy.health > 0:
            return result.format(self.enemy.name, self.player.name)

        else:
            return f"{self.player.name} и {self.enemy.name} держались " \
                   f"одинаково хорошо, бой закончился в ничью"

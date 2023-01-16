"""This unit contains a HeroFactory class serving to create a UnitClass
instances"""
from typing import Type, Union, Optional, Dict, Any
from factories.equipment_factory import EquipmentFactory
from factories.unitclass_factory import UnitClassFactory
from classes.unit import EnemyUnit, UserUnit
from classes.user_requests import UserRequest
# -------------------------------------------------------------------------


class HeroFactory:
    """The HeroFactory class serves to create a UnitClass instances"""
    def __init__(self) -> None:
        """Initialization of the HeroFactory"""
        self._equipment_factory: EquipmentFactory = EquipmentFactory()
        self._unit_class_factory: UnitClassFactory = UnitClassFactory()
        self._user_unit: Type[UserUnit] = UserUnit
        self._enemy_unit: Type[EnemyUnit] = EnemyUnit

    def get_full_info(self) -> Dict[str, Any]:
        """This method creates a dictionary with all available unit classes,
        weapon and armor

        :return: a dictionary with all available hero classes, weapon and armor
        """
        result = {
            "classes": self._unit_class_factory.get_class_names(),
            "weapons": self._equipment_factory.get_weapon_names(),
            "armors": self._equipment_factory.get_armor_names()
        }

        return result

    def create_hero(self, request: UserRequest) -> Optional[UserUnit]:
        """This method creates an instance of the UserUnit class for the
        player's unit

        :param request: an instance of UserRequest with data create requested
        unit

        :return: an instance of the UserUnit class
        """
        hero = self._create_unit(request, self._user_unit)

        if type(hero) is UserUnit:
            return hero

        return None

    def create_enemy(self, request: UserRequest) -> Optional[EnemyUnit]:
        """This method creates an instance of the EnemyUnit class for the
        computer's unit

        :param request: an instance of UserRequest with data create requested
        unit

        :return: an instance of the EnemyUnit class
        """
        enemy = self._create_unit(request, self._enemy_unit)

        if type(enemy) is EnemyUnit:
            return enemy

        return None

    def _create_unit(self, request: UserRequest,
                     unit: Union[Type[UserUnit], Type[EnemyUnit]]) -> \
            Union[EnemyUnit, UserUnit, None]:
        """This closed method creates an instance of either UserUnit or
        EnemyUnit class depending on request data

        :param request: an instance of UserRequest with data create
        :param unit: UserUnit or EnemyUnit class

        :return: an instance of either UserUnit or EnemyUnit
        """
        name = request.name
        unit_cls = self._unit_class_factory.get_hero_class(request.unit_class)
        weapon = self._equipment_factory.get_weapon(request.weapon)
        armor = self._equipment_factory.get_armor(request.armor)

        try:
            result = unit(name, unit_cls, unit_cls.max_health,  # type: ignore
                          unit_cls.max_stamina, armor, weapon)  # type: ignore

        except Exception as e:
            print(f"Не удалось создать персонажа, код ошибки {e}")
            return None

        return result

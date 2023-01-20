"""This unit contains TestHeroFactory class to test HeroFactory"""
from itertools import product
from typing import List, Iterable, Dict
from classes.unit import UserUnit, EnemyUnit
from classes.user_requests import UserRequest
from factories.hero_factory import HeroFactory
from tests.utils import check_class_types, check_class_names
# -------------------------------------------------------------------------


class TestHeroFactory:
    """The TestHeroFactory class provides all necessary methods to test
    original methods of HeroFactory"""
    def test_get_full_info(self, unit_factory: HeroFactory) -> None:
        """This method tests the get_class_names method of the
        HeroFactory

        :param unit_factory: a fixture representing an instance of
        HeroFactory class
        """
        unit_class_names = unit_factory.get_full_info()
        for class_names in unit_class_names.values():
            check_class_names(class_names)

    def test_get_unit_class(self, unit_factory: HeroFactory) -> None:
        """This method tests the get_hero and get_enemy methods of the
        HeroFactory

        :param unit_factory: a fixture representing an instance of
        HeroFactory class
        """
        names = unit_factory.get_full_info()
        hero_classes = names['classes']
        equip_list = product(names['weapons'], names['armors'])
        requests_list = (UserRequest('test', unit_class, equip[0], equip[1])
                         for unit_class, equip in
                         product(hero_classes, equip_list))
        units = self._create_test_units(unit_factory, requests_list)

        check_class_types(units.get('heroes'), UserUnit)
        check_class_types(units.get('enemies'), EnemyUnit)

    @staticmethod
    def _create_test_units(unit_factory: HeroFactory,
                           requests_list: Iterable[UserRequest]) -> \
            dict[str, List[EnemyUnit | UserUnit]]:
        """This method creates a dictionary with requested heroes and
        enemies

        :param unit_factory: a fixture representing an instance of
        HeroFactory class
        :param requests_list: a list of UserRequest instances

        :returns: a dictionary with requested heroes and enemies
        """
        units: Dict[str, list] = {
            'heroes': [],
            'enemies': []
        }

        for user_request in requests_list:
            hero = unit_factory.create_hero(user_request)
            enemy = unit_factory.create_enemy(user_request)
            units['heroes'].append(hero)
            units['enemies'].append(enemy)

        return units

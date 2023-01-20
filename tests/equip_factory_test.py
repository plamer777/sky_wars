"""This unit contains TestEquipmentFactory class to test EquipmentFactory"""
from classes.equipment import Armor, Weapon
from factories.equipment_factory import EquipmentFactory
from tests.utils import check_class_names, check_class_types
# -------------------------------------------------------------------------


class TestEquipmentFactory:
    """The TestEquipmentFactory class provides all necessary methods to test
    original methods of EquipmentFactory"""
    def test_get_weapon_names(self, equip_factory: EquipmentFactory) -> None:
        """This method tests the get_class_names method of the
        EquipmentFactory

        :param equip_factory: a fixture representing an instance of
        EquipmentFactory class
        """
        weapon_names = equip_factory.get_weapon_names()

        check_class_names(weapon_names)

    def test_get_armor_names(self, equip_factory: EquipmentFactory) -> None:
        """This method tests the get_armor_names method of the
        UnitClassFactory

        :param equip_factory: a fixture representing an instance of
        EquipmentFactory class
        """
        armor_names = equip_factory.get_armor_names()

        check_class_names(armor_names)

    def test_get_armor(self, equip_factory: EquipmentFactory) -> None:
        """This method tests the get_armor_names method of the
        EquipmentFactory

        :param equip_factory: a fixture representing an instance of
        EquipmentFactory class
        """

        armor_names = equip_factory.get_armor_names()
        armor_list = [equip_factory.get_armor(name) for name in armor_names]
        check_class_types(armor_list, Armor)

    def test_get_weapon(self, equip_factory: EquipmentFactory) -> None:
        """This method tests the get_weapon method of the
        EquipmentFactory

        :param equip_factory: a fixture representing an instance of
        EquipmentFactory class
        """

        weapon_names = equip_factory.get_weapon_names()
        weapon_list = [equip_factory.get_weapon(name) for name in weapon_names]
        check_class_types(weapon_list, Weapon)

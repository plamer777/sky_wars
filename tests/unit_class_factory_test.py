"""This unit contains TestUnitClassFactory class to test UnitClassFactory"""
from classes.hero_classes import UnitClass
from factories.unitclass_factory import UnitClassFactory
from tests.utils import check_class_types, check_class_names
# -------------------------------------------------------------------------


class TestUnitClassFactory:
    """The TestUnitClassFactory class provides all necessary methods to test
    original methods of UnitClassFactory"""
    def test_get_class_names(self, class_factory: UnitClassFactory) -> None:
        """This method tests the get_class_names method of the
        UnitClassFactory

        :param class_factory: a fixture representing an instance of
        UnitClassFactory class
        """
        unit_class_names = class_factory.get_class_names()

        check_class_names(unit_class_names)

    def test_get_unit_class(self, class_factory: UnitClassFactory) -> None:
        """This method tests the get_hero_class method of the
        UnitClassFactory

        :param class_factory: a fixture representing an instance of
        UnitClassFactory class
        """
        names = class_factory.get_class_names()
        unit_classes = [class_factory.get_hero_class(name) for name in names]
        check_class_types(unit_classes, UnitClass)

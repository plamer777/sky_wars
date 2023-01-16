"""This file contains a fixtures for testing purposes"""
import pytest
from factories.equipment_factory import EquipmentFactory
from factories.hero_factory import HeroFactory
from factories.unitclass_factory import UnitClassFactory
# --------------------------------------------------------------------------


@pytest.fixture(scope="session")
def equip_factory() -> EquipmentFactory:
    """This fixture provides an instance of EquipmentFactory"""
    return EquipmentFactory()


@pytest.fixture(scope="session")
def class_factory() -> UnitClassFactory:
    """This fixture provides an instance of UnitClassFactory"""
    return UnitClassFactory()


@pytest.fixture(scope="session")
def unit_factory() -> HeroFactory:
    """This fixture provides an instance of HeroFactory"""
    return HeroFactory()

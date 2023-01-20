"""This file contains a fixtures for testing purposes"""
from random import choice
from typing import Any, List
from flask.testing import FlaskClient
import pytest
from factories.equipment_factory import EquipmentFactory
from factories.hero_factory import HeroFactory
from factories.unitclass_factory import UnitClassFactory
from app import app
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


@pytest.fixture(scope="session")
def app_client() -> FlaskClient:
    """This fixture serves as a test client for the application"""
    return app.test_client()


@pytest.fixture()
def random_request(unit_factory) -> dict[str, Any]:
    """This fixture serves to provide a randomly generated dictionary
    """
    total_data = unit_factory.get_full_info()

    user_choice = {
        'name': 'Legat',
        'unit_class': choice(total_data.get('classes')),
        'weapon': choice(total_data.get('weapons')),
        'armor': choice(total_data.get('armors'))
    }

    return user_choice


@pytest.fixture(scope="session")
def actions() -> List[str]:
    """This fixture serves to provide a list of available actions in the
    game"""
    return ['hit', 'use-skill', 'pass-turn']

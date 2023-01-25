"""This unit contains EquipmentDao class serves to get ArmorModels and
WeaponModels classes from the database"""
from typing import List
from db.db_setup import db
from db.models.equipment_models import ArmorModel, WeaponModel
# ------------------------------------------------------------------------


class EquipmentDao:
    """
    Data access object for equipment data
    """
    def __init__(self) -> None:
        """
        Initializes the EquipmentDao and creates a session for database queries
        """
        self.db = db.session

    def get_all_armor(self) -> List[ArmorModel]:
        """
        Retrieves all armors from the database
        :return: a list of ArmorModel objects
        """
        armors = self.db.query(ArmorModel).all()

        return armors

    def get_all_weapon(self) -> List[WeaponModel]:
        """
        Retrieves all weapons from the database
        :return: a list of WeaponModel objects
        """
        weapons = self.db.query(WeaponModel).all()

        return weapons

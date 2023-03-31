"""This unit contains EquipmentDao class serves to get ArmorModels and
WeaponModels classes from the database"""
from typing import List
from db.db_setup import db
from db.models import ArmorModel, WeaponModel, WeaponSchema, ArmorSchema
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

    def add_weapon(self, weapon: WeaponSchema) -> WeaponModel:
        """This method adds a weapon to the database
        :param weapon: an instance of WeaponSchema class
        :return: an instance of WeaponModel class
        """
        new_weapon = WeaponModel(**weapon.dict())

        self.db.add(new_weapon)
        self.db.commit()

        return new_weapon

    def add_armor(self, armor: ArmorSchema) -> ArmorModel:
        """This method adds an armor to the database
        :param armor: an instance of ArmorSchema class
        :return: an instance of ArmorModel class
        """
        new_armor = ArmorModel(**armor.dict())

        self.db.add(new_armor)
        self.db.commit()

        return new_armor

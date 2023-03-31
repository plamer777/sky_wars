"""This unit contains EquipmentService provided a business logic to get
necessary data armors and weapons tables of the database"""
from typing import Dict, List, Any

from dao.equipment_dao import EquipmentDao
from db.models import ArmorSchema, WeaponSchema
# ------------------------------------------------------------------------


class EquipmentService:
    """The EquipmentService class provides all necessary methods to get
    armors and weapons list for game process"""
    def __init__(self) -> None:
        """Initialize the EquipmentService and creates an instance of
        EquipmentDao"""
        self.equipment_dao = EquipmentDao()

    def get_all(self) -> Dict[str, List[Dict]]:
        """This method returns a dictionary representing game's equipment

        :return: Dictionary containing a list of dictionaries
        """
        armor_models = self.equipment_dao.get_all_armor()
        weapon_models = self.equipment_dao.get_all_weapon()

        all_equipment = {
            'armors': [ArmorSchema.from_orm(armor).dict() for armor in
                       armor_models],
            'weapons': [WeaponSchema.from_orm(weapon).dict() for weapon in
                        weapon_models]
        }

        return all_equipment

    def add_weapon(self, weapon_data: dict[str, Any]) -> \
            str:
        """This method serves to add a new weapon to the game process
        :param weapon_data: A dictionary representing the weapon data
        :return: A string representing the result of the operation
        """
        try:
            validated_data = WeaponSchema(**weapon_data)
            self.equipment_dao.add_weapon(validated_data)
            return 'Added successfully'

        except Exception as e:
            return f'Failed to add weapon, error: {e}'

    def add_armor(self, armor_data: dict[str, Any]) -> str:
        """This method serves to add a new armor to the game process
        :param armor_data: A dictionary representing the armor data
        :return: A string representing the result of the operation
        """
        try:
            validated_data = ArmorSchema(**armor_data)
            self.equipment_dao.add_armor(validated_data)
            return 'Added successfully'

        except Exception as e:
            return f'Failed to add armor, error: {e}'

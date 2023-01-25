"""This unit contains EquipmentService provided a business logic to get
necessary data armors and weapons tables of the database"""
from typing import Dict, List
from dao.equipment_dao import EquipmentDao
from db.models.equipment_models import ArmorSchema, WeaponSchema
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

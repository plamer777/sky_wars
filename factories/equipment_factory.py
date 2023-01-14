"""This unit contains EquipmentFactory class to load and get necessary game's
equipment"""
from typing import List, Optional
from marshmallow_dataclass import class_schema
from marshmallow import ValidationError
from classes.equipment import EquipmentData, Weapon, Armor
from utils import load_from_json
from constants import EQUIPMENT_FILE
# ------------------------------------------------------------------------


class EquipmentFactory:
    """This class contains factory methods to load and get necessary game's
    equipment"""
    def __init__(self) -> None:
        self.equipment: Optional[EquipmentData] = self._load_all()

    @staticmethod
    def _load_all() -> Optional[EquipmentData]:
        """This closed method serves to load all available equipment from
        the json file

        :return: EquipmentData instance or None if there was an error during
        loading data
        """
        EquipmentSchema = class_schema(EquipmentData)
        equipments = load_from_json(EQUIPMENT_FILE)

        try:
            result = EquipmentSchema().load(equipments)
            return result
        except ValidationError as e:
            print(f"Ошибка валидации данных {e}")
            return None

    def get_weapon(self, weapon: str) -> Optional[Weapon]:
        """This method serves to get a weapon by its name

        :param weapon: a name of the required weapon
        :return: Weapon instance or None if there wasn't available
        weapon"""
        if self.equipment:
            found_weapon = list(filter(lambda x: x.name.lower() ==
                                       weapon.lower(), self.equipment.weapons))

            return found_weapon[0] if found_weapon else \
                self.equipment.weapons[0]

        return None

    def get_armor(self, armor: str) -> Optional[Armor]:
        """This method serves to get an armor by its name

        :param armor: a name of the required armor
        :return: Armor instance or None if there wasn't available
        armor"""
        if self.equipment:
            found_armor = list(filter(lambda x: x.name.lower() ==
                                      armor.lower(), self.equipment.armors))

            return found_armor[0] if found_armor else self.equipment.armors[0]

        return None

    def get_weapon_names(self) -> List[str]:
        """This method serves to get a list of all weapon names

        :return: a list of all weapon names"""
        if self.equipment:
            return list(map(lambda x: x.name, self.equipment.weapons))

        return []

    def get_armor_names(self) -> List[str]:
        """This method serves to get a list of all armor names

        :return: a list of all armor names
        """
        if self.equipment:
            return list(map(lambda x: x.name, self.equipment.armors))

        return []

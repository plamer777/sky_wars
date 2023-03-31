"""This unit contains UnitClassService provided a business logic to get
necessary data from the database"""
from typing import List, Dict, Any
from dao.unit_class_dao import UnitClassDao
from db.models import UnitClassSchema
# ------------------------------------------------------------------------


class UnitClassService:
    """
    Service class that handles business logic for unit classes
    """
    def __init__(self) -> None:
        """
        Initializes the UnitClassService and creates an instance of
        the UnitClassDao
        """
        self.unit_class_dao = UnitClassDao()

    def get_all(self) -> List[Dict[str, Any]]:
        """
        Retrieves all unit classes from the database and converts them to a
        list of dictionaries
        :return: a list of dictionaries representing all unit classes
        """
        unit_class_models = self.unit_class_dao.get_all()

        all_unit_classes = [UnitClassSchema.from_orm(
            unit_model).dict() for unit_model in unit_class_models]

        return all_unit_classes

    def add_new(self, unit_class: dict) -> str:
        """This method serves to add a new unit class to the game process
        :param unit_class: A dictionary representing the unit class data
        :return: A string representing the result of the operation
        """
        try:
            new_unit_class = UnitClassSchema(**unit_class)
            self.unit_class_dao.add_new(new_unit_class)
            return 'Added successfully'

        except Exception as e:
            return f'Failed to add unit class, error: {e}'

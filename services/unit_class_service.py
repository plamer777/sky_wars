"""This unit contains UnitClassService provided a business logic to get
necessary data from the database"""
from typing import List, Dict, Any
from dao.unit_class_dao import UnitClassDao
from db.models.unit_class_model import UnitClassSchema
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

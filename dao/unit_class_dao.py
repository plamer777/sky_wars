"""This unit contains UnitClassDao class provides a list of UnitClassModels
to be used by Service classes"""
from typing import List
from db.db_setup import db
from db.models.unit_class_model import UnitClassModel
# ------------------------------------------------------------------------


class UnitClassDao:
    """
    The UnitClassDao is a data access object for unit classes data
    """
    def __init__(self) -> None:
        """
        Initializes the UnitClassDao and creates a session for database queries
        """
        self.db = db.session

    def get_all(self) -> List[UnitClassModel]:
        """This method returns a list of all UnitClassModels available in the
        database

        :return: a list of UnitClassModels
        """
        all_classes = self.db.query(UnitClassModel).all()

        return all_classes

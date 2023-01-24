"""This unit contains SkillsDao class serves to get models representing
skills using in the game"""
from typing import List
from db.db_setup import db
from db.models.skills_model import SkillModel
# ------------------------------------------------------------------------


class SkillsDao:
    """
    The SkillsDao is a data access object for skills table
    """
    def __init__(self) -> None:
        """
        Initializes the SkillsDao and creates a session for database queries
        """
        self.db = db.session

    def get_all(self) -> List[SkillModel]:
        """This method returns a list of SkillModel classes

        :return: a list of SkillModel classes
        """
        all_skills = self.db.query(SkillModel).all()

        return all_skills

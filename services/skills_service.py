"""This unit contains SkillsService class provided a business logic to get
available skills from database and prepare them for using in the game"""
from typing import List, Dict, Any
from dao.skills_dao import SkillsDao
from db.models import SkillSchema
# ------------------------------------------------------------------------


class SkillsService:
    """The SkillsService class includes methods to provide game skills in
    the required form"""
    def __init__(self) -> None:
        """Initializes the SkillsService class and creates an instance of
        SkillsDao class"""
        self.skills_dao = SkillsDao()

    def get_all(self) -> List[Dict[str, Any]]:
        """This method returns all skills using in the game

        :return: A list of dictionaries containing skill's data
        """
        skill_models = self.skills_dao.get_all()

        all_skills = [SkillSchema.from_orm(
            skill_model).dict() for skill_model in skill_models]

        return all_skills

    def add_new(self, skill_data: dict) -> str:
        """This method serves to add a new skill to the game process
        :param skill_data: A dictionary representing the skill data
        :return: A string representing the result of the operation
        """
        try:
            new_skill = SkillSchema(**skill_data)
            self.skills_dao.add_new(new_skill)
            return 'Added successfully'

        except Exception as e:
            return f'Failed to add new skill, error: {e}'

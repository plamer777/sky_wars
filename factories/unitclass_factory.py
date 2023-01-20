"""This unit contains UnitClassFactory class to load and get necessary game's
hero classes"""
from typing import List, Optional
from random import shuffle
from marshmallow_dataclass import class_schema
from marshmallow import ValidationError
from classes.hero_classes import UnitClass
from utils import load_from_json
from constants import CLASSES_FILE, SKILLS_FILE, LOGS_FILE, DEFAULT_NEGATIVE, \
    DEFAULT_POSITIVE
# ------------------------------------------------------------------------


class UnitClassFactory:
    """This class contains factory methods to load and get necessary game's
    equipment"""

    def __init__(self) -> None:
        self.classes: Optional[List[UnitClass]] = self._load_all()

    @staticmethod
    def _load_all() -> Optional[List[UnitClass]]:
        """This closed method serves to load all available hero classes from
        the json file

        :return: UnitClass instance or None if there was an error during
        loading data
        """
        UnitClassSchema = class_schema(UnitClass)
        heroes = load_from_json(CLASSES_FILE)
        skills = load_from_json(SKILLS_FILE)
        phrases = load_from_json(LOGS_FILE)
        if type(skills) is list:
            shuffle(skills)

        try:
            for hero in heroes:
                hero['skill'] = skills.pop()
                hero['positive_logs'] = phrases.get('positive_logs',
                                                    DEFAULT_POSITIVE)
                hero['negative_logs'] = phrases.get('negative_logs',
                                                    DEFAULT_NEGATIVE)

            result = UnitClassSchema().load(heroes, many=True)
            return result

        except ValidationError as e:
            print(f"Ошибка валидации данных {e}")
            return None

    def get_hero_class(self, class_name: str) -> Optional[UnitClass]:
        """This method serves to get a hero class by its name

        :param class_name: a name of the required class of hero

        :return: UnitClass instance or None if there wasn't available
        class"""
        if self.classes:
            found_class = list(filter(
                lambda x: x.name.lower() == class_name.lower(), self.classes))

            return found_class[0] if found_class else self.classes[0]

        return None

    def get_class_names(self) -> Optional[List[str]]:
        """This method serves to get a list of all hero class names

        :return: a list of all hero class names"""
        if self.classes:
            return list(map(lambda x: x.name, self.classes))

        return None

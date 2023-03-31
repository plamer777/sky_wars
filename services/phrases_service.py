"""This unit contains PhrasesService class provided a business logic to get
unit's phrases"""
from typing import Dict, List
from dao.phrases_dao import PhrasesDao
from db.models import PhraseSchema
# ------------------------------------------------------------------------


class PhrasesService:
    """The PhrasesService class contains all methods to get phrases using in
    the game"""
    def __init__(self) -> None:
        """Initializes PhrasesService class and creates an instance of
        PhrasesDao"""
        self.phrases_dao = PhrasesDao()

    def get_all(self) -> Dict[str, List[str]]:
        """This method returns all game phases

        :return: A dictionary with positive and negative phrases
        """
        positive = self.phrases_dao.get_all_positive()
        negative = self.phrases_dao.get_all_negative()

        positive_logs = [PhraseSchema.from_orm(
            phrase).dict()['phrase'] for phrase in positive]
        negative_logs = [PhraseSchema.from_orm(
            phrase).dict()['phrase'] for phrase in negative]

        all_phrases = {'positive_logs': positive_logs,
                       'negative_logs': negative_logs
                       }

        return all_phrases

    def add_new(self, positive_log: str, negative_log: str) -> str:
        """This method serves to add a new phrases to the game process
        :param positive_log: A string representing the positive phrase
        :param negative_log: A string representing the negative phrase
        :return: A string representing the result of the operation
        """
        try:
            positive_schema = PhraseSchema(phrase=positive_log)
            negative_schema = PhraseSchema(phrase=negative_log)
            self.phrases_dao.add_positive(positive_schema)
            self.phrases_dao.add_negative(negative_schema)

            return 'Added successfully'

        except Exception as e:
            return f'Failed to add phrases, error: {e}'

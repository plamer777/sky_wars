"""This unit contains PhrasesDao class serves to get classes representing
positive and negative phrases from the database"""
from typing import List
from db.db_setup import db
from db.models.phrase_models import PositivePhraseModel, NegativePhraseModel
# ------------------------------------------------------------------------


class PhrasesDao:
    """
    The PhrasesDao is a data access object for phrases data
    """
    def __init__(self) -> None:
        """
        Initializes the PhrasesDao and creates a session for database queries
        """
        self.db = db.session

    def get_all_positive(self) -> List[PositivePhraseModel]:
        """This method returns a list of models representing positive
        phrases

        :return: a list of PositivePhraseModels
        """
        positive_phrases = self.db.query(PositivePhraseModel).all()

        return positive_phrases

    def get_all_negative(self) -> List[NegativePhraseModel]:
        """This method returns a list of models representing negative
        phrases

        :return: a list of NegativePhraseModels
        """
        negative_phrases = self.db.query(NegativePhraseModel).all()

        return negative_phrases

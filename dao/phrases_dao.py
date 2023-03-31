"""This unit contains PhrasesDao class serves to get classes representing
positive and negative phrases from the database"""
from typing import List, Union, Any
from db.db_setup import db
from db.models import PositivePhraseModel, NegativePhraseModel, PhraseSchema
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

    def add_positive(self, phrase: PhraseSchema) -> PositivePhraseModel:
        """This method adds a positive phrase to the database
        :param phrase: an instance of PhraseSchema class
        :return: a PositivePhraseModel class instance
        """
        new_positive = self._add_phrase(phrase, PositivePhraseModel)

        return new_positive

    def add_negative(self, phrase: PhraseSchema) -> NegativePhraseModel:
        """This method adds a negative phrase to the database
        :param phrase: an instance of PhraseSchema class
        :return: a NegativePhraseModel class instance
        """
        new_negative = self._add_phrase(phrase, NegativePhraseModel)

        return new_negative

    def _add_phrase(self, phrase: PhraseSchema, model: Any) -> \
            Union[PositivePhraseModel, NegativePhraseModel]:
        """This is an additional method helps to add phrases to the database
        :param phrase: an instance of PhraseSchema class
        :param model: an instance of PositivePhraseModel or NegativePhraseModel
        :return: an instance of PositivePhraseModel or NegativePhraseModel
        """
        new_phrase = model(**phrase.dict())

        self.db.add(new_phrase)
        self.db.commit()

        return new_phrase

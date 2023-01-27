"""This unit contains models and schemas for tables with phrases using in the
game process"""
from flask_sqlalchemy.model import Model
from db.db_setup import db
from pydantic import BaseModel
# ---------------------------------------------------------------------------


class PositivePhraseModel(db.Model):
    """
    Model class for the positive_phrases table in the database
    """
    __tablename__ = 'positive_phrases'
    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(150))


class NegativePhraseModel(db.Model):
    """
    Model class for the negative_phrases table in the database
    """
    __tablename__ = 'negative_phrases'
    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(150))


class PhraseSchema(BaseModel):
    """
    Schema class for the positive_phrases and negative_phrases table in the
    database
    """
    phrase: str

    class Config:
        orm_mode = True

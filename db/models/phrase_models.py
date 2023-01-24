from db.db_setup import db
from pydantic import BaseModel
# ---------------------------------------------------------------------------


class PositivePhraseModel(db.Model):
    __tablename__ = 'positive_phrases'
    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(150))


class NegativePhraseModel(db.Model):
    __tablename__ = 'negative_phrases'
    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(150))


class PhraseSchema(BaseModel):
    phrase: str

    class Config:
        orm_mode = True

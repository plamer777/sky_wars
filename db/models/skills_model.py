"""This unit contains models and schemas for table with available skills for
the game process"""
from flask_sqlalchemy.model import Model
from db.db_setup import db
from pydantic import BaseModel
# ---------------------------------------------------------------------------


class SkillModel(db.Model):
    """
    Model class for the skills table in the database
    """
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    damage = db.Column(db.Float)
    stamina_required = db.Column(db.Float)


class SkillSchema(BaseModel):
    """
    Schema class for the skills table in the database
    """
    name: str
    damage: float
    stamina_required: float

    class Config:
        orm_mode = True

from db.db_setup import db
from pydantic import BaseModel
# -------------------------------------------------------------------------


class UnitClassModel(db.Model):

    __tablename__ = 'unit_classes'
    id = db.Column(db.Integer, primary_key=True)
    armor = db.Column(db.Float)
    attack = db.Column(db.Float)
    max_health = db.Column(db.Float)
    max_stamina = db.Column(db.Float)
    name = db.Column(db.String(20))
    stamina = db.Column(db.Float)
    avatar = db.Column(db.String(30))


class UnitClassSchema(BaseModel):
    armor: float
    attack: float
    max_health: float
    max_stamina: float
    name: str
    stamina: float
    avatar: str

    class Config:
        orm_mode = True

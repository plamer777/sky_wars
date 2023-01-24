from db.db_setup import db
from pydantic import BaseModel
# ---------------------------------------------------------------------------


class WeaponModel(db.Model):
    __tablename__ = 'weapon'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    log_name = db.Column(db.String(30))
    min_damage = db.Column(db.Float)
    max_damage = db.Column(db.Float)
    stamina_per_hit = db.Column(db.Float)


class ArmorModel(db.Model):
    __tablename__ = 'armor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    defence = db.Column(db.Float)
    stamina_per_turn = db.Column(db.Float)


class WeaponSchema(BaseModel):
    name: str
    log_name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    class Config:
        orm_mode = True


class ArmorSchema(BaseModel):
    name: str
    defence: float
    stamina_per_turn: float

    class Config:
        orm_mode = True

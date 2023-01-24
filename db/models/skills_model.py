from db.db_setup import db
from pydantic import BaseModel
# ---------------------------------------------------------------------------


class SkillModel(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    damage = db.Column(db.Float)
    stamina_required = db.Column(db.Float)


class SkillSchema(BaseModel):
    name: str
    damage: float
    stamina_required: float

    class Config:
        orm_mode = True

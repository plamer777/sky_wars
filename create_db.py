from utils import load_from_json
from init_app import app
from db.db_setup import db
from db.models.phrase_models import PositivePhraseModel, NegativePhraseModel
from db.models.equipment_models import ArmorModel, WeaponModel
from db.models.skills_model import SkillModel
from db.models.unit_class_model import UnitClassModel
from constants import EQUIPMENT_FILE, LOGS_FILE, CLASSES_FILE, SKILLS_FILE
# -------------------------------------------------------------------------


def create_database():
    db.create_all()
    equipment = load_from_json(EQUIPMENT_FILE)
    classes = load_from_json(CLASSES_FILE)
    phrases = load_from_json(LOGS_FILE)
    skills = load_from_json(SKILLS_FILE)
    armors = equipment['armors']
    weapons = equipment['weapons']

    positive_phrases = [{'id': num, 'phrase': phrase}
                        for num, phrase in enumerate(phrases['positive_logs'],
                                                     1)]
    negative_phrases = [{'id': num, 'phrase': phrase}
                        for num, phrase in enumerate(phrases['negative_logs'],
                                                     1)]
    fill_up_table(ArmorModel, armors)
    fill_up_table(WeaponModel, weapons)
    fill_up_table(UnitClassModel, classes)
    fill_up_table(PositivePhraseModel, positive_phrases)
    fill_up_table(NegativePhraseModel, negative_phrases)
    fill_up_table(SkillModel, skills)

    db.session.commit()
    db.session.close()


def fill_up_table(model: db.Model, data: list[dict]):

    for item in data:
        created = model(**item)

        db.session.add(created)


if __name__ == '__main__':
    with app.app_context():
        create_database()

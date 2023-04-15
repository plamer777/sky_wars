"""This file contains functions to create a new database and add data to it"""
from services.auth_service import AuthService
from utils import load_from_json
from init_app import app
from db.db_setup import db
from db.models import PositivePhraseModel, NegativePhraseModel, ArmorModel, \
    WeaponModel, SkillModel, UnitClassModel
from constants import EQUIPMENT_FILE, LOGS_FILE, CLASSES_FILE, SKILLS_FILE, \
    ADMIN_FILE


# -------------------------------------------------------------------------


def create_database() -> None:
    """This function serves to create and fill up the database"""
    db.drop_all()
    db.create_all()
    equipment = load_from_json(EQUIPMENT_FILE)
    classes = load_from_json(CLASSES_FILE)
    phrases = load_from_json(LOGS_FILE)
    skills = load_from_json(SKILLS_FILE)
    admin_data = load_from_json(ADMIN_FILE)

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
    AuthService().register_user(admin_data)

    db.session.commit()
    db.session.close()


def fill_up_table(model: db.Model, data: list[dict]) -> None:
    """This function fills up the certain table by provided model and data
    :param model: One of the SQLAlchemy models
    :param data: A list of dictionaries containing data to create models
    """
    for item in data:
        created = model(**item)

        db.session.add(created)


if __name__ == '__main__':
    with app.app_context():
        create_database()

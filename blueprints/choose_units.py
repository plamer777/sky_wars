"""This unit contains a views to serve '/choose-hero/' and '/choose-enemy/
routes"""
from typing import Dict, Union
from flask import Blueprint, render_template, request, redirect, url_for, \
    abort
from werkzeug.wrappers.response import Response
from marshmallow import ValidationError
from marshmallow_dataclass import class_schema
from classes.unit import UserUnit, EnemyUnit
from classes.user_requests import UserRequest
from container import user_heroes, users_arenas
from classes.arena import Arena
from factories.hero_factory import HeroFactory
# ------------------------------------------------------------------------
units_blueprint = Blueprint('units_blueprint', __name__)
options = {}
# ------------------------------------------------------------------------


def get_requested_unit(unit_request: Dict[str, str],
                       unit_type: str) -> Union[UserUnit, EnemyUnit]:
    """This function serves to crate a user's and computer's unit

    :param unit_request: a dictionary containing data to create a unit
    :param unit_type: a string representing the type of unit 'hero' or 'enemy'

    :return - an instance of UserUnit or EnemyUnit class
    """
    RequestSchema = class_schema(UserRequest)
    try:
        unit_chosen = RequestSchema().load(unit_request)
        if unit_type == 'enemy':
            prepared_unit = HeroFactory().create_enemy(unit_chosen)
        elif unit_type == 'hero':
            prepared_unit = HeroFactory().create_hero(unit_chosen)
        else:
            raise ValidationError('Unknown hero type')

        return prepared_unit  # type: ignore

    except ValidationError as e:
        abort(400, f'Invalid request, there is an error {e}')


@units_blueprint.route('/choose-hero/')
def choose_hero() -> str:
    """This view serves to display a page to chose desirable unit for user's
    player

    :return: a string containing html content
    """
    user_host = request.host
    options.update(HeroFactory().get_full_info())
    users_arenas.setdefault(user_host, Arena()).clean()

    options['header'] = 'Героя'
    options['route'] = '/choose-hero/'

    return render_template('hero_choosing.html', result=options)


@units_blueprint.route('/choose-hero/', methods=['POST'])
def hero_chosen_page() -> str:
    """This view serves to display a page to chose desirable unit for
    computer's player

    :return: a string containing html content
    """
    hero_request = request.form
    user_host = request.host
    user_heroes.setdefault(user_host, {}).setdefault('player')
    user_heroes[user_host]['player'] = get_requested_unit(
        hero_request, 'hero')  # type: ignore

    options['header'] = 'Противника'
    options['route'] = '/choose-enemy/'
    options['classes'].remove(hero_request.get('unit_class'))  # type: ignore
    options['weapons'].remove(hero_request.get('weapon'))  # type: ignore
    options['armors'].remove(hero_request.get('armor'))  # type: ignore

    return render_template('hero_choosing.html', result=options)


@units_blueprint.route('/choose-enemy/', methods=['POST'])
def enemy_chosen_page() -> Response:
    """This view allows to create a computer's unit and prepare an arena for
    the game

    :return: a string containing html content
    """
    enemy_request = request.form
    user_host = request.host
    user_heroes.setdefault(user_host, {}).setdefault('enemy', {})
    user_heroes[user_host]['enemy'] = get_requested_unit(
        enemy_request, 'enemy')  # type: ignore

    if isinstance(user_heroes[user_host]['player'], UserUnit) and \
            isinstance(user_heroes[user_host]['enemy'], EnemyUnit):

        users_arenas[user_host].start_game(**user_heroes[user_host])

    else:
        abort(400, 'Не удалось загрузить арену')

    return redirect(url_for('main_blueprint.fight_page', act_request='start'))

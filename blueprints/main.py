"""This unit contains a views to serve '/' and '/fight/ routes"""
from typing import Dict, Any
from flask import Blueprint, render_template, request
from marshmallow_dataclass import class_schema
from classes.user_requests import UserRequest
from container import users_arenas, user_heroes
from utils import clean_objects
# ------------------------------------------------------------------------
main_blueprint = Blueprint('main_blueprint', __name__)
RequestSchema = class_schema(UserRequest)
# ------------------------------------------------------------------------


@main_blueprint.route('/')
def main_page() -> str:
    """This function represents a main page of the game

    :return a string containing html content
    """
    clean_objects(users_arenas, user_heroes)
    return render_template('index.html')


@main_blueprint.route('/fight/<act_request>')
def fight_page(act_request: str) -> str:
    """This function represents a view to show an arena

    :param act_request: the string representing user's action

    :return a string containing html content
    """
    user_host = request.remote_addr

    user_action: Dict[str, Any] = {
        'hit': users_arenas[user_host].hit_rival,
        'use-skill': users_arenas[user_host].use_skill,
        'pass-turn': users_arenas[user_host].next_step,
        'end-fight': users_arenas[user_host].finish_game
    }
    current_action = user_action.get(act_request)

    if current_action:
        result = current_action()

    else:
        result = {'result': '', 'battle_result': ''}

    return render_template('fight.html', heroes=user_heroes[user_host],
                           result=result)

"""This unit contains a views to serve '/' and '/fight/ routes"""
from flask import Blueprint, render_template
from marshmallow_dataclass import class_schema
from classes.user_requests import UserRequest
from container import user_action, heroes
# ------------------------------------------------------------------------
main_blueprint = Blueprint('main_blueprint', __name__)
RequestSchema = class_schema(UserRequest)
# ------------------------------------------------------------------------


@main_blueprint.route('/')
def main_page() -> str:
    """This function represents a main page of the game

    :return a string containing html content
    """
    return render_template('index.html')


@main_blueprint.route('/fight/<act_request>')
def fight_page(act_request: str) -> str:
    """This function represents a view to show an arena

    :param act_request: the string representing user's action

    :return a string containing html content
    """
    current_action = user_action.get(act_request)

    if current_action:
        result = current_action()

    else:
        result = {'result': '', 'battle_result': ''}

    return render_template('fight (copy).html', heroes=heroes, result=result)

"""This unit contains views to log in and register new users"""
import os
from typing import Union
from flask import Blueprint, request, render_template, redirect, abort
from werkzeug import Response
from db.models import UserSchema
from container import auth_service
from constants import AUTH_LOGS
# -----------------------------------------------------------------------
auth_blueprint = Blueprint('auth_blueprint', __name__)
# -----------------------------------------------------------------------


class LoginView:
    """LoginView class is a view for login process"""
    @staticmethod
    @auth_blueprint.route('/login/')
    def login_page() -> str:
        """This view serves to display the login page
        :return: An html template
        """
        return render_template('login.html')

    @staticmethod
    @auth_blueprint.route('/login/', methods=['POST'])
    def validate_login() -> Union[str, Response]:
        """This view serves to get email and password from user and either
        display options page or login page again if data is invalid
        :return: An html template or Response object
        """
        user_data = request.form
        result = auth_service.validate_user(user_data)

        if type(result) is dict:
            os.environ['AUTH_TOKEN'] = result['auth_token']
            return redirect('/options/')

        return render_template('login.html', error=result)


class RegisterView:
    """RegisterView class is a view for register process. As for now only
    user with admin role can register another users"""
    @staticmethod
    @auth_blueprint.route('/register/')
    def register_page() -> str:
        """This view serves to display the register page
        :return: An html template
        """
        return render_template('register.html')

    @staticmethod
    @auth_blueprint.route('/register/', methods=['POST'])
    def validate_register() -> str:
        """This view serves to get register data from user and either
        to add user to database or display message if data is invalid
        :return: An html template
        """
        user_data = request.json if request.json else {}
        if user_data.get('role') == 'admin' and not auth_service.is_admin():
            abort(403, 'Access denied')

        result = auth_service.register_user(user_data)

        if isinstance(result, UserSchema):
            message = AUTH_LOGS['reg_success']['message']
            link = AUTH_LOGS['reg_success']['login']
            return render_template('register.html', log=message, link=link)

        return render_template('register.html', log=result)

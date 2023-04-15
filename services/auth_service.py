"""There is an AuthService class in the file serving to register new users
and validate credentials of the existing ones"""
import logging
import os
import functools
from typing import Optional, Union
from hmac import compare_digest
from flask import abort
from pydantic import ValidationError
from db.models import UserSchema, UserAuthSchema
from dao.auth_dao import UserDao
from managers.hash_manager import HashManager
# ----------------------------------------------------------------------

logging.basicConfig(filename='data/logs.txt')


class AuthService:
    """
    Service class for authentication-related tasks.
    """
    def __init__(self) -> None:
        """
        Initializes the class with the necessary dependencies.
        """
        self._schema = UserSchema
        self._user_dao = UserDao()
        self._auth_schema = UserAuthSchema
        self._hash_manager = HashManager()

    def register_user(self, user_data: dict) -> Optional[UserSchema | str]:
        """
        Registers a new user.

        :param user_data: A dictionary containing user data.
        :return: The result of adding the new user to the database.
        """
        try:
            new_user = self._schema(**user_data)
            if self._user_dao.get_user_by_email(new_user.email):
                return 'The user already exists'
            new_user.password = self._hash_manager.encode_password(
                new_user.password)

        except ValidationError as e:
            print(f'Invalid user data, error: {e}')
            return f'Invalid user data, error: {e}'

        result = self._user_dao.add_new_user(new_user)

        if result:
            return new_user

        return 'Failed to add user'

    def validate_user(self, user_data: dict) -> Union[dict[str, str], str]:
        """This method validates existing user's and provides a couple of
        tokens with email and password

        :param user_data: A dictionary containing user data
        :return: a dictionary containing access and refresh tokens or an error
        message instead
        """
        try:
            validated_data = self._auth_schema(**user_data)
        except ValidationError as e:
            print(f'Data validation failed, error: {e}')
            return f'Login failed, error: {e}'

        found_user = self._user_dao.get_user_by_email(validated_data.email)
        logging.info(f'Найден пользователь - {found_user}')
        logging.info(f'Почта: {found_user.email}, {validated_data.email}')
        if found_user and self._is_pass_valid(validated_data.password,
                                              found_user.password):
            return self._hash_manager.create_token(
                {'email': found_user.email,
                 'password': str(found_user.password)})

        return 'Invalid email or password'

    def check_rules(self, func):
        """
        A decorator function to check the authorization rules for an endpoint.

        :param func: The function to be decorated.
        :return: The wrapper function that performs the authorization check.
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            The wrapper function that performs the authorization check.
            """
            received_token = os.getenv('AUTH_TOKEN')
            user_data = self._hash_manager.decode_token(received_token)

            try:
                validated_data = self._auth_schema(**user_data)
                found_user = self._user_dao.get_user_by_email(
                    validated_data.email)
                if not found_user or found_user.role != 'admin':
                    abort(403, 'Access denied')

            except ValidationError:
                abort(400, 'Invalid Authorization Data')

            return func(*args, **kwargs)

        return wrapper

    def is_admin(self) -> bool:
        """This method serves to check user's permission

        :return: boolean indicating if the user is an administrator
        """
        token = os.getenv('AUTH_TOKEN')
        data = self._hash_manager.decode_token(token)

        if data and data.get('role') == 'admin':
            return True

        return False

    def _is_pass_valid(self, password: str, valid_password: str) -> bool:
        """This method checks if provided password is valid

        :param password: the password to check
        :param valid_password: the valid password to compare against
        :return: True if the password is valid or False otherwise
        """
        hashed_pass = self._hash_manager.encode_password(password)
        logging.info(
            f'Пароли: {hashed_pass}, {valid_password}')

        return compare_digest(hashed_pass, valid_password.encode('utf-8'))

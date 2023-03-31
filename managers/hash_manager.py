"""There is a HashManager class in the file that provides interface to
encode passwords and to create/decode tokens"""
from flask import current_app
import jwt
from datetime import datetime, timedelta
from calendar import timegm
from hashlib import pbkdf2_hmac
from base64 import b64encode
# ----------------------------------------------------------------------


class HashManager:
    """HashManager class provides a mechanism to create/decode tokens and
    encode passwords"""
    @staticmethod
    def _prepare_token(token: str) -> str:
        """
        Prepares a received token for decoding.
        :param token: The received token.
        :return: The fixed token.
        """
        try:
            if 'Bearer' in token:
                token = token.split('Bearer ')[-1]
            return token

        except Exception as e:
            print(f'Failed to process the token, exception: {e}')
            return ''

    def decode_token(self, token: str) -> dict:
        """
        Decodes a JWT token.
        :param token: The token to be decoded.
        :return: A dictionary containing the decoded token data.
        """
        algo, secret, _ = self._get_token_params()
        try:
            token = self._prepare_token(token)
            result = jwt.decode(token, key=secret, algorithms=[algo])

        except jwt.DecodeError:
            print('Decoding token failed')
            return {}

        return result

    def create_token(self, user_data: dict) -> dict[str, str]:
        """This method will create a couple of tokens by provided user data
        :param user_data: A dictionary containing user data
        :return: A dictionary containing the created tokens
        """
        algo, secret, auth_exp_time = self._get_token_params()
        user_data['exp'] = timegm(auth_exp_time.timetuple())

        auth_token = jwt.encode(user_data, key=secret, algorithm=algo)

        _, _, refresh_exp_time = self._get_token_params('day', 120)
        user_data['exp'] = timegm(refresh_exp_time.timetuple())

        refresh_token = jwt.encode(user_data, key=secret, algorithm=algo)

        return {'auth_token': auth_token, 'refresh_token': refresh_token}

    @staticmethod
    def _get_token_params(period: str = 'min', exp_time: int = 30) -> tuple:
        """This is an additional method that helps to create tokens by
        preparing data such as algorithm and expiration time

        :param period: The period of time (min or day)
        :param exp_time: The period of time the token will expire after
        :return: A tuple containing the algorithm, expiration time and secret
        """
        algo = current_app.config.get('JWT_ALGO')
        secret = current_app.config.get('JWT_SECRET')

        if period == 'min':
            auth_exp_time = datetime.now() + timedelta(minutes=exp_time)
        else:
            auth_exp_time = datetime.now() + timedelta(days=exp_time)

        return algo, secret, auth_exp_time

    def encode_password(self, password: str) -> bytes:
        """This method serves to encode provided password

        :param password: the password to encode
        :return: the bytes representing encoded password
        """
        salt, algo, iters = self._get_pass_hash_params()

        hashed_pass = pbkdf2_hmac(algo, password.encode(), salt, iters)

        return b64encode(hashed_pass)

    @staticmethod
    def _get_pass_hash_params() -> tuple:
        """This method returns the parameters to hash passwords

        :return: a tuple containing the salt, algorithm and iterations
        """
        salt = current_app.config['HASH_SALT']
        algo = current_app.config['HASH_ALGO']
        iterations = current_app.config['HASH_ITERATIONS']

        return salt, algo, iterations

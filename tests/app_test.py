"""This unit contains TestApplication class to test the Flask app"""
from typing import Any, List
from flask.testing import FlaskClient
from tests.utils import check_response
# -------------------------------------------------------------------------


class TestApplication:
    """The TestApplication class provides all the functionality for testing
    Flask application"""
    def test_main_route(self, app_client: FlaskClient) -> None:
        """This method tests the main route

        :param app_client: test application client
        """
        response = app_client.get('/')
        result = response.data.decode('utf-8')

        check_response(response)
        assert 'Начать игру' in result, 'Неверные данные на главной странице'

    def test_chose_hero(self, app_client: FlaskClient) -> None:
        """This method tests the /choose-hero/ route

        :param app_client: test application client
        """
        response = app_client.get('/choose-hero/')
        result = response.data.decode('utf-8')

        check_response(response)
        assert 'Выбрать Героя' in result, 'Загружена неверная страница'

    def test_hero_chosen_page(self, app_client: FlaskClient,
                              random_request: dict[str, Any]) -> None:
        """This method tests a POST request to the /choose-hero/ route

        :param app_client: test application client
        :param random_request: a dictionary emulating user's request
        """
        data = random_request
        response = app_client.post('/choose-hero/', data=data)
        result = response.data.decode('utf-8')

        check_response(response)
        assert 'Выбрать Противника' in result, 'Загружена неверная страница'

    def test_enemy_chosen_page(self, app_client: FlaskClient,
                               random_request: dict[str, Any]) -> None:
        """This method tests the /choose-enemy/ route

        :param app_client: test application client
        :param random_request: a dictionary emulating user's request
        """

        data = random_request
        response = app_client.post('/choose-enemy/', data=data,
                                   follow_redirects=True)
        result = response.data.decode('utf-8')

        check_response(response)
        assert 'Нанести удар' in result, 'Загружена неверная страница'

    def test_fight_page(self, app_client: FlaskClient,
                        random_request: dict[str, Any],
                        actions: List[str]) -> None:
        """This method tests the /fight/ route

        :param app_client: test application client
        :param random_request: a dictionary emulating user's request
        :param actions: a list of possible actions
        """
        data = random_request
        app_client.post('/choose-hero/', data=data,
                        follow_redirects=True)
        app_client.post('/choose-enemy/', data=data,
                        follow_redirects=True)
        for action in actions:
            response = app_client.get(f'/fight/{action}')
            result = response.data.decode('utf-8')

            check_response(response)
            assert data.get('unit_class') in result, \
                'Загружена неверная страница'

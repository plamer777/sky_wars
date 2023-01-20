"""This file provides additional functions for testing purposes"""
from typing import Any
from werkzeug.test import TestResponse
# ------------------------------------------------------------------------


def check_class_types(instances: list[Any], parent_class: Any) -> None:
    """This closed method serves to check if provided data is valid

    :param instances: a list of class instances
    :param parent_class: A class to check if instances was created by the
    class
    """

    assert type(instances) is list, 'Неверный тип данных'
    assert len(instances) > 0, 'Список пуст'

    for item in instances:
        assert isinstance(item, parent_class)


def check_class_names(names: list[str]) -> None:
    """This closed method serves to check if provided data is valid

    :param names: a list of available class names
    """
    assert type(names) is list, 'Неверный тип данных'
    assert len(names) > 0, 'Список пуст'
    for name in names:
        assert type(name) is str, 'Неверный тип данных внутри списка'


def check_response(response: TestResponse) -> None:
    """This closed method serves to check provided response

    :param response: an instance of TestResponse
    """
    assert response.status_code == 200, 'ответ сервера не ОК'
    assert 'text/html' in response.content_type, 'Загружается не html'

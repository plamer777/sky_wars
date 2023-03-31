"""This file contains utility functions to load and prepare necessary data"""
import json
from datetime import datetime
from classes.arena import Arena
# --------------------------------------------------------------------------


def load_from_json(filename: str) -> list | dict:
    """This function loads data from a json file

    :param filename: relative path to json file including filename

    :return: uploaded data such as dictionary of list or None if there will be
    an error during loading
    """
    try:
        with open(filename, encoding='utf-8') as fin:
            return json.load(fin)
    except FileNotFoundError:
        print("File not found")
        return []
    except json.JSONDecodeError:
        print("File is not valid json")
        return []


def clean_objects(user_arenas: dict[str, Arena], heroes: dict[str, dict]) -> \
        None:
    """This function serves to clean dictionaries with user arenas and heroes
    if there weren't any actions during 30 minutes from certain user
    :param user_arenas: A dictionary with all arenas
    :param heroes: A dictionary with all heroes
    """
    for host, arena in user_arenas.items():

        timeout = datetime.now() - arena.created_at
        if timeout.seconds // 60 > 30:
            user_arenas.pop(host)
            heroes.pop(host)

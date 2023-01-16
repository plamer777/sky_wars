"""This file contains utility functions to load and prepare necessary data"""
import json
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

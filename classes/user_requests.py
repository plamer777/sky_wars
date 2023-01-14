"""This unit contains a classes to work with user's requests to create game
units"""
from dataclasses import dataclass
# -------------------------------------------------------------------------


@dataclass
class UserRequest:
    """This class represents a user's request"""
    name: str
    unit_class: str
    weapon: str
    armor: str

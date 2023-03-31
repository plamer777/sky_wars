"""This file contains instances and dictionaries required for the game
process"""
from typing import Dict, Any
from services.auth_service import AuthService
# ------------------------------------------------------------------------

user_heroes: Dict[str, Any] = {}

users_arenas: Dict[str, Any] = {}

auth_service = AuthService()

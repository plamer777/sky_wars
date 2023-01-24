"""This file contains instances and dictionaries required for the game
process"""
from typing import Dict, Any
from factories.hero_factory import HeroFactory
from classes.arena import Arena
# ------------------------------------------------------------------------
hero_factory = HeroFactory()
arena = Arena()

heroes: Dict[str, Any] = {
    'player': None,
    'enemy': None
}

user_action: Dict[str, Any] = {
    'hit': arena.hit_rival,
    'use-skill': arena.use_skill,
    'pass-turn': arena.next_step,
    'end-fight': arena.finish_game
}

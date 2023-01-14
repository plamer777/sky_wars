from factories.hero_factory import HeroFactory
from classes.arena import Arena
# ------------------------------------------------------------------------
hero_factory = HeroFactory()
arena = Arena()
heroes = {
    'player': None,
    'enemy': None
}

user_action = {
    'hit': arena.hit_rival,
    'use-skill': arena.use_skill,
    'pass-turn': arena.next_step,
    'end-fight': arena.finish_game
}

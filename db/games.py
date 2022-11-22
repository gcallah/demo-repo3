"""
This module encapsulates details about games.
"""
import db.db_connect as dbc

TEST_GAME_NAME = 'Test game'
NAME = 'name'
NUM_PLAYERS = 'num_players'
LEVEL = 'level'
VIOLENCE = 'violence'

# We expect the game database to change frequently:
# For now, we will consider NUM_PLAYERS and LEVEL to be
# our mandatory fields.
REQUIRED_FLDS = [NUM_PLAYERS, LEVEL, VIOLENCE]
games = {TEST_GAME_NAME: {NUM_PLAYERS: 7, LEVEL: 10, VIOLENCE: 2},
         'game2': {NUM_PLAYERS: 9, LEVEL: 9, VIOLENCE: 2},
         'game3': {NUM_PLAYERS: 6, LEVEL: 1, VIOLENCE: 2}, }

GAME_KEY = 'name'
GAMES_COLLECT = 'games'


def get_game_details(game):
    dbc.connect_db()
    return dbc.fetch_one(GAMES_COLLECT, {GAME_KEY: game})


def game_exists(name):
    """
    Returns whether or not a game exists.
    """
    return get_game_details(name) is not None


def get_games_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(GAME_KEY, GAMES_COLLECT)


def get_games():
    dbc.connect_db()
    return dbc.fetch_all(GAMES_COLLECT)


def add_game(name, details):
    doc = details
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    dbc.connect_db()
    doc[GAME_KEY] = name
    return dbc.insert_one(GAMES_COLLECT, doc)


def del_game(name):
    return dbc.del_one(GAMES_COLLECT, {GAME_KEY: name})


def main():
    print('Getting games as a list:')
    games = get_games()
    print(f'{games=}')
    print('Getting games as a dict:')
    games = get_games_dict()
    print(f'{games=}')
    print(f'{get_game_details(TEST_GAME_NAME)=}')


if __name__ == '__main__':
    main()

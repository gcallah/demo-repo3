"""
This module encapsulates details about games.
"""

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


def game_exists(name):
    """
    Returns whether or not a game exists.
    """
    return name in games


def get_games():
    return list(games.keys())


def get_game_details(game):
    return games.get(game, None)


def add_game(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    games[name] = details


def main():
    games = get_games()
    print(f'{games=}')
    print(f'{get_game_details(TEST_GAME_NAME)=}')


if __name__ == '__main__':
    main()

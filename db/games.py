
"""
This module encapsulates details about games.
"""

TEST_GAME_NAME = 'Test game'
NUM_PLAYERS = 'num_players'

# We expect the game database to change frequently:
games = {TEST_GAME_NAME: {NUM_PLAYERS: 7, 'level': 10},
         'game2': {NUM_PLAYERS: 9, 'level': 9},
         'game3': {NUM_PLAYERS: 6, 'level': 1}, }


def get_games():
    return list(games.keys())


def get_game_details(game):
    return games.get(game, None)


def main():
    games = get_games()
    print(f'{games=}')
    print(f'{get_game_details(TEST_GAME_NAME)=}')


if __name__ == '__main__':
    main()

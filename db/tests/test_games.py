import os

import pytest

import db.games as gm


RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)

TEST_DEL_NAME = 'Game to be deleted'


def create_game_details():
    details = {}
    for field in gm.REQUIRED_FLDS:
        details[field] = 2
    return details


@pytest.fixture(scope='function')
def temp_game():
    gm.add_game(gm.TEST_GAME_NAME, create_game_details())
    yield
    gm.del_game(gm.TEST_GAME_NAME)


@pytest.fixture(scope='function')
def new_game():
    return gm.add_game(TEST_DEL_NAME, create_game_details())


def test_del_game(new_game):
    gm.del_game(TEST_DEL_NAME)
    assert not gm.game_exists(TEST_DEL_NAME)


def test_get_games(temp_game):
    gms = gm.get_games()
    assert isinstance(gms, list)
    assert len(gms) > 0


def test_get_games_dict(temp_game):
    gms = gm.get_games_dict()
    assert isinstance(gms, dict)
    assert len(gms) > 0


def test_get_game_details(temp_game):
    gm_dtls = gm.get_game_details(gm.TEST_GAME_NAME)
    assert isinstance(gm_dtls, dict)


def test_game_exists(temp_game):
    assert gm.game_exists(gm.TEST_GAME_NAME)


def test_game_not_exists():
    assert not gm.game_exists('Surely this is not a game name!')


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        gm.add_game(7, {})


def test_add_wrong_details_type():
        with pytest.raises(TypeError):
            gm.add_game('a new game', [])


def test_add_missing_field():
    with pytest.raises(ValueError):
        gm.add_game('a new game', {'foo': 'bar'})


def test_add_game():
    gm.add_game(gm.TEST_GAME_NAME, create_game_details())
    assert gm.game_exists(gm.TEST_GAME_NAME)
    gm.del_game(gm.TEST_GAME_NAME)

from http import HTTPStatus

from unittest.mock import patch
import pytest
import werkzeug.exceptions as wz

import db.users as usr
import db.games as gm

import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()

TEST_CHAR_TYPE = 'Warrior'
TEST_BAD_CHAR_TYPE = 'Wimp'


def test_hello():
    """
    See if Hello works.
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)


SAMPLE_USER_NM = 'SampleUser'
SAMPLE_USER = {
    usr.NAME: SAMPLE_USER_NM,
    usr.EMAIL: 'x@y.com',
    usr.FULL_NAME: 'Sample User',
}


SAMPLE_GAME_NM = "TestGame"
SAMPLE_GAME_DETAILS = {
  gm.NAME: "TestGame",
  "num_players": 7,
  gm.LEVEL: 10,
  "violence": 2
}


@pytest.fixture(scope='function')
def a_game():
    ret = gm.add_game(SAMPLE_GAME_NM, SAMPLE_GAME_DETAILS)
    yield ret
    gm.del_game(SAMPLE_GAME_NM)


@patch('db.games.get_game_details', return_value=SAMPLE_GAME_DETAILS)
def test_get_game_details(mock_get_game_details):
    resp = TEST_CLIENT.get(f'{ep.GAME_DETAILS_W_NS}/{SAMPLE_GAME_NM}')
    assert resp.status_code == HTTPStatus.OK
    assert isinstance(resp.json, dict)
    # every game must have a name:
    assert gm.NAME in resp.json[ep.GAME_DETAILS_STR]


@patch('db.games.get_game_details', return_value=None)
def test_get_game_details_no_such_game(mock_get_game_details):
    resp = TEST_CLIENT.get(f'{ep.GAME_DETAILS_W_NS}/NotAGameName')
    assert resp.status_code == HTTPStatus.NOT_FOUND


def test_add_user():
    """
    Test adding a user.
    """
    resp = TEST_CLIENT.post(ep.USER_ADD, json=SAMPLE_USER)
    assert usr.user_exists(SAMPLE_USER_NM)
    usr.del_user(SAMPLE_USER_NM)


def test_get_user_list():
    """
    See if we can get a user list properly.
    Return should look like:
        {USER_LIST_NM: [list of users types...]}
    """
    resp = TEST_CLIENT.get(ep.USER_LIST_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json[ep.USER_LIST_NM], list)


def test_get_character_type_list():
    """
    See if we can get a charcter type list properly.
    Return should look like:
        {CHAR_TYPE_LIST_NM: [list of chars types...]}
    """
    resp_json = TEST_CLIENT.get(ep.CHAR_TYPE_LIST_W_NS).get_json()
    assert isinstance(resp_json[ep.CHAR_TYPE_LIST_NM], list)


def test_get_character_type_list_not_empty():
    """
    See if we can get a charcter type list properly.
    Return should look like:
        {CHAR_TYPE_LIST_NM: [list of chars types...]}
    """
    resp_json = TEST_CLIENT.get(ep.CHAR_TYPE_LIST_W_NS).get_json()
    assert len(resp_json[ep.CHAR_TYPE_LIST_NM]) > 0


def test_get_character_type_details():
    """
    """
    resp_json = TEST_CLIENT.get(f'{ep.CHAR_TYPE_DETAILS_W_NS}/{TEST_CHAR_TYPE}').get_json()
    assert TEST_CHAR_TYPE in resp_json
    assert isinstance(resp_json[TEST_CHAR_TYPE], dict)


def test_get_missing_character_type_details():
    """
    """
    resp = TEST_CLIENT.get(f'{ep.CHAR_TYPE_DETAILS_W_NS}/{TEST_BAD_CHAR_TYPE}')
    assert resp.status_code == HTTPStatus.NOT_FOUND

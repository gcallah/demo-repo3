import os

import pymongo as pm

import pytest

import db.db_connect as dbc

RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)

TEST_DB = dbc.GAME_DB
TEST_COLLECT = 'test_collect'
# can be used for field and value:
TEST_NAME = 'test'


@pytest.fixture(scope='function')
def temp_rec():
    if not RUNNING_ON_CICD_SERVER:
        dbc.connect_db()
        dbc.client[TEST_DB][TEST_COLLECT].insert_one({TEST_NAME: TEST_NAME})
        # yield to our test function
        yield
        dbc.client[TEST_DB][TEST_COLLECT].delete_one({TEST_NAME: TEST_NAME})
    else:
        yield
        return True

def test_fetch_one(temp_rec):
    if not RUNNING_ON_CICD_SERVER:
        ret = dbc.fetch_one(TEST_COLLECT, {TEST_NAME: TEST_NAME})
        assert ret is not None


def test_fetch_one_not_there(temp_rec):
    if not RUNNING_ON_CICD_SERVER:
        ret = dbc.fetch_one(TEST_COLLECT, {TEST_NAME: 'not a field value in db!'})
        assert ret is None

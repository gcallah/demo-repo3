"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus

from flask import Flask, request
from flask_restx import Resource, Api, fields
import werkzeug.exceptions as wz

import db.char_types as ctyp
import db.games as gm

app = Flask(__name__)
api = Api(app)

LIST = 'list'
DETAILS = 'details'
ADD = 'add'
MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'
HELLO = '/hello'
MESSAGE = 'message'
CHAR_TYPES_NS = 'character_types'
CHAR_TYPE_LIST = f'/{CHAR_TYPES_NS}/{LIST}'
CHAR_TYPE_LIST_NM = '{CHAR_TYPES_NS}_list'
CHAR_TYPE_DETAILS = f'/{CHAR_TYPES_NS}/{DETAILS}'
GAMES_NS = 'games'
GAME_LIST = f'/{GAMES_NS}/{LIST}'
GAME_LIST_NM = '{GAMES_NS}_list'
GAME_DETAILS = f'/{GAMES_NS}/{DETAILS}'
GAME_ADD = f'/{GAMES_NS}/{ADD}'
USERS_NS = 'users'
USER_LIST = f'/{USERS_NS}/{LIST}'
USER_LIST_NM = '{USERS_NS}_list'
USER_DETAILS = f'/{USERS_NS}/{DETAILS}'


@api.route(HELLO)
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {MESSAGE: 'hello world'}


@api.route(MAIN_MENU)
class MainMenu(Resource):
    """
    This will deliver our main menu.
    """
    def get(self):
        """
        Gets the main game menu.
        """
        return {MAIN_MENU_NM: {'the': 'menu'}}


@api.route(CHAR_TYPE_LIST)
class CharacterTypeList(Resource):
    """
    This will get a list of character types.
    """
    def get(self):
        """
        Returns a list of character types.
        """
        return {CHAR_TYPE_LIST_NM: ctyp.get_char_types()}


@api.route(f'{CHAR_TYPE_DETAILS}/<char_type>')
class CharacterTypeDetails(Resource):
    """
    This will return details on a character type.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, char_type):
        """
        This will return details on a character type.
        """
        ct = ctyp.get_char_type_details(char_type)
        if ct is not None:
            return {char_type: ctyp.get_char_type_details(char_type)}
        else:
            raise wz.NotFound(f'{char_type} not found.')


@api.route(GAME_LIST)
class GameList(Resource):
    """
    This will get a list of currrent games.
    """
    def get(self):
        """
        Returns a list of current games.
        """
        return {GAME_LIST_NM: gm.get_games()}


@api.route(f'{GAME_DETAILS}/<game>')
class GameDetails(Resource):
    """
    This will get details on a game.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, game):
        """
        Returns a list of character types.
        """
        ct = gm.get_game_details(game)
        if ct is not None:
            return {game: gm.get_game_details(game)}
        else:
            raise wz.NotFound(f'{game} not found.')


game_fields = api.model('NewGame', {
    gm.NAME: fields.String,
    gm.NUM_PLAYERS: fields.Integer,
    gm.LEVEL: fields.Integer,
    gm.VIOLENCE: fields.Integer,
})


@api.route(GAME_ADD)
class AddGame(Resource):
    """
    Add a game.
    """
    @api.expect(game_fields)
    def post(self):
        """
        Add a game.
        """
        print(f'{request.json=}')
        name = request.json[gm.NAME]
        del request.json[gm.NAME]
        gm.add_game(name, request.json)


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = ''
        # sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}

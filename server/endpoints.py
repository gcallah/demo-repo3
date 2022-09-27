"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask
from flask_restx import Resource, Api
import db.char_types as ctyp

app = Flask(__name__)
api = Api(app)

LIST = 'list'
DETAILS = 'details'
MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'
HELLO = '/hello'
MESSAGE = 'message'
CHAR_TYPE_LIST = f'/character_types/{LIST}'
CHAR_TYPE_LIST_NM = 'character_types_list'
CHAR_TYPE_DETAILS = f'/character_types/{DETAILS}'


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


@api.route(f'{CHAR_TYPE_DETAILS}/<character_type>')
class CharacterTypeDetails(Resource):
    """
    This will get a list of character types.
    """
    def get(self, character_type):
        """
        Returns a list of character types.
        """
        return {character_type: {}}


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

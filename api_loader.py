from flask_restful import Api, Resource

from modules.hello.api import load_api as hello_api
from settings import API_VERSION


class API(Resource):
    def get(self):
        return 'Hello API', 200, {'API-Version': API_VERSION}


def load_api(app):
    Api(app).add_resource(API, '/api')
    hello_api(app)

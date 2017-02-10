from flask_restful import Api, Resource
from flask_restful import reqparse

from errors import APIException


def load_api(app):
    rest = Api(app)
    rest.add_resource(SayHelloAPI, '/api/say-hello')


class SayHelloAPI(Resource):
    def get(self):
        args = reqparse.RequestParser() \
            .add_argument('say', required=True) \
            .parse_args()
        say = args.get('say')
        if say.lower() == 'hello':
            return 'Hello ~', 200
        else:
            raise APIException('You should say hello.')

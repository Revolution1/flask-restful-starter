import logging
import os

from flask import Flask
from flask import send_from_directory

from api_loader import load_api
from settings import SOURCE_ROOT, ENABLE_CORS, setup_logging

log = logging.getLogger(__name__)


def setup_routes(app):
    # @app.route('/')
    # def index():
    #     return send_file(os.path.join(SOURCE_ROOT, 'static', 'index.html'))

    @app.route('/<path:path>')
    def static_files(path):
        return send_from_directory(os.path.join(SOURCE_ROOT, 'static'), path)

    if ENABLE_CORS:
        @app.after_request
        def after_request(response):
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Headers',
                                 'Content-Type,Authorization')
            response.headers.add(
                'Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            return response


def create_app(name=None):
    setup_logging()
    app = Flask(name or 'App')
    app.config.root_path = os.path.dirname(os.path.abspath(__file__))
    app.config.from_pyfile('settings.py')
    load_api(app)
    setup_routes(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', 8000, True, use_reloader=True)

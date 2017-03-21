import logging
import os
import sys

ERROR_404_HELP = False

SECRET_KEY = os.getenv('SECRET_KEY') or 'flask_restful_starter'

SOURCE_ROOT = os.path.abspath(os.path.dirname(__file__))

DATA_DIR = os.path.join(SOURCE_ROOT, 'data')
# if not os.path.exists(DATA_DIR):
#     os.mkdir(DATA_DIR)


def in_data_dir(*path):
    return os.path.join(DATA_DIR, *path)


API_VERSION = '0.1'
ENABLE_CORS = True
PROD = os.getenv('PROD') or False
GUNICORN_WORKERS = os.getenv('GUNICORN_WORKERS')

LOG_LEVEL = logging.INFO if PROD else logging.DEBUG
LOG_FORMAT = '%(asctime)s (%(process)d/%(threadName)s) %(name)s %(levelname)s - %(message)s'

def setup_logging(level=None):
    level = level or LOG_LEVEL
    console_handler = logging.StreamHandler(sys.stderr)
    formatter = logging.Formatter(LOG_FORMAT)
    console_handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.addHandler(console_handler)
    root_logger.setLevel(level)
    # Disable requests logging
    logging.getLogger("requests").propagate = False

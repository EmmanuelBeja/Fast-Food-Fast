# third-party imports
import os
from flask import Flask

# local imports
from config import app_config

def create_app(config_name):
    """ create app """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    from .v1.food import food_api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/v1')

    return app

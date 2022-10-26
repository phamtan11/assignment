from flask import Flask
from app.apiv1 import blueprint, api


def create_app(config_name=None):
    app = Flask(__name__)

    app.register_blueprint(blueprint)

    return app

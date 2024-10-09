from flask import Flask
from .extensions import cors
from .config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    cors.init_app(app, resources={r'/*': {'origins': '*'}})


    from .api.auth.routes import auth

    app.register_blueprint(auth)

    return app
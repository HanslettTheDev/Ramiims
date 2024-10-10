from flask import Flask

from .config import Config
from .extensions import cors


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    cors.init_app(app, resources={r"/*": {"origins": "*"}})

    from .api.auth.routes import auth
    from .api.home.routes import homepage

    app.register_blueprint(auth)
    app.register_blueprint(homepage)

    return app

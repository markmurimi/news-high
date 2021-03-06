from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()


def creating_app(config_name):

    app = Flask(__name__)

    """This creation of the app configurations"""
    app.config.from_object(config_options[config_name])

    """This method is to initialize bootstrap"""
    bootstrap.init_app(app)

    """Setting up the configuration"""
    from .requests import configure_request
    configure_request(app)

    """Function for registering the blueprint"""
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

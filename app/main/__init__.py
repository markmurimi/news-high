from config import config_options 
from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def creation_app(config_name):
    app = Flask(__name__)

    """Creating the configurations to run the app"""

    app.config.from_object(config_options[config_name])
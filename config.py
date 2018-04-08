import os


class Config:
    """This is the config class for the whole app"""
    NEWS_API_KEY = 'a0105d92777949db8ce68f1b4952b724'
    NEWS_API_BASE_URL = 'https://newsapi.org/v1/sources/'

class  DevConfig(Config):
    """This is the configuration class for the development stage of the app"""
    DEBUG = True

class ProdConfig(Config):
    """This is the config class for the app during production stage"""
    pass

config_options = {
        'development':DevConfig,
        'production':ProdConfig
    }

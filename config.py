import os

class  DevConfig(Config):
    """This is the configuration class for the development stage of the app"""
    DEBUG = True

class Config:
    """This is the config class for the whole app"""
    NEWS_API_KEY = 'a0105d92777949db8ce68f1b4952b724'

class ProdConfig(config):
    """This is the config class for the app during production stage"""
    pass

config_options = {
        'development':Devconfig,
        'production':ProdConfig
    }

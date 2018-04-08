import urllib.request
import json
from .models import Sources, Articles

"""this is getting the API KEY"""
api_key = None

"""this is getting the news base url"""
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']



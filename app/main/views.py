from .import main
from flask import render_template, request, redirect
from ..requests import get_sources, get_articles

@main.route('/')
def index():
    """This is the view root function wwhich returns the the index page"""
    title = 'News Highlights websites'
    news_sources = get_sources('sources')
    return render_template('index.html', title=title, sources=news_sources)

@main.route('/articles/<source_id>')
def the_articles(source_id):
    """This is the function that views the source page and returns the required data for the source page"""
    title = f"{source_id} page"
    the_articles = get_articles(source_id)
    return render_template('article.html',articles = the_articles, title = title)
    
#!/usr/bin/env python3
"""
THis file we use for create a simple Flask App
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel()


class Config:
    """
    We use that class for create basic config parameters for our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale():
    """
    We use this function for getting the lang from browser
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def main_page():
    """
    This route is main route, which show us the main page
    """
    return render_template('0-index.html')


babel.init_app(app, locale_selector=get_locale())


if "__main__" == __name__:
    app.run(debug=True)

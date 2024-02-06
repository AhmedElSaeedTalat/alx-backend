#!/usr/bin/env python3

""" run app module """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union
app = Flask(__name__)
babel = Babel(app)

users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }


class Config(object):
    """ class config fot babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ return locale """
    if 'locale' in request.args:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict[str, str], None]:
    """ gets user """
    return users.get(int(request.args['login_as']), 0)


@app.before_request
def before_request():
    """ before request method  """
    g.user = get_user()


@app.route('/')
def hello() -> str:
    """ home page """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()

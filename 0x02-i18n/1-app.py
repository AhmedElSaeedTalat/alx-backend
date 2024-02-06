#!/usr/bin/env python3
""" run app module """
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ class config fot babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
bable = Babel(app)
app.config.from_object(Config)


@app.route('/')
def hello() -> str:
    """ home page """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()

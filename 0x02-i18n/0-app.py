#!/usr/bin/env python3
""" run app module """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    """ home page """
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

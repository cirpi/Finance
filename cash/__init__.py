from tkinter.filedialog import test
from flask import Flask, redirect, url_for
import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    from . import pages
    app.register_blueprint(pages.blueprint)
    # index route
    @app.route('/')
    def index():
        return redirect(url_for('page.news'))
    return app
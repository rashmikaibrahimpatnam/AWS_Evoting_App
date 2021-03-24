import os

from flask import Flask
from flask_material import Material

from . import register, login, voterHome


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = os.urandom(24)
    Material(app)

    app.register_blueprint(register.bp, url_prefix="/register")
    app.register_blueprint(login.bp, url_prefix="/login")
    app.register_blueprint(voterHome.bp, url_prefix="/voterHome")

    return app

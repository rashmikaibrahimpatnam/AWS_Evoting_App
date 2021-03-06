from flask import Flask
from flask_material import Material

from . import register, login


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    Material(app)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    app.register_blueprint(register.bp, url_prefix="/register")
    app.register_blueprint(login.bp, url_prefix="/login")

    return app

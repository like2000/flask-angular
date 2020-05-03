from importlib import import_module

from flask import Flask, redirect, url_for, send_from_directory


def register_blueprint(server: Flask):
    ...


def register_extension(server: Flask):
    module_name = 'home'
    module = import_module(f"flask_angular.{module_name}.routes")
    server.register_blueprint(module.blueprint, url_prefix=f"/{module_name}")


def create_app():
    server = Flask(__name__)

    register_blueprint(server)

    @server.route("/")
    def home():
        # return "Hello World!"
        # return redirect(url_for('home_blueprint.home'))
        return send_from_directory('../frontend/src', 'index.html')

    return server

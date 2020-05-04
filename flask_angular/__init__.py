from importlib import import_module

from flask import Flask, redirect, url_for, send_from_directory, render_template
from flask_cors import CORS


def register_blueprint(server: Flask):
    module_name = 'home'
    module = import_module(f"flask_angular.{module_name}.routes")
    server.register_blueprint(module.blueprint, url_prefix=f"/{module_name}")


def register_extension(server: Flask):
    ...


def create_app():
    server = Flask(
        __name__,
        # static_folder='home/static'
    )
    # CORS(server)

    register_blueprint(server)
    # print(server.blueprints['home_blueprint'])

    # @server.route('/<path:path>', methods=['GET'])
    # def static_proxy(path):
    #     return send_from_directory('./', path)

    @server.route("/")
    def home():
        # return "Hello World!"
        return redirect(url_for('home_blueprint.home'))
        # return send_from_directory('./', 'index.html')

    return server

from flask import render_template

from flask_angular.home import blueprint


@blueprint.route("/")
def home():
    return render_template("index.html")

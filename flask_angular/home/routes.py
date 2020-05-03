from flask_angular.home import blueprint


@blueprint.home("/")
def home():
    return "Hello Kevin!"

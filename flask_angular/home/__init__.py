from flask import Blueprint

name = "home"
blueprint = Blueprint(
    name + "_blueprint",
    import_name=__name__,
    static_folder='static',
    template_folder='templates',
    static_url_path=f'/{name}/static'
)

from flask import Blueprint

adminka = Blueprint('adminka', __name__, template_folder='templates')


@adminka.route('/sadas')
def index():
    return "HEllo admin"
from flask import (
    Blueprint, render_template
)

bp = Blueprint('login', __name__, template_folder="templates", static_folder="static")


@bp.route("/login", methods=['GET'])
def get_login_page():
    return render_template("login.html")


@bp.route("/login", methods=['POST'])
def submit_data():
    return "HI"

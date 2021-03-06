from flask import (
    Blueprint, render_template
)

bp = Blueprint('register', __name__, template_folder="templates", static_folder="static")


@bp.route("/", methods=['GET'])
def get_register_page():
    return render_template("register.html")


@bp.route("/signup", methods=['POST'])
def submit_data():
    return "HI"

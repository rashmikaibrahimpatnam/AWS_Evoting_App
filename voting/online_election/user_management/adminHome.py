from flask import Blueprint, render_template

bp = Blueprint('adminHome', __name__, template_folder="templates", static_folder="static")


@bp.route("/adminHome", methods=["GET"])
def get_admin_home():
    return render_template("admin_home.html")

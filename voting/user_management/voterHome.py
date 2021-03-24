from flask import Blueprint, render_template

bp = Blueprint('voterHome', __name__, template_folder="templates", static_folder="static")


@bp.route("/voterHome", methods=["GET"])
def get_voter_home():
    return render_template("voter_home.html")

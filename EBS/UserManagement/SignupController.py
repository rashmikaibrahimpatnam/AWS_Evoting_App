from flask import render_template, Flask
from flask_material import Material

app = Flask(__name__)
Material(app)


@app.route("/")
def index():
    return render_template("signup.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return "HI"

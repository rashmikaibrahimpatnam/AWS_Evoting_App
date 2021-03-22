import hashlib
import json
import pdb
from collections import namedtuple

import requests
from flask import (
    Blueprint, render_template, request, flash, session
)

from user_management.User import UserDetails

bp = Blueprint('login', __name__, template_folder="templates", static_folder="static")


@bp.route("/login", methods=['GET'])
def get_login_page():
    if 'email' in session:
        return 'Logged in as {}'.format(session['email_id'])
    return render_template("login.html")


def json_decoder(user_dictionary):
    return namedtuple('X', user_dictionary.keys())(*user_dictionary.values())


@bp.route("/login", methods=['POST'])
def submit_data():
    email = str(request.form.get("email", ""))
    password = str(request.form.get("password", ""))
    hashed_pwd = hashlib.sha256(password.encode("utf-8")).hexdigest()
    user = UserDetails(first_name='', last_name='', phone='', email=email, password=hashed_pwd)
    print(email)
    print(hashed_pwd)
    if email == "" or password == "":
        flash("One or more fields are empty!!! Please try again!")
        return render_template("login.html")
    else:
        # fetch data from dynamo for the user, if does not exist, redirect to register page fetch data from dynamo
        # for the user, if exists, check for the verified field, if verified redirect to home page
        session['email_id'] = user.email
        get_user_url = "https://as5r1zw6c8.execute-api.us-east-1.amazonaws.com/test/usermanagement"
        headers = {"Content-type": "application/json"}
        params = {"email_id": user.email}
        response = requests.get(get_user_url, params=params, headers=headers)
        user_details = json.loads(response.text, object_hook=json_decoder)

        validate_details = {
            'email_id': user.email,
            'password': user.password
        }
        validate_user_url = "https://as5r1zw6c8.execute-api.us-east-1.amazonaws.com/test/login"

        if bool(user_details):
            # check for verification code and match the password
            response = requests.post(validate_user_url, json=validate_details)
            return render_template("home.html")
        else:
            flash("The user does not exist. Please register instead!")
            return render_template("register.html")


@bp.route('/logout')
def logout():
    # remove the email from the session if it is present 
    session.pop('email_id', None)
    return render_template("login.html")

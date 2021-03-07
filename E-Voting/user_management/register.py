import json

import requests
from flask import Blueprint, render_template, request, flash

from user_management.User import UserDetails

bp = Blueprint('register', __name__, template_folder="templates", static_folder="static")


@bp.route("/", methods=['GET'])
def get_register_page():
    return render_template("register.html")


@bp.route("/signup", methods=['POST'])
def submit_data():
    first_name = str(request.form.get("first_name", ""))
    last_name = str(request.form.get("last_name", ""))
    password = str(request.form.get("password", ""))
    confirm_password = str(request.form.get("confirm_password", ""))
    phone = str(request.form.get("phone", ""))
    email = str(request.form.get("email", ""))
    user = UserDetails(first_name, last_name, password, phone, email)

    if first_name == "" or last_name == "" or password == "" or phone == "" or email == "":
        flash("One or more fields are empty!!! Please try again!")
        return render_template("register.html")
    if password != confirm_password:
        flash("The passwords are not matching!! Please try again!!")
        return render_template("register.html")
    else:
        # 1. get details from dynamodb for the email id. If exists, throw error
        # 2. If not existing, insert to dynamodb and also encrypt the password
        # 3. Once inserted, send an email with a verification code
        # 4. Render a template which verifies that verification code

        get_user_url = " https://as5r1zw6c8.execute-api.us-east-1.amazonaws.com/test/usermanagement"
        add_user_url = "https://as5r1zw6c8.execute-api.us-east-1.amazonaws.com/test/usermanagement"

        headers = {"Content-type": "application/json"}
        params = {"email_id": user.email}

        add_user_params = {
            "email_id": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "password": user.password,
            "phone": user.phone,
            "verified": user.verified
        }

        response = requests.get(get_user_url, params=params, headers=headers)

        user_details = json.loads(response.text, object_hook=UserDetails.decode)

        if not bool(user_details):
            response = requests.post(add_user_url, json=add_user_params)
            print(response.text)
            return render_template("login.html")
        else:
            flash("The user already exists in the system. Please login instead!")
            return render_template("register.html")
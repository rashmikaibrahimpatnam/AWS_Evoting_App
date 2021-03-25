import json
import pdb
import uuid

import requests
from flask import Blueprint, render_template, request, flash, session

from online_election.Candidate import Candidate
from online_election.Election import Election

bp = Blueprint('adminElection', __name__, template_folder="templates", static_folder="static")


def view_elections():
    if "email_id" not in session:
        return render_template("view_elections.html")


@bp.route("/createElection", methods=["GET"])
def create_election():
    return render_template("create_election.html")


@bp.route("/saveElectionDetails", methods=["POST"])
def submit_data():
    if "email_id" not in session:
        return render_template("create_election.html")

    election_type = str(request.form.get("election_type", ""))
    election_title = str(request.form.get("election_title", ""))
    election_text = str(request.form.get("election_text", ""))
    election_start_date = (request.form.get("start_date", ""))
    election_end_date = (request.form.get("end_date", ""))
    election_candidate_name = request.form.getlist("candidate")
    election_candidate_party = request.form.getlist("candidate_party")

    if election_type == "":
        flash("Election type is required!!")
        return render_template("create_election.html")
    if election_title == "":
        flash("Election title is required!!")
        return render_template("create_election.html")
    if election_text == "":
        flash("Election description is required!!")
        return render_template("create_election.html")
    if election_start_date is None:
        flash("Election start date is required!!")
        return render_template("create_election.html")
    if election_end_date is None:
        flash("Election end date is required!!")
        return render_template("create_election.html")
    if election_candidate_name is None or election_candidate_party is None:
        flash("Two or more candidates must be included in the election in order to cast a vote!")
        return render_template("create_election.html")
    if len(election_candidate_name) <= 1 or len(election_candidate_party) <= 1:
        flash("Two or more candidates must be included in the election in order to cast a vote!")
        return render_template("create_election.html")
    if election_start_date >= election_end_date:
        flash("The start date must be less than the end date!!")
        return render_template("create_election.html")

    candidate_list = []

    for i, j in zip(election_candidate_name, election_candidate_party):
        candidate = Candidate(str(i), str(j))
        candidate_list.append(candidate)

    election_id = str(uuid.uuid4())
    election = Election(election_id, election_type, election_text, election_title, candidate_list,
                        election_start_date, election_end_date)
    print(str(election))

    create_election_url = "https://s9uztjegil.execute-api.us-east-1.amazonaws.com/test/electionmanagement"
    serialized_election = json.dumps(election, default=lambda o: o.__dict__)
    print(serialized_election)
    pdb.set_trace()
    response = requests.post(create_election_url, data=serialized_election)
    print(response.text)
    return "Success"


def delete_election():
    if "email_id" not in session:
        return render_template("delete_election.html")

import json
from collections import namedtuple
from datetime import date

import requests
from flask import Blueprint, session, render_template

from online_election.Election import Election

bp = Blueprint('elections', __name__, template_folder="templates", static_folder="static")


def json_decoder(user_dictionary):
    return namedtuple('X', user_dictionary.keys())(*user_dictionary.values())


@bp.route("/ongoing", methods=["GET"])
def get_ongoing_elections():
    if "email_id" not in session:
        return render_template("create_election.html")
    get_elections_url = "https://s9uztjegil.execute-api.us-east-1.amazonaws.com/test/votingmanagement"
    headers = {"Content-type": "application/json"}
    params = {"email_id": session["email_id"]}

    response = requests.get(get_elections_url, params=params, headers=headers)
    election_list_response = json.loads(response.text, object_hook=json_decoder)

    print(election_list_response.elections)
    submitted_elections = election_list_response.submittedElections

    elections = []
    for election_item in election_list_response.elections:
        election = Election(election_item.election_id, election_item.election_type,
                            election_item.election_text,
                            election_item.election_title,
                            election_item.election_candidates,
                            election_item.start_date, election_item.end_date)
        elections.append(election)

    # filter elections that are already submitted by the user
    if len(election_list_response.submittedElections) > 0:
        elections = [x for x in elections if x.election_id not in submitted_elections]

    # filter out the elections that have not yet started or already over!

    date_formatted = date.today().strftime("%d/%m/%Y")
    elections = [x for x in elections if x.start_date <= date_formatted <= x.end_date]

    return render_template("ongoing_election_list.html", election_list=elections, len=len(elections))


@bp.route("/submitted", methods=["GET"])
def get_submitted_elections():
    if "email_id" not in session:
        return render_template("create_election.html")
    pass


@bp.route('/castVote/<string:election_id>', methods=['GET'])
def get_cast_vote_page(election_id):
    if "email_id" not in session:
        return render_template("create_election.html")
    print(election_id)
    return "Success"

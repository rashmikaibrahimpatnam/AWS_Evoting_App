import json
from collections import namedtuple
from datetime import date

import requests
from flask import Blueprint, session, render_template, request

from online_election.access_secmanager import SecretManager
from online_election.voting_management.Election import Election

bp = Blueprint('elections', __name__, template_folder="templates", static_folder="static")


def json_decoder(user_dictionary):
    return namedtuple('X', user_dictionary.keys())(*user_dictionary.values())

def fetch_secret_key():
    secret_name = "electionmgmt/electionmgmtkey"
    key_name = "ElectionMgmtAPIKey"
    secret = SecretManager().get_secret(secret_name, key_name)
    return secret

@bp.route("/ongoing", methods=["GET"])
def get_ongoing_elections():
    if "email_id" not in session:
        return render_template("ongoing_election_list.html")
    secret = fetch_secret_key()
    get_elections_url = "https://s9uztjegil.execute-api.us-east-1.amazonaws.com/test/votingmanagement"
    headers = {"Content-type": "application/json","x-api-key": secret, "authorizationToken": secret}
    params = {"email_id": session["email_id"]}

    response = requests.get(get_elections_url, params=params, headers=headers)
    if "Unauthorized" in response.text or "Forbidden" in response.text:
        return render_template('error.html')
    election_list_response = json.loads(response.text, object_hook=json_decoder)
    submitted_elections = election_list_response.submittedElections
    elections = []
    for election_item in election_list_response.elections:
        election = Election(election_item.election_id, election_item.election_type,
                            election_item.election_text,
                            election_item.election_title,
                            election_item.election_candidates,
                            election_item.start_date, election_item.end_date,
                            election_item.results_published)
        elections.append(election)

    # filter elections that are already submitted by the user
    if len(submitted_elections) > 0:
        submitted_elections = [x for x in submitted_elections
                               if x.voter_id == session["email_id"]]
        election_id_list = [o.election_id for o in submitted_elections]
        print(election_id_list)
        elections = [y for y in elections if y.election_id not in election_id_list]
        print(submitted_elections)

    # filter out the elections that have not yet started or already over!

    date_formatted = date.today().strftime("%d/%m/%Y")
    elections = [x for x in elections if x.start_date <= date_formatted <= x.end_date]

    return render_template("ongoing_election_list.html", election_list=elections, len=len(elections))


@bp.route("/submitted", methods=["GET"])
def get_submitted_elections():
    if "email_id" not in session:
        return render_template("submitted_election_list.html")
    secret = fetch_secret_key()
    get_elections_url = "https://s9uztjegil.execute-api.us-east-1.amazonaws.com/test/votingmanagement"
    headers = {"Content-type": "application/json","x-api-key": secret, "authorizationToken": secret}
    params = {"email_id": session["email_id"]}

    response = requests.get(get_elections_url, params=params, headers=headers)
    if "Unauthorized" in response.text or "Forbidden" in response.text:
        return render_template('error.html')
    election_list_response = json.loads(response.text, object_hook=json_decoder)
    submitted_elections = election_list_response.submittedElections
    elections = []
    for election_item in election_list_response.elections:
        election = Election(election_item.election_id, election_item.election_type,
                            election_item.election_text,
                            election_item.election_title,
                            election_item.election_candidates,
                            election_item.start_date, election_item.end_date,
                            election_item.results_published)
        elections.append(election)

    # filter elections that are already submitted by the user
    if len(submitted_elections) > 0:
        submitted_elections = [x for x in submitted_elections
                               if x.voter_id == session["email_id"]]
        election_id_list = [o.election_id for o in submitted_elections]
        print(election_id_list)
        elections = [y for y in elections if y.election_id in election_id_list]
        print(submitted_elections)
    else:
        elections = []
    return render_template("submitted_election_list.html", election_list=elections, len=len(elections),
                           submitted_elections=submitted_elections,
                           submitted_len=len(submitted_elections))


@bp.route('/castVote/<string:election_id>', methods=['GET'])
def get_cast_vote_page(election_id):
    if "email_id" not in session:
        return render_template("create_election.html")
    get_election_by_id_url = "https://s9uztjegil.execute-api.us-east-1.amazonaws.com/test/electionmanagement"
    secret = fetch_secret_key()
    headers = {"Content-type": "application/json","x-api-key": secret, "authorizationToken": secret}
    params = {"election_id": election_id}
    response = requests.get(get_election_by_id_url, params=params, headers=headers)
    if "Unauthorized" in response.text or "Forbidden" in response.text:
        return render_template('error.html')
    election_details = json.loads(response.text, object_hook=json_decoder)
    return render_template("cast_election.html", election=election_details,
                           len=len(election_details.election_candidates))


@bp.route("/castVote", methods=["POST"])
def cast_vote():
    if "email_id" not in session:
        return render_template("cast_election.html")
    option = request.form.getlist('candidate_group')
    election_id = request.form.get("election_id", "")
    print(option)
    print(election_id)
    secret = fetch_secret_key()
    cast_your_vote_url = "https://s9uztjegil.execute-api.us-east-1.amazonaws.com/test/votingmanagement"
    cast_vote_params = {
        "email_id": session["email_id"],
        "election_id": election_id,
        "status": "voted",
        "vote_date": date.today().strftime("%d/%m/%Y"),
        "candidate_voted": option[0]
    }
    headers = {"Content-type": "application/json","x-api-key": secret, "authorizationToken": secret}

    response = requests.post(cast_your_vote_url, json=cast_vote_params,headers=headers)
    if "Unauthorized" in response.text or "Forbidden" in response.text:
        return render_template('error.html')
    details = json.loads(response.text)
    session["message"] = "Successfully created the election!"
    # sns mail must be sent
    return render_template("voter_home.html")

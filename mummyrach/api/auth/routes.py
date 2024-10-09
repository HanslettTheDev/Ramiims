from flask import Blueprint, jsonify

auth = Blueprint("auth", __name__)


@auth.route("/test_server_status", methods=["GET"])
def check_user():
    return jsonify("Yeah, Server is running")
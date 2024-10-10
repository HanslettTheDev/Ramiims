from flask import Blueprint, render_template

homepage = Blueprint("homepage", __name__)


@homepage.route("/", methods=["GET", "POST"])
@homepage.route("/home", methods=["POST"])
def home():
    return render_template("home/index.html")

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/", methods=["POST", "GET"])
def home():
    return render_template('index.html')

@views.route("/loen", methods=["POST", "GET"])
def loen():
    return render_template('loen.html')
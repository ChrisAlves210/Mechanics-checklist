from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

main = Blueprint("main", __name__)


@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@main.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    return redirect(url_for("auth.login"))

@main.route("/checklist")
def checklist():
    return render_template("checklist.html")

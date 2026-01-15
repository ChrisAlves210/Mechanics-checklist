from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required

main = Blueprint("main", __name__)


@main.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("main.checklist"))
    return redirect(url_for("auth.login"))

## login is required for access to the checklist ##
@main.route("/checklist")
@login_required
def checklist():
    return render_template("checklist.html")

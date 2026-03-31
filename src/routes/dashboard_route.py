from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder='templates', static_folder='static')


@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")
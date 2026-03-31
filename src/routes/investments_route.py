from flask import Blueprint, render_template

investments_bp = Blueprint('investments_bp', __name__, template_folder='templates', static_folder='static')

@investments_bp.route("/investments", methods=["GET"])
def investments():
    return render_template("investments.html")
from flask import Blueprint, render_template

investments_bp = Blueprint('investments_bp', __name__, template_folder='templates', static_folder='static')

@investments_bp.route("/<user_id>/investments", methods=["GET"])
def investments(user_id: str):
    return render_template("investments.html", user_id=user_id)
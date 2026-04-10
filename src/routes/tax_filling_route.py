from flask import Blueprint, render_template

tax_filling_bp = Blueprint('tax_filling_bp', __name__, template_folder='templates', static_folder='static')

@tax_filling_bp.route("/<user_id>/tax_filling", methods=["GET"])
def tax_filling(user_id: str):
    return render_template("tax_filling.html", user_id=user_id)
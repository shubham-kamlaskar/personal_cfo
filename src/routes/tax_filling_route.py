from flask import Blueprint, render_template

tax_filling_bp = Blueprint('tax_filling_bp', __name__, template_folder='templates', static_folder='static')

@tax_filling_bp.route("/tax_filling", methods=["GET"])
def tax_filling():
    return render_template("tax_filling.html")
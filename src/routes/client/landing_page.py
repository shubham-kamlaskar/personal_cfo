from flask import Blueprint, render_template

landing_page_b2b_bp = Blueprint('landing_page_bp', __name__, template_folder='templates', static_folder='static')

@landing_page_b2b_bp.route("/", methods=['GET'])
def landing_page():
    return render_template("b2b/landing_page.html")
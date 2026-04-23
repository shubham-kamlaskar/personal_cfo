from flask import Blueprint, render_template

landing_page_bp = Blueprint('landing_page_bp', __name__, template_folder='templates', static_folder='static')

@landing_page_bp.route("/", methods=['GET'])
def landing_page():
    return render_template("b2b/landing_page.html")

@landing_page_bp.route("/about", methods=['GET'])
def about():
    return render_template("home/about.html")

@landing_page_bp.route("/careers", methods=['GET'])
def careers():
    return render_template("home/careers.html")

@landing_page_bp.route("/contact", methods=['GET'])
def contact():
    return render_template("home/contact.html")

@landing_page_bp.route("/privacy", methods=['GET'])
def privacy():
    return render_template("home/privacy.html")

@landing_page_bp.route("/terms", methods=['GET'])
def terms():
    return render_template("home/terms.html")
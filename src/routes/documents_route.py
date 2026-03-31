from flask import Blueprint, render_template

documents_bp = Blueprint('documents_bp', __name__, template_folder='templates', static_folder='static')

@documents_bp.route("/documents", methods=["GET"])
def documents():
    return render_template("documents.html")
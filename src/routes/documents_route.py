from flask import Blueprint, render_template

documents_bp = Blueprint('documents_bp', __name__, template_folder='templates', static_folder='static')

@documents_bp.route("/<user_id>/documents", methods=["GET"])
def documents(user_id: str):
    return render_template("documents.html", user_id=user_id)
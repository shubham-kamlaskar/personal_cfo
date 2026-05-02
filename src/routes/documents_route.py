from flask import Blueprint, render_template
import logging

from src.util.access_provider import login_required

logger = logging.getLogger(__name__)

documents_bp = Blueprint('documents_bp', __name__, template_folder='templates', static_folder='static')

@documents_bp.route("/<client_id>/<employee_id>/documents", methods=["GET"])
@login_required
def documents(client_id: str, employee_id: str):
    try:
        return render_template("employee/documents.html", client_id=client_id, employee_id=employee_id)
    except Exception as e:
        logger.error(f"An error occured in documents route: {str(e)}")
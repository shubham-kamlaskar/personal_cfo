import os
from dotenv import load_dotenv
import logging
from flask import Blueprint, render_template

from src.database.infodb.service.mongo_client import MongoDBClient
from src.util.access_provider import login_required

load_dotenv()
mongodb_client = MongoDBClient()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME')) 
logger = logging.getLogger(__name__)

dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder='templates', static_folder='static')

@dashboard_bp.route("/<client_id>/<employee_id>/dashboard", methods=["GET"])
@login_required
def dashboard(client_id: str,employee_id: str):
    try:
        filter_items = {"client_id": client_id, "employee_id": employee_id}
        fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, filter_items)
        return render_template("employee/dashboard.html", user=fetch_user_info, employee_id=employee_id)
    except Exception as e:
        logger.error(f"An error occured in dashboard route: {str(e)}")
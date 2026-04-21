import os
from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, render_template
from src.database_provider.mongo_client import MongoDBClient
from src.util.access_provider import login_required

dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder='templates', static_folder='static')

mongodb_client = MongoDBClient()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME')) 

@dashboard_bp.route("/<user_id>/dashboard", methods=["GET"])
@login_required
def dashboard(user_id: str):
    fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, "user_id", user_id)
    return render_template("dashboard.html", user=fetch_user_info, user_id=user_id)
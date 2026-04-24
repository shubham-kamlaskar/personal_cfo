import os
from dotenv import load_dotenv
import logging
load_dotenv()
from flask import Blueprint, render_template
from src.database.infodb.service.mongo_client import MongoDBClient
from src.util.access_provider import login_required

client_dashboard_bp = Blueprint('client_dashboard_bp', __name__, template_folder='templates', static_folder='static')

mongodb_client = MongoDBClient()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME')) 
logger = logging.getLogger(__name__)

@client_dashboard_bp.route("/client_dashboard", methods=["GET"])
@login_required
def client_dashboard():
    try:
        # fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, "user_id", user_id)
        # return render_template("employee/dashboard.html", client=fetch_user_info, client_id=client_id)
        return render_template("client/client_dashboard.html", company={}, user={}, emp={})
    except Exception as e:
        logger.error(f"An error occured in dashboard route: {str(e)}")
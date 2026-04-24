import os
from dotenv import load_dotenv
import logging
load_dotenv()
from flask import Blueprint, render_template
from src.database.infodb.service.mongo_client import MongoDBClient
from src.util.access_provider import login_required

mongodb_client = MongoDBClient()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME')) 
logger = logging.getLogger(__name__)

tax_filling_bp = Blueprint('tax_filling_bp', __name__, template_folder='templates', static_folder='static')

@tax_filling_bp.route("/<user_id>/tax_filling", methods=["GET"])
@login_required
def tax_filling(user_id: str):
    try:
        fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, "user_id", user_id)
        return render_template("employee/tax_filling.html", user=fetch_user_info, user_id=user_id)
    except Exception as e:
        logger.error(f"An error occured in tax_filling route: {str(e)}")
        
@tax_filling_bp.route("/<user_id>/post_tax_filling", methods=["POST"])
@login_required
def post_tax_filling(user_id: str):
    try:
        fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, "user_id", user_id)
        return render_template("employee/tax_filling.html", user=fetch_user_info, user_id=user_id)
    except Exception as e:
        logger.error(f"An error occured in post_tax_filling route: {str(e)}")
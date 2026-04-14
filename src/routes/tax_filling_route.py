import os
from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, render_template
from src.database_provider.mongo_client import MongoDBClient

mongodb_client = MongoDBClient()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME')) 

tax_filling_bp = Blueprint('tax_filling_bp', __name__, template_folder='templates', static_folder='static')

@tax_filling_bp.route("/<user_id>/tax_filling", methods=["GET"])
def tax_filling(user_id: str):
    fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, "user_id", user_id)
    return render_template("tax_filling.html", user=fetch_user_info, user_id=user_id)
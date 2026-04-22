import os
from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, render_template, request, jsonify
from src.database_provider.mongo_client import MongoDBClient
from src.database_provider.strategy.investment_strategy import update_user_investments_in_db
from src.util.access_provider import login_required

investments_bp = Blueprint('investments_bp', __name__, template_folder='templates', static_folder='static')

mongodb_client = MongoDBClient()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME')) 

@investments_bp.route("/<user_id>/investments", methods=["GET"])
@login_required
def investments(user_id: str):
    fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, "user_id", user_id)
    return render_template("investments.html", user=fetch_user_info, user_id=user_id)

@investments_bp.route("/<user_id>/add_investments", methods=["POST"])
@login_required
def add_investments(user_id: str):
    data = request.get_json()
    fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, "user_id", user_id)

    if data:
        financial_year = data.get('fy')
        investments = data.get("investments", [])
        totals = data.get('totals', [])
        summary = data.get('summary', [])

        if not investments:
            return jsonify({"status": "error", "message": "No investments received"}), 400

        update_user_investments_in_db(fetch_user_info, investments, totals, user_id) 

    return jsonify({
        "status": "success",
        "message": "Investments saved"
    })
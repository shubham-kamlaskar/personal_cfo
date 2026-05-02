import os
from dotenv import load_dotenv
import logging
load_dotenv()
from flask import Blueprint, render_template, request, jsonify
from src.database.infodb.service.mongo_client import MongoDBClient
from src.database.infodb.strategy.investment_strategy import update_user_investments_in_db
from src.util.access_provider import login_required

mongodb_client = MongoDBClient()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME')) 
logger = logging.getLogger(__name__)

investments_bp = Blueprint('investments_bp', __name__, template_folder='templates', static_folder='static')

@investments_bp.route("/<client_id>/<employee_id>/investments", methods=["GET"])
@login_required
def investments(client_id: str, employee_id: str):
    try:
        fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, "employee_id", employee_id)
        return render_template("employee/investments.html", user=fetch_user_info, client_id=client_id,employee_id=employee_id)
    except Exception as e:
        logger.error(f"An error occured in investments route: {str(e)}")
        
@investments_bp.route("/<client_id>/<employee_id>/add_investments", methods=["POST"])
@login_required
def add_investments(client_id: str, employee_id: str):
    try:
        data = request.get_json()
        fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, "employee_id", employee_id)

        if data:
            financial_year = data.get('fy')
            investments = data.get("investments", [])
            totals = data.get('totals', [])
            summary = data.get('summary', [])

            if not investments:
                return jsonify({"status": "error", "message": "No investments received"}), 400

            update_user_investments_in_db(fetch_user_info, investments, totals, employee_id) 

        return jsonify({
            "status": "success",
            "message": "Investments saved"
        })
    except Exception as e:
        logger.error(f"An error occured in add_investments route: {str(e)}")
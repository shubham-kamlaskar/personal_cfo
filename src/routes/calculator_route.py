import os
from dotenv import load_dotenv
from flask import Blueprint, render_template, request, jsonify

from src.database_provider.strategy.calculate_tax_strategy import update_calculate_tax_in_db
from src.util.calculation_helper import TaxEngine
from src.database_provider.mongo_client import MongoDBClient


load_dotenv()
tax_engine = TaxEngine()
mongodb_client = MongoDBClient()

calculator_bp = Blueprint('calculator_bp', __name__, template_folder='templates', static_folder='static')

db_name = str(os.getenv('DB_NAME'))
tax_calculator_collection = str(os.getenv("TAX_CALCULATOR_COLLECTION"))
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))

@calculator_bp.route("/<user_id>/calculator", methods=["GET"])
def calculator(user_id: str):
    fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, "user_id", user_id)
    return render_template("calculator.html", user=fetch_user_info, user_id=user_id)

@calculator_bp.route("/<user_id>/tax_calculator", methods=["POST"])
def tax_calculator(user_id: str):
    if request.method == "POST":
        data = request.get_json()
        if data:
            selected: dict = update_calculate_tax_in_db(data, user_id)

            return jsonify({
                "selected_regime": selected.get('selected_regime'),
                "gross": round(selected.get('gross_income'), 2),
                "taxable_income": round(selected.get('taxable_income'), 2),
                "total_tax": round(selected.get('selected_tax'), 2),
                "total_deductions": round(selected.get('total_deductions'), 2),
                "tax_before_cess": round(selected.get('selected_base_tax'), 2),
                "cess": round(selected.get('selected_extra_cess'), 2),
                "old_regime_tax": round(selected.get('old_regime_tax'), 2),
                "new_regime_tax": round(selected.get('new_regime_tax'), 2)
            })

    return jsonify({"error": "Invalid request"}), 400

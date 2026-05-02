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
        # fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, "employee_id", employee_id)
        # return render_template("employee/dashboard.html", client=fetch_user_info, client_id=client_id)
        company = {
            "name": "ABC Corporation",
            "plan": "Premium",
            "total_employees": 150,
            "active_employees": 120,
            "filing_percentage": 80,
            "filed_count": 100,
            "total_savings": 50000,
            "monthly_bill": 15000,
            "next_billing_date": "2026-12-30",
            "pending_amount": 0,
            "payment_due_date": "2026-12-30",
            "pending_payments": 10000,
            "status_counts": {
                "filed": 500,
                "review": 200,
                "pending": 100,
                "not_started": 50
            }
        }
        user= {
            "initials": "JDK",
            "name": "John Digital Kumar",
        }
        emp = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "status": "Active",
            "department": "Engineering",
            "tax_savings": 5000,
            "last_updated": "2026-12-30"
        }
        return render_template("client/client_dashboard.html", company=company, user=user, emp=emp)
    except Exception as e:
        logger.error(f"An error occured in dashboard route: {str(e)}")
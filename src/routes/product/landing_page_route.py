from flask import Blueprint, render_template, request, jsonify
from src.util.datetime_helper import get_current_dt_in_milliseconds_precision
from src.database.infodb.service.mongo_client import MongoDBClient
import uuid
from src.models.client_object import DemoRequest
import logging

mongodb_client = MongoDBClient()
db_name = "client"
collection_name = "demo_request"
logger = logging.getLogger(__name__)
landing_page_bp = Blueprint('landing_page_bp', __name__, template_folder='templates', static_folder='static')

@landing_page_bp.route("/", methods=['GET'])
def landing_page():
    return render_template("product/landing_page.html")

@landing_page_bp.route("/demo_request", methods=["POST"])
def demo_request():
    try:
        data = request.get_json()

        if not data or "email" not in data:
            return jsonify({
                "status": "error",
                "message": "Email is required"
            }), 400

        email = data.get("email")
        ip_address = request.remote_addr
        user_agent = request.headers.get("User-Agent")
        request_id = str(uuid.uuid4())
        createdAt = get_current_dt_in_milliseconds_precision()

        demo_request_data = DemoRequest(
            request_id=request_id,
            email=email,
            ip_address=ip_address,
            user_agent=user_agent,
            createdAt=createdAt
        )

        mongodb_client.insert_one_item_in_collection(
            database_name=db_name,
            collection_name=collection_name,
            data=demo_request_data.model_dump()
        )

        return jsonify({
            "status": "success",
            "message": "Request saved"
        }), 200

    except Exception as e:
        logger.error(f"Error saving demo request: {str(e)}")

        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500

@landing_page_bp.route("/about", methods=['GET'])
def about():
    return render_template("home/about.html")

@landing_page_bp.route("/careers", methods=['GET'])
def careers():
    return render_template("home/careers.html")

@landing_page_bp.route("/contact", methods=['GET'])
def contact():
    return render_template("home/contact.html")

@landing_page_bp.route("/privacy", methods=['GET'])
def privacy():
    return render_template("home/privacy.html")

@landing_page_bp.route("/terms", methods=['GET'])
def terms():
    return render_template("home/terms.html")
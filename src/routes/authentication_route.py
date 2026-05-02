import os
from dotenv import load_dotenv
import logging
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session

from src.database.infodb.service.mongo_client import MongoDBClient
from src.database.infodb.strategy.signup_strategy import update_signup_form_in_db
from src.util.datetime_helper import get_current_dt_in_milliseconds_precision
from src.util.userid_generator import generate_employee_id
from src.util.app_constants import VariableConstant
from src.util.password_helper import PasswordHelper
from src.models.authentication_object import UserInfo

load_dotenv()
mongodb_client = MongoDBClient()
password_helper = PasswordHelper()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME')) 
email_id_field = VariableConstant.EMAIL_ID_FIELD_DB
employee_id_field = VariableConstant.EMPLOYEE_ID_FIELD_DB
logger = logging.getLogger(__name__)

authentication_bp = Blueprint('authentication_bp', __name__, template_folder='templates', static_folder='static')

@authentication_bp.route("/login", methods=["GET"])
def login():
    return render_template("authentication/login.html")

@authentication_bp.route("/login_user", methods=["POST"])
def loginUser():
    try:
        if request.method == "POST":
            data = request.get_json()
            if data:
                email = data.get("email")
                password = data.get("password")

            filter_items = {email_id_field: email}
            fetch_user_info = mongodb_client.find_one_item_from_collection("user_info", "LoginInfo", filter_items)
            if fetch_user_info:
                if email.lower() == fetch_user_info.get('email'):
                    fetch_password = fetch_user_info.get('password')
                    if password_helper.verify_password_hash(password, fetch_password):
                        
                        user_info = UserInfo(
                            client_id = fetch_user_info.get('client_id'),
                            employee_id = fetch_user_info.get('employee_id'),
                            rbac_role = fetch_user_info.get('rbac_role')
                        )
                        last_user_activity = {"billing_info.last_user_activity": get_current_dt_in_milliseconds_precision()}
                        session['user'] = user_info.employee_id
                        filter_items = {"client_id": user_info.client_id,
                                        "employee_id": user_info.employee_id}
                        mongodb_client.update_one_item_in_collection(db_name, user_info_collection,
                                                                    filter_items, last_user_activity )
                        if user_info.client_id != "CLT-2600000":
                            return jsonify({
                                        "status": "success",
                                        "redirect": url_for("dashboard_bp.dashboard", client_id= user_info.client_id, employee_id=user_info.employee_id)
                                    })
                        else:
                            return jsonify({
                                        "status": "success",
                                        "redirect": url_for("admin_dashboard_bp.admin_dashboard", client_id= user_info.client_id, employee_id=user_info.employee_id)
                                    })
                            
            else:
                return render_template("authentication/login.html")
    except Exception as e:
        logger.error(f"An error occured in loginUser route: {str(e)}")
        
@authentication_bp.route("/signup", methods=["GET"])
def signup():
    return render_template("authentication/signup.html")

@authentication_bp.route("/signup_user", methods=["POST"])
def signupUser():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"message": "Invalid request"}), 400

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        repassword = data.get("repassword")

        if password != repassword:
            return jsonify({"message": "Passwords do not match"}), 400
        
        employee_id = generate_employee_id()
        password_hash = password_helper.generate_password_hash(password)
        
        update_signup_form_in_db(employee_id, name, email, password_hash)

        return jsonify({
            "message": "Account created successfully",
            "redirect": url_for("authentication_bp.loginUser")
        }), 200
    except Exception as e:
        logger.error(f"An error occured in SignupUser route: {str(e)}")
        
@authentication_bp.route("/forgot-password", methods=["GET"])
def forgot_password():
    return render_template("authentication/forgot_password.html")

@authentication_bp.route("/forgot_password_user", methods=["POST"])
def forgotPasswordUser():
    try:
        if request.method == "POST":
            data = request.get_json()
            if data:
                email = data.get("email")
                print(email)

        return jsonify({
            "message": "email send to your email id",
            "redirect": url_for("authentication_bp.loginUser")
        }), 200
    except Exception as e:
        logger.error(f"An error occured in forgotPasswordUser route: {str(e)}")
    
@authentication_bp.route("/signout", methods=["GET"])
def signout():
    session.pop("user", None)
    return redirect(url_for("authentication_bp.loginUser"))
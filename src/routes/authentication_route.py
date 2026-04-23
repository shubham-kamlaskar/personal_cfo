import os
from dotenv import load_dotenv
load_dotenv()
import logging
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session
from src.database_provider.fetch_user_info import user
from src.database_provider.mongo_client import MongoDBClient
from src.database_provider.strategy.signup_strategy import update_signup_form_in_db
from src.util.datetime_helper import get_current_dt_in_milliseconds_precision
from src.util.userid_generator import generate_user_id
from src.util.app_constants import VariableConstant
from src.util.password_helper import PasswordHelper

authentication_bp = Blueprint('authentication_bp', __name__, template_folder='templates', static_folder='static')

mongodb_client = MongoDBClient()
password_helper = PasswordHelper()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME')) 
email_id_field = VariableConstant.EMAIL_ID_FIELD_DB
user_id_field = VariableConstant.USER_ID_FIELD_DB
logger = logging.getLogger(__name__)

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

            search_item = "personal_info" + "." + email_id_field
            fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, search_item, email)
            if fetch_user_info:
                personal_info = fetch_user_info.get('personal_info')
                if email.lower() == personal_info.get('email'):
                    fetch_password = fetch_user_info.get('password')
                    if password_helper.verify_password_hash(password, fetch_password):
                        user_id = fetch_user_info.get('user_id')
                        
                        last_user_activity = {"billing_info.last_user_activity": get_current_dt_in_milliseconds_precision()}
                        session['user'] = user_id
                        mongodb_client.update_one_item_in_collection(db_name, user_info_collection,
                                                                    user_id_field, user_id, last_user_activity )
                        return jsonify({
                                    "status": "success",
                                    "redirect": url_for("dashboard_bp.dashboard", user_id=user_id)
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
        
        user_id = generate_user_id()
        password_hash = password_helper.generate_password_hash(password)
        
        update_signup_form_in_db(user_id, name, email, password_hash)

        return jsonify({
            "message": "Account created successfully",
            "redirect": url_for("authentication_bp.login")
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
            "redirect": url_for("authentication_bp.login")
        }), 200
    except Exception as e:
        logger.error(f"An error occured in forgotPasswordUser route: {str(e)}")
    
@authentication_bp.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
import os
from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, render_template, request, redirect, url_for
from src.database_provider.mongo_client import MongoDBClient
from src.util.app_constants import VariableConstant
from src.models.authentication_object import UserInfoObject, PersonalInfo, TaxInfo, EmploymentInfo, AddressInfo, IncomeInfo
from src.util.password_helper import PasswordHelper
from src.util.datetime_helper import get_current_dt_in_milliseconds_precision

user_profile_bp = Blueprint('user_profile_bp', __name__, template_folder='templates', static_folder='static')

mongodb_client = MongoDBClient()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME'))
USER_ID_FIELD_NAME =  VariableConstant.USER_ID_FIELD_DB
password_helper = PasswordHelper()

@user_profile_bp.route('/<user_id>/profile', methods=["GET"])
def profile(user_id: str):
    fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, USER_ID_FIELD_NAME, user_id)
    return render_template("user_profile/profile.html", user=fetch_user_info, user_id=user_id)

@user_profile_bp.route('/<user_id>/edit_profile', methods=["GET", "POST"])
def edit_profile(user_id: str):
    try:
        fetch_user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, USER_ID_FIELD_NAME, user_id)
        if request.method == "POST":
            form = request.form
            update_data = UserInfoObject(
                user_id = user_id,
                personal_info=PersonalInfo(
                    name= str(form.get("name")).title(),
                    dob=form.get("dob"),
                    email= str(form.get("email")).lower(),
                    phone= form.get("phone"),
                    gender= str(form.get("gender")).title(),
                    marital_status= str(form.get("marital_status")).title()
                ),

                tax_info=TaxInfo(
                    pan= str(form.get("pan")).upper(),
                    aadhar= str(form.get("aadhar")),
                    tax_regime= str(form.get("tax_regime")).title()
                ),

                employment_info=EmploymentInfo(
                    employment_type= form.get("employment_type"),
                    company= str(form.get("company")).title(),
                    designation= str(form.get("designation")).title(),
                    industry= str(form.get("industry")).title()
                ),
                income_info = IncomeInfo(
                    gross_salary= float(form.get("salary")),
                ),

                address_info=AddressInfo(
                    address_line1=form.get("address_line1"),
                    address_line2=form.get("address_line2"),
                    city= str(form.get("city")).title(),
                    state= str(form.get("state")).title(),
                    pincode= int(form.get("pincode"))
                ),
                updatedAt = get_current_dt_in_milliseconds_precision()
            )
            if form.get("new_password"):
                if password_helper.verify_password_hash(entered_password=form.get('current_password'),hashed_password=fetch_user_info['password']):
                    if form.get('new_password') == form.get('confirm_password'):
                        update_data.personal_info.password = password_helper.generate_password_hash(password=form.get("new_password"))

            mongodb_client.update_one_item_in_collection(db_name, user_info_collection, USER_ID_FIELD_NAME, user_id, update_data.model_dump(exclude_none=True))
            return redirect(url_for('user_profile_bp.profile', user_id=user_id))

        return render_template('user_profile/edit_profile.html', user=fetch_user_info, user_id=user_id)
    except Exception as e:
        raise Exception(f"An error occured in edit_profile route: {str(e)}")
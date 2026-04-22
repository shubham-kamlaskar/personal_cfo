import os
from dotenv import load_dotenv
load_dotenv()

from src.util.app_constants import VariableConstant
from src.database_provider.mongo_client import MongoDBClient
from src.util.datetime_helper import get_current_dt_in_milliseconds_precision
from src.util.password_helper import PasswordHelper

password_helper = PasswordHelper()
mongodb_client = MongoDBClient()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME'))
USER_ID_FIELD_NAME =  VariableConstant.USER_ID_FIELD_DB

def update_profile_in_db(data: dict, user_id: str, fetch_user_info):
    update_data = {
                "personal_info.name": str(data.get("name")).title(),
                "personal_info.dob":data.get("dob"),
                "personal_info.email": str(data.get("email")).lower(),
                "personal_info.phone": data.get("phone"),
                "personal_info.gender": str(data.get("gender")).title(),
                "personal_info.marital_status": str(data.get("marital_status")).title(),
                
                "tax_info.pan": str(data.get("pan")).upper(),
                "tax_info.aadhar": str(data.get("aadhar")),
                "tax_info.tax_regime": str(data.get("tax_regime")).title(),

                "employment_info.employment_type": data.get("employment_type"),
                "employment_info.company": str(data.get("company")).title() if data.get("company") else None,
                "employment_info.designation": str(data.get("designation")).title() if data.get("designation") else None,
                "employment_info.industry": str(data.get("industry")).title() if data.get("industry") else None,

                "income_info.gross_salary": float(data.get("salary", 0)),

                "address_info.address_line1": str(data.get("address_line1")),
                "address_info.address_line2": str(data.get("address_line2")),
                "address_info.city": str(data.get("city")).title(),
                "address_info.state": str(data.get("state")).title(),
                "address_info.pincode": int(data.get("pincode", 000000)),

                "updatedAt": get_current_dt_in_milliseconds_precision()   
            }
            
    if data.get("new_password"):
        if password_helper.verify_password_hash(entered_password=data.get('current_password'),hashed_password=fetch_user_info['password']):
            if data.get('new_password') == data.get('confirm_password'):
                update_data["password"] = password_helper.generate_password_hash(password=data.get("new_password"))

    mongodb_client.update_one_item_in_collection(db_name, user_info_collection, USER_ID_FIELD_NAME, user_id, update_data)
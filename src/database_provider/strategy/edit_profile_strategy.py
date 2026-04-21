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
                "personal_info":{
                        "name": str(data.get("name")).title(),
                        "dob":data.get("dob"),
                        "email": str(data.get("email")).lower(),
                        "phone": data.get("phone"),
                        "gender": str(data.get("gender")).title(),
                        "marital_status": str(data.get("marital_status")).title(),
                },
                
                "tax_info": {
                    "pan": str(data.get("pan")).upper(),
                    "aadhar": str(data.get("aadhar")),
                    "tax_regime": str(data.get("tax_regime")).title()
                },
                
                "employment_info": {
                        "employment_type": data.get("employment_type"),
                        "company": str(data.get("company")).title() if data.get("company") else None,
                        "designation": str(data.get("designation")).title() if data.get("designation") else None,
                        "industry": str(data.get("industry")).title() if data.get("industry") else None,
                },
                
                "income_info": {
                    "gross_salary": float(data.get("salary")),
                },
                
                "address_info": {
                    "address_line1": str(data.get("address_line1")),
                    "address_line2": str(data.get("address_line2")),
                    "city": str(data.get("city")).title(),
                    "state": str(data.get("state")).title(),
                    "pincode": int(data.get("pincode")),
                },
                
                "updatedAt": get_current_dt_in_milliseconds_precision()   
            }
            
    if data.get("new_password"):
        if password_helper.verify_password_hash(entered_password=data.get('current_password'),hashed_password=fetch_user_info['password']):
            if data.get('new_password') == data.get('confirm_password'):
                update_data["password"] = password_helper.generate_password_hash(password=data.get("new_password"))

    mongodb_client.update_one_item_in_collection(db_name, user_info_collection, USER_ID_FIELD_NAME, user_id, update_data)
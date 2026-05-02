import os
from dotenv import load_dotenv
load_dotenv()
from src.models.authentication_object import UserInfoObject, PersonalInfo, BillingInfo
from src.util.datetime_helper import get_current_dt_in_milliseconds_precision
from src.database.infodb.service.mongo_client import MongoDBClient
mongodb_client = MongoDBClient()

user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME')) 

def update_signup_form_in_db(employee_id, name, email, password_hash):
    signup_data = UserInfoObject(
        employee_id = employee_id,
        password=password_hash,
        personal_info= PersonalInfo(
                name=name.title(),
                email=email.lower(),   
        ),
        billing_info = BillingInfo(
                subscription_status="Active",
                subscription_plan="Free Plan",
                member_since=get_current_dt_in_milliseconds_precision(),
                account_active_status=True,
                next_billing_date=get_current_dt_in_milliseconds_precision(),
                preference={"email_notification":"True",
                            "sms_alerts": "False",
                            "two_factor": "False",
                            "dark_mode": "False"},
        ),
        createdAt=get_current_dt_in_milliseconds_precision(),
        updatedAt=get_current_dt_in_milliseconds_precision(),
    )

    mongodb_client.insert_one_item_in_collection(database_name=db_name,
                                                 collection_name=user_info_collection,
                                                 data=signup_data.model_dump())
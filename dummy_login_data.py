from src.util.datetime_helper import get_current_dt_in_milliseconds_precision
from src.database.infodb.service.mongo_client import MongoDBClient
from src.util.password_helper import PasswordHelper

mongodb_client = MongoDBClient()
password_helper = PasswordHelper()

# data = [
#     {
#         "client_id": "CLT-2600000",
#         "employee_id": "EMP-000001",
#         "email": "super_admin@personalinfo.com",
#         "password": password_helper.generate_password_hash("admin"),
#         "rbac_role": "super_admin",
#         "createdAt": get_current_dt_in_milliseconds_precision(),
#         "updatedAt": get_current_dt_in_milliseconds_precision()
#     },
#     {
#         "client_id": "CLT-2600000",
#         "employee_id": "EMP-000002",
#         "email": "admin@personalinfo.com",
#         "password": password_helper.generate_password_hash("admin"),
#         "rbac_role": "admin",
#         "createdAt": get_current_dt_in_milliseconds_precision(),
#         "updatedAt": get_current_dt_in_milliseconds_precision()
#     },
#     {
#         "client_id": "CLT-2600000",
#         "employee_id": "EMP-000003",
#         "email": "support@personalinfo.com",
#         "password": password_helper.generate_password_hash("admin"),
#         "rbac_role": "support",
#         "createdAt": get_current_dt_in_milliseconds_precision(),
#         "updatedAt": get_current_dt_in_milliseconds_precision()
#     },
#     {
#         "client_id": "CLT-2600000",
#         "employee_id": "EMP-000004",
#         "email": "finance@personalinfo.com",
#         "password": password_helper.generate_password_hash("admin"),
#         "rbac_role": "finance",
#         "createdAt": get_current_dt_in_milliseconds_precision(),
#         "updatedAt": get_current_dt_in_milliseconds_precision()
#     },
#     {
#         "client_id": "CLT-2600000",
#         "employee_id": "EMP-000005",
#         "email": "ca@personalinfo.com",
#         "password": password_helper.generate_password_hash("admin"),
#         "rbac_role": "ca",
#         "createdAt": get_current_dt_in_milliseconds_precision(),
#         "updatedAt": get_current_dt_in_milliseconds_precision()
#     },
#     {
#         "client_id": "CLT-2600000",
#         "employee_id": "EMP-000006",
#         "email": "hr@personalinfo.com",
#         "password": password_helper.generate_password_hash("admin"),
#         "rbac_role": "hr",
#         "createdAt": get_current_dt_in_milliseconds_precision(),
#         "updatedAt": get_current_dt_in_milliseconds_precision()
#     },
#     {
#         "client_id": "CLT-2600000",
#         "employee_id": "EMP-000008",
#         "email": "employee@personalinfo.com",
#         "password": password_helper.generate_password_hash("admin"),
#         "rbac_role": "employee",
#         "createdAt": get_current_dt_in_milliseconds_precision(),
#         "updatedAt": get_current_dt_in_milliseconds_precision()
#     },

#     # Client 2
#     {
#         "client_id": "CLT-2600001",
#         "employee_id": "EMP-000001",
#         "email": "super_admin_client@amphibius.com",
#         "password": password_helper.generate_password_hash("admin"),
#         "rbac_role": "super_admin",
#         "createdAt": get_current_dt_in_milliseconds_precision(),
#         "updatedAt": get_current_dt_in_milliseconds_precision()
#     },
#     {
#         "client_id": "CLT-2600001",
#         "employee_id": "EMP-000002",
#         "email": "admin_client@amphibius.com",
#         "password": password_helper.generate_password_hash("admin"),
#         "rbac_role": "admin",
#         "createdAt": get_current_dt_in_milliseconds_precision(),
#         "updatedAt": get_current_dt_in_milliseconds_precision()
#     },
#     {
#         "client_id": "CLT-2600001",
#         "employee_id": "EMP-000003",
#         "email": "employee_client@amphibius.com",
#         "password": password_helper.generate_password_hash("admin"),
#         "rbac_role": "employee",
#         "createdAt": get_current_dt_in_milliseconds_precision(),
#         "updatedAt": get_current_dt_in_milliseconds_precision()
#     },
#     {
#         "client_id": "CLT-2600001",
#         "employee_id": "EMP-000004",
#         "email": "finance_client@amphibius.com",
#         "password": password_helper.generate_password_hash("admin"),
#         "rbac_role": "finance",
#         "createdAt": get_current_dt_in_milliseconds_precision(),
#         "updatedAt": get_current_dt_in_milliseconds_precision()
#     },
#     {
#         "client_id": "CLT-2600001",
#         "employee_id": "EMP-000005",
#         "email": "support_client@amphibius.com",
#         "password": password_helper.generate_password_hash("admin"),
#         "rbac_role": "support",
#         "createdAt": get_current_dt_in_milliseconds_precision(),
#         "updatedAt": get_current_dt_in_milliseconds_precision()
#     },
#     {
#         "client_id": "CLT-2600001",
#         "employee_id": "EMP-000006",
#         "email": "employee2_client@amphibius.com",
#         "password": password_helper.generate_password_hash("admin"),
#         "rbac_role": "employee",
#         "createdAt": get_current_dt_in_milliseconds_precision(),
#         "updatedAt": get_current_dt_in_milliseconds_precision()
#     },
# ]

# for i in data:
#     mongodb_client.insert_one_item_in_collection(database_name="user_info",
#                                                  collection_name="LoginInfo",
#                                                  data=i)
import os
from dotenv import load_dotenv

from flask import Blueprint, render_template, request, jsonify
from src.database.infodb.service.mongo_client import MongoDBClient
from src.models.client_object import ClientOnboarding, ClientInfo, ClientBillingInfo, ClientSuperAdminInfo, ClientEmpInfo
from src.models.internal_employee_object import InternalEmployeeInfo
from src.util.datetime_helper import get_current_dt_in_milliseconds_precision
from datetime import datetime
from src.models.ca_object import CAOnboarding, PersonalInfo, CAProfessionalInfo, CASpecialization, CADocuments, CAServiceAgreement, ActiveStatus
from src.util.generate_id import generate_client_id
from src.models.authentication_object import LoginObject
from src.util.password_helper import PasswordHelper

load_dotenv()
mongodb_client = MongoDBClient()
client_onboarding_collection = str(os.getenv('CLIENT_ONBOARDING_COLLECTION'))
employee_collection = str(os.getenv('EMPLOYEE_COLLECTION'))
ca_collection = str(os.getenv('CA_COLLECTION'))
db_name = str(os.getenv('CLIENT_DB_NAME')) 
password_helper = PasswordHelper()

admin_dashboard_bp = Blueprint('admin_dashboard_bp', __name__, template_folder='templates', static_folder='static')

### dashboard management routes ###

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/admin_dashboard", methods=["GET"])
def admin_dashboard(client_id: str, employee_id: str):
    return render_template("admin/dashboard/dashboard_panel.html", client_id=client_id, employee_id=employee_id)

### client management routes ###

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/client/list", methods=["GET"])
def list_client(client_id: str, employee_id: str):
    fetch_client_onboarding = mongodb_client.fetch_all_records_from_collection(db_name, client_onboarding_collection)
    return render_template("admin/client/admin_client_list.html", client_id=client_id, employee_id=employee_id, clients=fetch_client_onboarding)

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/client/add", methods=["GET"])
def add_client(client_id: str, employee_id: str):
    return render_template("admin/client/admin_add_client.html", client_id=client_id, employee_id=employee_id)

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/client/add/confirm", methods=["POST"])
def confirm_add_client(client_id: str, employee_id: str):
    client_count = mongodb_client.count_all_records_from_collection(db_name, client_onboarding_collection)
    client_id= "CLT-" + "2600" + str(generate_client_id(client_count))
    data = request.get_json()
    current_dt = get_current_dt_in_milliseconds_precision()
    if data:
        update_data = ClientInfo(
            client_id=client_id,
            client_onboarding= ClientOnboarding(
                legal_name = data.get("legal_name", None),
                short_name = data.get("short_name", None),
                pan= data.get("pan", None),
                gstin = data.get("gstin", None),
                address = data.get("address", None),
                city = data.get("city", None),
                state = data.get("state", None),
                pincode = data.get("pincode", None),
                industry = data.get("industry", None),
                notes = data.get("notes", None),
                send_welcome_note = data.get("send_welcome_note", None),
                client_added_by = employee_id,
            ),
        client_super_admin_info= ClientSuperAdminInfo(
            admin_name= data.get('admin_name', None),
            admin_email= data.get('admin_email', None),
            admin_phone= data.get('admin_phone', None),
            admin_designation= data.get('admin_designation', None),
            admin_department= data.get('admin_department', None),
        ),
        client_billing_info= ClientBillingInfo(
            plan = data.get('admin_name', None) ,
            billing_cycle= data.get('billing_cycle', None),
            billing_start_date= current_dt,
            next_billing_date= current_dt,
        ),
        client_emp_info = ClientEmpInfo(
            total_employees=data.get('billing_cycle', None)
            active_employees=data.get('billing_cycle', None)
        ),
        
    
        
        mongodb_client.insert_one_item_in_collection(db_name, client_onboarding_collection,
                                                     update_data.model_dump())
        
        update_login_data = LoginObject(
            client_id= client_id,
            employee_id= "EMP-" + "2600" + str(generate_client_id(0)),
            email = data.get("admin_email", None),
            password = password_helper.generate_password_hash("EMP-" + "2600" + str(generate_client_id(0))),
            rbac_role= ["super_admin","Employee"],
            createdAt= current_dt,
            updatedAt= current_dt
        )
        
        mongodb_client.insert_one_item_in_collection("user_info", "LoginInfo",
                                                     update_data.model_dump())
        
        total_employees = data.get("employee_count", None),
        super_admin_name = data.get("admin_name", None),
        super_admin_email = data.get("admin_email", None),
        super_admin_phone = data.get("admin_phone", None),
        super_admin_designation = data.get("admin_designation", None), 
        
        return jsonify({
            "status": "success",
            "message": "Client create successfully!"
        })
        

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/client/remove", methods=["GET"])
def remove_client(client_id: str, employee_id: str):
    return render_template("admin/client/admin_add_client.html", client_id=client_id, employee_id=employee_id)

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/client/modify", methods=["GET"])
def modify_client(client_id: str, employee_id: str):
    return render_template("admin/client/admin_add_client.html", client_id=client_id, employee_id=employee_id)

### ca management routes ###

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/ca/add", methods=["GET"])
def add_ca(client_id: str, employee_id: str):
    return render_template("admin/ca/admin_add_ca.html", client_id=client_id, employee_id=employee_id)

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/ca/add/confirm", methods=["POST"])
def confirm_add_ca(client_id: str, employee_id: str):
    ca_count = mongodb_client.count_all_records_from_collection(db_name, ca_collection)
    
    # Handle form data and files
    current_dt = get_current_dt_in_milliseconds_precision()
    employee_id = "CA-" + "2600" + str(generate_client_id(ca_count))
    form = request.form
    files = request.files
    
    update_login_data = LoginObject(
        client_id=client_id,
        employee_id = employee_id,
        email = form.get("email", None),
        password = password_helper.generate_password_hash(employee_id), # type: ignore
        rbac_role= ["ca", "employee"],
        createdAt= current_dt,
        updatedAt=current_dt
    )
    mongodb_client.insert_one_item_in_collection("user_info", "LoginInfo",
                                                 update_login_data.model_dump())
    
    update_personal_info = PersonalInfo(
                client_id=client_id,
                employee_id = employee_id,
                title= form.get("title", None),
                full_name = form.get("full_name", None),
                alternate_email = form.get("alternate_email", None),
                phone = form.get("phone", None),
                whatsapp = form.get("whatsapp", None),
                dob = form.get("dob", None),
                gender = form.get("gender", None),
                address = form.get("address", None),
                city = form.get("city", None),
                state = form.get("state", None),
                pincode = form.get("pincode", None),
                pan = form.get("pan", None),
                aadhaar = form.get("aadhaar", None),
                createdAt= current_dt,
                updatedAt= current_dt,
                )
    
    mongodb_client.insert_one_item_in_collection("user_info", "PersonalInfo",
                                                 update_personal_info.model_dump())
    
    update_caprofessional_info= CAProfessionalInfo(
                client_id=client_id,
                employee_id = employee_id,
                icai_number= form.get("icai_number", None),
                membership_type= form.get("membership_type", None),
                qualification_date= form.get("qualification_date", None),
                experience_years= form.get("experience_years", None),
                cop_number= form.get("cop_number", None),
                firm_name= form.get("firm_name", None),
                firm_registration= form.get("firm_registration", None),
                office_address= form.get("office_address", None),
                office_city= form.get("office_city", None),
                office_state= form.get("office_state", None),
                office_pincode= form.get("office_pincode", None),
                bio= form.get("bio", None),
                createdAt= current_dt,
                updatedAt= current_dt,
            )
    mongodb_client.insert_one_item_in_collection("user_info", "CAProfessionalInfo",
                                                 update_caprofessional_info.model_dump())
    
    update_specialization = CASpecialization(
            client_id=client_id,
            employee_id = employee_id,
            primary_specialization= form.get("primary_specialization", None),
            client_size= form.get("client_size", None),
            languages= form.get("languages", None),
            additional_services= form.getlist("additional_services"),
            tax_services= form.getlist("tax_services"),
            industry_expertise= form.getlist("industry_expertise"),
            createdAt= current_dt,
            updatedAt= current_dt,
            )
    mongodb_client.insert_one_item_in_collection("user_info", "CASpecialization",
                                                 update_specialization.model_dump())
    
    update_cadocuments = CADocuments(
            client_id=client_id,
            employee_id = employee_id,
            icai_cert = files.get("icai_cert").filename if files.get("icai_cert") else None,
            cop_cert = files.get("cop_cert").filename if files.get("cop_cert") else None,
            pan_doc = files.get("pan_doc").filename if files.get("pan_doc") else None,
            aadhaar_doc = files.get("aadhaar_doc").filename if files.get("aadhaar_doc") else None,
            resume = files.get("resume").filename if files.get("resume") else None,
            photo = files.get("photo").filename if files.get("photo") else None,
            certs = files.get("certs").filename if files.get("certs") else None,
            createdAt= current_dt,
            updatedAt= current_dt,
        )
    mongodb_client.insert_one_item_in_collection("user_info", "CADocuments",
                                                 update_cadocuments.model_dump())
    
    uodate_caservice_agreement = CAServiceAgreement(
                client_id=client_id,
                employee_id = employee_id,
                engagement_type= form.get("engagement_type", None) ,
                rate_itr_individual= form.get("rate_itr_individual", None) ,
                rate_itr_business= form.get("rate_itr_business", None) ,
                rate_consultation= form.get("rate_consultation", None) ,
                rate_gsts= form.get("rate_gst", None) ,
                revenue_share= form.get("revenue_share", None) ,
                payment_terms= form.get("payment_terms", None) ,
                max_clients= form.get("max_clients", None) ,
                response_time= form.get("response_time", None) ,
                work_hours_from= form.get("work_hours_from", None) ,
                work_hours_to= form.get("work_hours_to", None) ,
                working_day= form.getlist("working_day") ,
                bank_account_name= form.get("bank_account_name", None) ,
                bank_name= form.get("bank_name", None) ,
                bank_ifsc= form.get("bank_ifsc", None) ,
                createdAt= current_dt,
                updatedAt= current_dt,
            )
    
    mongodb_client.insert_one_item_in_collection("user_info", "CAServiceAgreement",
                                                 uodate_caservice_agreement.model_dump())
    
    update_active_status = ActiveStatus(
                client_id=client_id,
                employee_id = employee_id,
                is_active = True,
                last_active_datetime= current_dt
    )
    
    mongodb_client.insert_one_item_in_collection("user_info", "ActiveStatus",
                                                 update_active_status.model_dump())
    
    return jsonify({
        "status": "success",
        "message": "CA created successfully!"
    })

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/ca/list", methods=["GET"])
def ca_list(client_id: str, employee_id: str):
    fetch_ca_info = mongodb_client.fetch_all_records_from_collection(db_name, ca_collection)
    return render_template("admin/ca/admin_ca_list.html", client_id=client_id, employee_id=employee_id, cas=fetch_ca_info)

### billing management routes ###

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/billing", methods=["GET"])
def billing(client_id: str, employee_id: str):
    return render_template("admin/billing/admin_client_billing.html", client_id=client_id, employee_id=employee_id)

### compliance management routes ###

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/compliance", methods=["GET"])
def compliance(client_id: str, employee_id: str):
    return render_template("admin/compliance/admin_compliance_checker.html", client_id=client_id, employee_id=employee_id)

### analytics management routes ###

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/analytics", methods=["GET"])
def analytics(client_id: str, employee_id: str):
    return render_template("admin/analytics/admin_expense_analytics.html", client_id=client_id, employee_id=employee_id)

### support management routes ###

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/support", methods=["GET"])
def support(client_id: str, employee_id: str):
    return render_template("admin/support/admin_support_ticket.html", client_id=client_id, employee_id=employee_id)

### user management routes ###

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/employee/add", methods=["GET"])
def employee_add(client_id: str, employee_id: str):
    return render_template("admin/employee/admin_user_management.html", client_id=client_id, employee_id=employee_id)

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/employee/add/confirm", methods=["POST"])
def confirm_employee_add(client_id: str, employee_id: str):
    emp_count = mongodb_client.count_all_records_from_collection(db_name, employee_collection)

    data = request.get_json()
    if data:
        update_data = InternalEmployeeInfo(
            client_id=client_id,
            employee_id= "EMP-" + "2600" + str(generate_client_id(emp_count)),
            employee_name= data.get('legal_name', None),
            employee_initials=data.get('display_name', None),
            dob = data.get('dob'),
            doj = data.get('doj'),
            pan=data.get('pan', None),
            aadhar=data.get('aadhar', None),
            registered_address=data.get('address', None),
            city=data.get('city', None),
            state=data.get('state', None),
            pincode=data.get('pincode', None),
            manager_name=data.get('manager_name', None),
            manager_id= data.get('manager_id', None),
            department=data.get('department', None),
            designation=data.get('designation', None),
            role=data.get('role', None),
            createdAt=get_current_dt_in_milliseconds_precision(),
            updatedAt=get_current_dt_in_milliseconds_precision()
        )
        
        mongodb_client.insert_one_item_in_collection(db_name, employee_collection,
                                                     update_data.model_dump())
    
        
        return jsonify({
            "status": "success",
            "message": "Employee create successfully!"
        })
    

@admin_dashboard_bp.route("/<client_id>/<employee_id>/admin/employee/list", methods=["GET"])
def employee_list(client_id: str, employee_id: str):
    fetch_employee_info = mongodb_client.fetch_all_records_from_collection(db_name, employee_collection)
    return render_template("admin/employee/admin_user_list.html", client_id=client_id, employee_id=employee_id, employees=fetch_employee_info)

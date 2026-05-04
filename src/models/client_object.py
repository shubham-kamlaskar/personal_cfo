from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime

class DemoRequest(BaseModel):
    request_id: Optional[str] = None
    email: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    status: Optional[str] = None
    addtional_info: Optional[Any] = None
    representative_id: Optional[str] = None
    createdAt: Optional[datetime] = None
    responedOn: Optional[datetime] = None

class ClientOnboarding(BaseModel):
    legal_name: Optional[str] = None
    short_name: Optional[str] = None
    pan: Optional[str] = None
    gstin: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[int] = None
    industry: Optional[str] = None
    notes: Optional[str] = None
    send_welcome_note: Optional[str] = None
    client_added_by: Optional[str] = None
    
class ClientSuperAdminInfo(BaseModel):
    admin_name: Optional[str] = None
    admin_email: Optional[str] = None
    admin_phone: Optional[str] = None
    admin_designation: Optional[str] = None
    admin_department: Optional[str] = None
    
class ClientBillingInfo(BaseModel):
    plan: Optional[str] = None
    billing_cycle: Optional[str] = None
    billing_start_date: Optional[datetime] = None
    next_billing_date: Optional[datetime] = None
    pending_payments: Optional[int] = None
    pending_amount: Optional[float] = None
    payment_due_date: Optional[datetime] = None
    
class ClientEmpInfo(BaseModel):
    total_employees: Optional[int] = None
    active_employees: Optional[int] = None
    filing_percentage: Optional[float] = None
    filed_count: Optional[int] = None
    total_savings: Optional[float] = None
    monthly_bill: Optional[float] = None
    status_counts : Optional[dict[str,int]] = None
    
class ActiveStatus(BaseModel):
    is_approved: Optional[bool] = None
    is_active: Optional[bool] = None
    last_active_datetime: Optional[datetime] = None
    
class ClientInfo(BaseModel):
    client_id: Optional[str] = None 
    client_onboarding: Optional[ClientOnboarding] = None
    client_super_admin_info: Optional[ClientSuperAdminInfo] = None
    client_billing_info: Optional[ClientBillingInfo] = None
    client_emp_info: Optional[ClientEmpInfo] = None
    client_active_status: Optional[ActiveStatus] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    

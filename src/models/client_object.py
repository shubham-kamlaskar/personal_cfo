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
    client_id: Optional[str] = None
    client_password: Optional[bytes] = None
    legal_name: Optional[str] = None
    short_name: Optional[str] = None
    pan: Optional[str] = None
    gstin: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[int] = None
    industry: Optional[str] = None
    employee_count: Optional[int] = None

    admin_name: Optional[str] = None
    admin_email: Optional[str] = None
    admin_phone: Optional[str] = None
    admin_designation: Optional[str] = None
    notes: Optional[str] = None
    send_welcome_note: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
class ClientBillingInfo(BaseModel):
    client_id: Optional[str] = None
    plan: Optional[str] = None
    billing_cycle: Optional[str] = None
    
class ClientInfo(BaseModel):
    client_id: Optional[str] = None
    name: Optional[str] = None
    total_employees: Optional[int] = None
    active_employees: Optional[int] = None
    filing_percentage: Optional[float] = None
    filed_count: Optional[int] = None
    total_savings: Optional[float] = None
    monthly_bill: Optional[float] = None
    next_billing_date: Optional[datetime] = None
    pending_payments: Optional[int] = None
    pending_amount: Optional[float] = None
    payment_due_date: Optional[datetime] = None
    status_counts : Optional[dict[str,int]] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
class EmployeeInfo(BaseModel):
    employee_id: Optional[str] = None
    client_id: Optional[str] = None
    initials: Optional[str] = None
    name: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    designation: Optional[str] = None
    department: Optional[str] = None
    date_of_joining: Optional[str] = None
    status: Optional[str] = None
    status_class: Optional[str] = None
    tax_savings: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
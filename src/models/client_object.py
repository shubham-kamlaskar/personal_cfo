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

class ClientInfo(BaseModel):
    client_id: Optional[str] = None
    client_password: Optional[bytes] = None
    address: Optional[str] = None
    name: Optional[str] = None
    plan: Optional[str] = None
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
        # filed
        # review
        # pending
        # not_started
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
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class LoginObject(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    
class UserLoginObject(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[bytes]
    user_id: Optional[str]
    createAt: Optional[datetime]
    updatedAt: Optional[datetime]
    job_profile: Optional[str] = None
    phone: Optional[str] = None
    dob: Optional[str] = None
    pan: Optional[str] = None
    aadhar: Optional[str] = None
    tax_regime: Optional[str] = None
    employment_type: Optional[str] = None
    company: Optional[str] = None
    salary: Optional[str] = None
    deductions: Optional[str] = None
    tax_liability: Optional[str] = None
    potential_savings: Optional[str] = None
    tax_saved: Optional[str] = None
    city: Optional[str] = None
    member_since: Optional[datetime] = None
    days_active: Optional[str] = None
    account_active_status: Optional[bool] = None
    documents_len: Optional[str] = None
    subscription_plan: Optional[str] = None
    next_billing_date: Optional[datetime] = None
    preference: Optional[dict[str, str]] = None

class ForgotPasswordObject(BaseModel):
    email: Optional[str] = None
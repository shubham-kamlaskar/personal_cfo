from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime
from src.models.investment_object import Section80C, Section80D, Section80CCD, Section24B, MutualFund, OtherInvestments

class LoginObject(BaseModel):
    client_id: Optional[str] = None
    employee_id: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    rbac_role: Optional[list[str]] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class PersonalInfo(BaseModel):
    client_id: Optional[str] = None
    employee_id: Optional[str] = None
    name: Optional[str] = None
    dob: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    gender: Optional[str] = None
    marital_status: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
class TaxInfo(BaseModel):
    client_id: Optional[str] = None
    employee_id: Optional[str] = None
    pan: Optional[str] = None
    aadhar: Optional[str] = None
    tax_regime: Optional[str] = None
    deductions: Optional[float] = None
    tax_liability: Optional[float] = None
    potential_savings: Optional[float] = None
    estimated_tax_saved: Optional[float] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
class IncomeInfo(BaseModel):
    client_id: Optional[str] = None
    employee_id: Optional[str] = None
    gross_salary: Optional[float] = None
    tds_deducted: Optional[float] = None
    is_form_16_available: Optional[bool] = None
    annual_rental_income: Optional[float] = None
    home_loan_interest: Optional[float] = None
    short_term_capital_gains: Optional[float] = None
    long_term_capital_gains: Optional[float] = None
    interest_income_fd_savings: Optional[float] = None
    dividend_income: Optional[float] = None
    total_hra: Optional[float] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
class TotalInvestments(BaseModel):
    client_id: Optional[str] = None
    employee_id: Optional[str] = None
    section80c: Optional[Section80C] = None
    total_80c: Optional[Section80C] = None
    section80d: Optional[Section80D] = None
    total_80d: Optional[Section80C] = None
    section80ccd: Optional[Section80CCD] = None
    total_80ccd: Optional[Section80C] = None
    section24b: Optional[Section24B] = None
    total_24b: Optional[Section80C] = None
    mutualfund: Optional[MutualFund] = None
    total_mf: Optional[Section80C] = None
    otherinvestments: Optional[OtherInvestments] = None
    total_other: Optional[Section80C] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
class EmploymentInfo(BaseModel):
    client_id: Optional[str] = None
    employee_id: Optional[str] = None
    employment_type: Optional[str] = None
    company: Optional[str] = None
    designation: Optional[str] = None
    department: Optional[str] = None
    industry: Optional[str] = None
    date_of_joining: Optional[str] = None
    manager_name: Optional[str] = None
    manager_id: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class AddressInfo(BaseModel):
    client_id: Optional[str] = None
    employee_id: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[int] = None
    country: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
class BillingInfo(BaseModel):
    client_id: Optional[str] = None
    employee_id: Optional[str] = None
    subscription_status: Optional[str] = None
    member_since: Optional[datetime] = None
    last_user_activity: Optional[datetime] = None
    days_active: Optional[int] = None
    account_active_status: Optional[bool] = None
    documents_len: Optional[int] = None
    subscription_plan: Optional[str] = None
    next_billing_date: Optional[datetime] = None
    preference: Optional[dict[str, str]] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

    
class UserInfoObject(BaseModel):
    client_id: str
    employee_id: str
    password: Optional[bytes] = None
    rbac_role: Optional[str] = None
    personal_info: Optional[PersonalInfo] = None
    tax_info: Optional[TaxInfo] = None
    employment_info: Optional[EmploymentInfo] = None
    address_info: Optional[AddressInfo] = None
    billing_info: Optional[BillingInfo] = None
    income_info: Optional[IncomeInfo] = None
    investments_info: Optional[TotalInvestments] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
class UserInfo(BaseModel):
    client_id: str
    employee_id: str
    rbac_role: Optional[list[str]] = None


class ForgotPasswordObject(BaseModel):
    email: Optional[str] = None
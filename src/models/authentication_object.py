from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime

class LoginObject(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None

class PersonalInfo(BaseModel):
    name: Optional[str] = None
    dob: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    gender: Optional[str] = None
    marital_status: Optional[str] = None
    password: Optional[bytes] = None
    
class TaxInfo(BaseModel):
    pan: Optional[str] = None
    aadhar: Optional[str] = None
    tax_regime: Optional[str] = None
    deductions: Optional[str] = None
    tax_liability: Optional[str] = None
    potential_savings: Optional[str] = None
    tax_saved: Optional[str] = None
    
class IncomeInfo(BaseModel):
    gross_salary: Optional[float] = None
    tds_deducted: Optional[float] = None
    form_16_available: Optional[float] = None
    annual_rental_income: Optional[float] = None
    home_loan_interest: Optional[float] = None
    short_term_capital_gains: Optional[float] = None
    long_term_capital_gains: Optional[float] = None
    interest_income_fd_savings: Optional[float] = None
    dividend_income: Optional[float] = None
    
class DeductionsInfo(BaseModel):
    section_80c: Optional[float] = None
    section_80d: Optional[float] = None
    hra_examption: Optional[float] = None
    nps_80ccd: Optional[float] = None
    home_loan_interest: Optional[float] = None
    other_deductions: Optional[float] = None
    
class EmploymentInfo(BaseModel):
    employment_type: Optional[str] = None
    company: Optional[str] = None
    designation: Optional[str] = None
    industry: Optional[str] = None

class AddressInfo(BaseModel):
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[int] = None
    country: Optional[str] = None
    
class BillingInfo(BaseModel):
    subscription_status: Optional[str] = None
    member_since: Optional[datetime] = None
    last_user_activity: Optional[datetime] = None
    days_active: Optional[int] = None
    account_active_status: Optional[bool] = None
    documents_len: Optional[int] = None
    subscription_plan: Optional[str] = None
    next_billing_date: Optional[datetime] = None
    preference: Optional[dict[str, str]] = None

    
class UserInfoObject(BaseModel):
    user_id: Optional[str] = None
    personal_info: Optional[PersonalInfo] = None
    tax_info: Optional[TaxInfo] = None
    employment_info: Optional[EmploymentInfo] = None
    address_info: Optional[AddressInfo] = None
    billing_info: Optional[BillingInfo] = None
    income_info: Optional[IncomeInfo] = None
    deductions_info: Optional[DeductionsInfo] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class ForgotPasswordObject(BaseModel):
    email: Optional[str] = None
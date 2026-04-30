from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime

class PersonalInfo(BaseModel):
    title: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    alternate_email: Optional[str] = None
    phone: Optional[str] = None
    whatsapp: Optional[str] = None
    dob: Optional[str] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[int] = None
    pan: Optional[str] = None
    aadhaar: Optional[str] = None

class ProfessionalInfo(BaseModel):
    icai_number: Optional[str] = None
    membership_type: Optional[str] = None
    qualification_date: Optional[str] = None
    experience_years: Optional[str] = None
    cop_number: Optional[str] = None
    firm_name: Optional[str] = None
    firm_registration: Optional[str] = None
    office_address: Optional[str] = None
    office_city: Optional[str] = None
    office_state: Optional[str] = None
    office_pincode: Optional[str] = None
    bio: Optional[str] = None

class Specialization(BaseModel):
    primary_specialization: Optional[str] = None
    client_size: Optional[str] = None
    languages: Optional[str] = None
    additional_services: Optional[list[str]] = None
    tax_services: Optional[list[str]] = None
    industry_expertise: Optional[list[str]] = None

class Documents(BaseModel):
    icai_cert: Optional[str] = None
    cop_cert: Optional[str] = None
    pan_doc: Optional[str] = None
    aadhaar_doc: Optional[str] = None
    resume: Optional[str] = None
    photo: Optional[str] = None
    certs: Optional[str] = None

class ServiceAgreement(BaseModel):
    engagement_type: Optional[str] = None
    rate_itr_individual: Optional[str] = None
    rate_itr_business: Optional[str] = None
    rate_consultation: Optional[str] = None
    rate_gsts: Optional[str] = None
    revenue_share: Optional[str] = None
    payment_terms: Optional[str] = None
    max_clients: Optional[str] = None
    response_time: Optional[str] = None
    work_hours_from: Optional[str] = None
    work_hours_to: Optional[str] = None
    working_day: Optional[list[str]] = None
    bank_account_name: Optional[str] = None
    bank_name: Optional[str] = None
    bank_ifsc: Optional[str] = None

class CAOnboarding(BaseModel):
    ca_id: Optional[str] = None
    password: Optional[bytes] = None
    personal_info: Optional[PersonalInfo] = None
    professional_info: Optional[ProfessionalInfo] = None
    specialization: Optional[Specialization] = None
    documents: Optional[Documents] = None
    service_agreement: Optional[ServiceAgreement] = None
    status: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
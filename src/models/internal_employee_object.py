from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime, date

class LoginObject(BaseModel):
    client_id: Optional[str] = None
    employee_id: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    rbac_role: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class InternalEmployeeInfo(BaseModel):
    client_id: Optional[str] = None
    employee_id: Optional[str] = None
    employee_name: Optional[str] = None
    employee_initials: Optional[str] = None
    manager_id: Optional[str] = None
    manager_name: Optional[str] = None
    dob: Optional[str] = None
    doj: Optional[str] = None
    pan: Optional[str] = None
    aadhar: Optional[str] = None
    registered_address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[int] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    role: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime

class LoginObject(BaseModel):
    client_id: Optional[str] = None
    employee_id: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    rbac_role: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
from pydantic import BaseModel, Field
from typing import Optional

class LoginObject(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    
class SignUpObject(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    
class ForgotPasswordObject(BaseModel):
    email: Optional[str] = None
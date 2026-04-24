from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime

class DemoRequest(BaseModel):
    request_id: Optional[str] = None
    email: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    createdAt: Optional[datetime] = None
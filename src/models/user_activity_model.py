from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime

class ConversationObject(BaseModel):
    client_id: str
    employee_id: str
    query: Optional[str]
    response: Optional[str] = None
    session_id: Optional[str] = None
    conversation_id: Optional[str] = None
    message_id: Optional[str] = None
    agent: Optional[dict[str, Any]] = None
    token_count: Optional[dict[str, int]] = None
    latency_ms: Optional[int] = None
    error: Optional[str] = None
    status: Optional[str] = None
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]


class TaxCalculator(BaseModel):
    client_id: str
    employee_id: str
    session_id: str
    age: Optional[str]
    gross_income: Optional[float]
    std: Optional[float]
    d80c: Optional[float]
    d80d: Optional[float]
    hra: Optional[float]
    hl: Optional[float]
    nps: Optional[float]
    selected_regime: Optional[str]
    taxable_income: Optional[float]
    total_tax: Optional[float]
    total_deductions: Optional[float]
    tax_before_cess: Optional[float]
    cess: Optional[float]
    old_regime_tax: Optional[float]
    new_regime_tax: Optional[float] 
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]

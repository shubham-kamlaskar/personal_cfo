from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime

class ConversationObject(BaseModel):
    user_id: str
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

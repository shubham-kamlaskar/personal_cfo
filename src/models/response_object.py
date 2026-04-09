from pydantic import BaseModel, Field
from typing import Optional

class ResponseObject(BaseModel):
    query: str
    thread_id: str
    tool_name: Optional[str] = None
    tool_status: bool
    tool_call_id: Optional[str] = None
    input_tokens: int
    output_tokens: int
    total_tokens: int
    model: Optional[str] = None
    created_at: Optional[str] = None
    response: str
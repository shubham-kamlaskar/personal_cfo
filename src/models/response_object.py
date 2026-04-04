from pydantic import BaseModel, Field


class ResponseObject(BaseModel):
    query: str
    tool_name : str
    tool_status : bool
    tool_call_id : str
    input_tokens : int
    output_tokens : int
    total_tokens : int
    model : str
    created_at : str
    response : str
from pydantic import BaseModel, Field
from typing import Optional

    
class CalculateNetPayableTax(BaseModel):
    """Input schema for calculate_net_taxable_income tool."""
    total_income: Optional[float] = Field(default=None, description="Total income earned in the fiscal year")
    deductions: Optional[float] = Field(default=None, description="Total deductions applicable for the fiscal year")
    tax_regime: Optional[str] = Field(default="new", description="Tax regime applicable for the fiscal year, either 'new' or 'old'") 
class SuggestTaxSavingInvestments(BaseModel):
    query: Optional[str] = Field(default=None, description="User query for suggesting best tax saving options based on tax regime.")
    tax_regime: Optional[str] = Field(default=None, description="Tax regime applicable for the fiscal year, either 'new' or 'old'") 
    
class InternetBasedTaxResearch(BaseModel):
    query: Optional[str] = Field(default=None, description="User query for performing real time internet based research on tax and saving related queries.")
    

class KnowledgeBaseRetriever(BaseModel):
    user_query: Optional[str] = Field(description="User query related to documents available in knowledge base")
    
class HumanAgentConnection(BaseModel):
    user_query: Optional[str] = Field(description="An user request to hndover conversation to human agent or when user is not satisfied with the provided responses.")
    
class CheckComplaintStatus(BaseModel):
    complaint_no: Optional[str] = Field(description="Complaint number")
    user_query: Optional[str] = Field(description="User request for checking the complaint status")
    
class RaiseComplaintRequest(BaseModel):
    user_query: Optional[str] = Field(description="User request to raise a complaint against a issue")
    complaint: Optional[str] = Field(description="Expalination related to the complaint")
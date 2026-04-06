from pydantic import BaseModel, Field
from typing import Optional

    
class CalculateNetPayableTax(BaseModel):
    """Input schema for calculate_net_taxable_income tool."""
    total_income: Optional[float] = Field(default=None, description="Total income earned in the fiscal year")
    deductions: Optional[float] = Field(default=None, description="Total deductions applicable for the fiscal year")
    tax_regime: Optional[str] = Field(default="new", description="Tax regime applicable for the fiscal year, either 'new' or 'old'") 
class SuggestTaxSavingInvestments(BaseModel):
    query: Optional[str] = Field(default=None, description="User query for suggesting best tax saving options.")
    
class InternetBasedTaxResearch(BaseModel):
    query: Optional[str] = Field(default=None, description="User query for performing real time internet based research on tax and saving related queries.")
    

class KnowledgeBaseRetriever(BaseModel):
    embedding_model_name: str = Field(description="Name of the embedding model")
    user_query: Optional[str] = Field(description="User query related to documents available in knowledge base")
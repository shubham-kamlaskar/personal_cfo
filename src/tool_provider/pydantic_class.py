from pydantic import BaseModel, Field
from typing import Optional

class GetWeather(BaseModel):
    """Input schema for get_weather tool."""
    city: Optional[str] = Field(default=None, description="City name to get the weather for")
    
class CalculateNetTaxableIncome(BaseModel):
    """Input schema for calculate_net_taxable_income tool."""
    total_income: Optional[float] = Field(default=None, description="Total income earned in the fiscal year")
    deductions: Optional[float] = Field(default=None, description="Total deductions applicable for the fiscal year")
    
class CalculateNetPayableTax(BaseModel):
    """Input schema for calculate_net_payable_tax tool."""
    total_income: Optional[float] = Field(default=None, description="Total income earned in the fiscal year")
    deductions: Optional[float] = Field(default=None, description="Total deductions applicable for the fiscal year")
    tax_rate: Optional[float] = Field(default=None, description="Applicable tax rate in percentage for the fiscal year")
    
class SuggestTaxSavingInvestments(BaseModel):
    query: Optional[str] = Field(default=None, description="User query for suggesting best tax saving options.")
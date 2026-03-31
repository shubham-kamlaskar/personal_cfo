from langchain.tools import tool
from src.tool_provider.pydantic_class import CalculateNetPayableTax, SuggestTaxSavingInvestments
from typing import Optional
from src.util.calculation_helper import calculate_net_tax

@tool("calculate_net_payable_tax", args_schema=CalculateNetPayableTax)
def calculate_net_payable_tax(total_income: float, tax_regime: str, deductions: Optional[float] = 0) -> float:
    """Calculate net payable tax based on the total income, tax regime and deductions."""
    tax = calculate_net_tax(total_income, tax_regime, deductions)
    return f"The net payable tax for a total income of {total_income} under the {tax_regime} is {tax}."

    
@tool("suggest_tax_saving_investments", args_schema=SuggestTaxSavingInvestments)
def suggest_tax_saving_investments(query: str) -> str:
    """Suggest best tax saving investments to user for maximizing tax savings"""
    return f"""Based on your tax slab here are the same best tax saving investments you can consider:
1. ELSS
2. PPF
3. NPS
4. Tax Saving Fixed Deposits
5. ULIPs
6. Senior Citizen Savings Scheme
7. Sukanya Samriddhi Yojana."""

def calculate_tax_as_per_indian_new_regime():
    pass

def calculate_tax_as_per_indian_old_regime():
    pass

def decide_best_tax_regime_for_user():
    pass

def explain_tax_saving_options_to_user(query: str) -> str:
    pass

def future_tax_planning_for_user():
    pass

def check_any_penalties_or_interest_for_user():
    pass

    

tools = [ calculate_net_payable_tax, suggest_tax_saving_investments]
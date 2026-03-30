from langchain.tools import tool
from src.tool_provider.pydantic_class import GetWeather, CalculateNetTaxableIncome, CalculateNetPayableTax, SuggestTaxSavingInvestments

@tool("get_weather", args_schema=GetWeather)
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

def get_net_taxable_income(tax_regime: str, total_income: float, deductions: float) -> float:
    """Calculate net taxable income."""
    try:
        if tax_regime.lower() == "new regime":
            standard_deduction = 75000
            taxable_income=total_income- standard_deduction- deductions
        else:
            standard_deduction = 50000
            taxable_income = total_income - standard_deduction - deductions
        return taxable_income
    except Exception as e:
        raise Exception(f"Error in calculating taxable income: {e}")

@tool("calculate_net_taxable_income", args_schema=CalculateNetTaxableIncome)
def calculate_net_taxable_income(tax_regime: str, total_income: float, deductions: float) -> float:
    """Calculate net taxable income."""
    return get_net_taxable_income(tax_regime=tax_regime,total_income=total_income, deductions=deductions)
    
@tool("calculate_net_payable_tax", args_schema=CalculateNetPayableTax)
def calculate_net_payable_tax(age_limit: str, tax_regime: str, total_income: float, deductions: float, tax_rate: float) -> float:
    """Calculate total tax liability."""
    taxable_income = get_net_taxable_income(tax_regime=tax_regime, total_income=total_income, deductions=deductions)
    try:
        if age_limit.lower() == "Below 60 years":
            
        net_payable_tax  = taxable_income * (tax_rate/100)
        return net_payable_tax
    except Exception as e:
        raise Exception(f"Error in calculating net payable tax: {e}")
    
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

    

tools = [get_weather, calculate_net_taxable_income, calculate_net_payable_tax, suggest_tax_saving_investments]
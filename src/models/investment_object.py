from pydantic import BaseModel
from typing import Any, Optional

class Section80C(BaseModel):
    ppf: Optional[float] = None
    elss_mf: Optional[float] = None
    lic_premium: Optional[float] = None
    year5_fd: Optional[float] = None
    nsc: Optional[float] = None
    sukanya_samruddhi: Optional[float] = None
    epf: Optional[float] = None
    home_loan_principal: Optional[float] = None
    ulip: Optional[float] = None
    
class Section80D(BaseModel):
    "Health Insurance"
    self_family_health_insurance: Optional[float] = None
    parents_health_insurance: Optional[float] = None
    senior_citizen_health_insurance: Optional[float] = None
    preventive_health_checkup: Optional[float] = None
    
class Section80CCD(BaseModel):
    "National Pension Scheme"
    tier1_vol_80ccd_1b: Optional[float] = None
    tier1_employer_contribution_80ccd_2: Optional[float] = None
    
class Section24B(BaseModel):
    "Home Loan"
    self_occupied_property: Optional[float] = None
    let_out_property: Optional[float] = None
    under_construction_property: Optional[float] = None
    
class MutualFund(BaseModel):
    elss_tax_saving: Optional[float] = None
    large_cap: Optional[float] = None
    mid_cap: Optional[float] = None
    index_fund: Optional[float] = None
    debt_fund: Optional[float] = None
    
class OtherInvestments(BaseModel):
    fixed_deposit: Optional[float] = None
    education_loan_interest_80e: Optional[float] = None
    donations_80g: Optional[float] = None
    saving_account_interest: Optional[float] = None
    gold_soverign_gold_bond: Optional[float] = None
    stocks_equity: Optional[float] = None
    bonds_deventures: Optional[float] = None
    real_estate: Optional[float] = None
    cryptocurrency: Optional[float] = None

import os
from dotenv import load_dotenv
from src.database_provider.mongo_client import MongoDBClient
from src.util.calculation_helper import TaxEngine
from src.util.datetime_helper import get_current_dt_in_milliseconds_precision
load_dotenv()

mongodb_client = MongoDBClient()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME'))
tax_engine = TaxEngine()

def update_user_investments_in_db(user_info: dict, investments: dict, totals: dict, user_id: str):
    tax_info: dict = user_info.get('tax_info', {})
    tax_regime: str = tax_info.get('tax_regime', "old")
    income_info: dict = user_info.get('income_info', {})
    gross_salary: float = income_info.get('gross_salary', 0)
    existing_tax: float = tax_info.get('deductions', 0)
    section80c = {}
    section80c_new = investments.get('80c', [])
    for item in section80c_new:
        if item['name'] == "PPF":
            section80c['ppf'] = item['amount']
        if item['name'] == "LIC Premium":
            section80c['lic_premium'] = item['amount']
        if item['name'] == "ELSS Mutual Fund":
            section80c['elss_mf'] = item['amount']
        if item['name'] == "5-Year FD":
            section80c['year5_fd'] = item['amount']
        if item['name'] == "NSC":
            section80c['nsc'] = item['amount']
        if item['name'] == "Sukanya Samriddhi (SSY)":
            section80c['sukanya_samruddhi'] = item['amount']
        if item['name'] == "EPF (Employee)":
            section80c['epf'] = item['amount']
        if item['name'] == "Home Loan Principal":
            section80c['home_loan_principal'] = item['amount']
        if item['name'] == "ULIP":
            section80c['ulip'] = item['amount']
            
    section80d = {}    
    section80d_new = investments.get('80d', [])
    for item in section80d_new:
        if item['name'] == "Self & Family Health Insurance":
            section80d['self_family_health_insurance'] = item['amount']
        if item['name'] == "Parents Health Insurance":
            section80d['parents_health_insurance'] = item['amount']
        if item['name'] == "Senior Citizen Parents":
            section80d['senior_citizen_health_insurance'] = item['amount']
        if item['name'] == "Preventive Health Check-up":
            section80d['preventive_health_checkup'] = item['amount']

    section80ccd = {}
    section80ccd_new = investments.get('nps', [])
    for item in section80ccd_new:
        if item['name'] == "Tier I — Voluntary (80CCD 1B) Parents":
            section80ccd['tier1_vol_80ccd_1b'] = item['amount']
        if item['name'] == "Tier I — Employer Contribution (80CCD 2) Health Check-up":
            section80ccd['tier1_employer_contribution_80ccd_2'] = item['amount']
        
    section24b = {}            
    section24b_new = investments.get('hl', [])
    for item in section24b_new:
        if item['name'] == "Self-Occupied Property Interest":
            section24b['self_occupied_property'] = item['amount']
        if item['name'] == "Let-Out Property Interest":
            section24b['let_out_property'] = item['amount']
        if item['name'] == "Under-Construction Property":
            section24b['under_construction_property'] = item['amount']

    mutualfund = {}
    mutualfund_new = investments.get('mf', [])
    for item in mutualfund_new:
        if item['name'] == "ELSS (Tax Saving)":
            mutualfund['elss_tax_saving'] = item['amount']
        if item['name'] == "Large Cap":
            mutualfund['large_cap'] = item['amount']
        if item['name'] == "Mid Cap":
            mutualfund['mid_cap'] = item['amount']
        if item['name'] == "Index Fund":
            mutualfund['index_fund'] = item['amount']
        if item['name'] == "Debt Fund":
            mutualfund['debt_fund'] = item['amount']

    otherinvestments = {}
    otherinvestments_new = investments.get('other', [])
    for item in otherinvestments_new:
        if item['name'] == "Fixed Deposit":
            otherinvestments['fixed_deposit'] = item['amount']
        if item['name'] == "Education loan interest (24B)":
            otherinvestments['education_loan_interest_80e'] = item['amount']
        if item['name'] == "Donations (80G)":
            otherinvestments['donations_80g'] = item['amount']
        if item['name'] == "Saving Account interest":
            otherinvestments['saving_account_interest'] = item['amount']
        if item['name'] == "Gold / Sovereign Gold Bond":
            otherinvestments['gold_soverign_gold_bond'] = item['amount']
        if item['name'] == "Stocks / Equity":
            otherinvestments['stocks_equity'] = item['amount']
        if item['name'] == "Bonds / Debentures":
            otherinvestments['bonds_deventures'] = item['amount']
        if item['name'] == "Real Estate":
            otherinvestments['real_estate'] = item['amount']
        if item['name'] == "Cryptocurrency":
            otherinvestments['cryptocurrency'] = item['amount']
    
    total_deductions = totals.get('80c', 0) + totals.get('80d', 0) + totals.get('hra',0) + totals.get('nps', 0) + totals.get('hl', 0) + otherinvestments.get('education_loan_interest_80e', 0) + otherinvestments.get('saving_account_interest', 0) + otherinvestments.get('donations_80g', 0)
    old_base_tax, old_extra_cess, old_tax = tax_engine.old_regime_tax_calculation(total_income=gross_salary, deductions=total_deductions)
    new_base_tax, new_extra_cess, new_tax = tax_engine.new_regime_tax_calculation(total_income=gross_salary)
    
    if tax_regime.lower() == "old":
        selected = {
        "selected_regime": "old",
        "selected_tax": old_tax,
        "selected_extra_cess": old_extra_cess,
        "selected_base_tax": old_base_tax,
        "total_deductions": total_deductions,
        "standard_deductions": 50000,
        "taxable_income": max(0.0, gross_salary - total_deductions - 50000)
        }
        
    else:
        selected = {
        "selected_regime": "new",
        "selected_tax": new_tax,
        "selected_extra_cess": new_extra_cess,
        "selected_base_tax": new_base_tax,
        "total_deductions": 0,
        "standard_deductions": 50000,
        "taxable_income": max(0.0, gross_salary - 75000)
        }
    
    selected['potetial_saving'] = old_tax - new_tax
    
    update_data = {

        "investments_info.section80c" : section80c,
        'investments_info.total_80c': totals.get('80c'),
        "investments_info.section80d": section80d,
        'investments_info.total_80d': totals.get('80d'),
        "investments_info.section80ccd": section80ccd,
        'investments_info.total_80ccd': totals.get('nps')  ,   
        "investments_info.section24b": section24b,
        'investments_info.total_24b': totals.get('hl'),
        "investments_info.mutualfund": mutualfund,
        'investments_info.total_mf': totals.get('mf'),
        "investments_info.otherinvestments": otherinvestments,
        'investments_info.total_other': totals.get('other'),

        "tax_info.tax_regime": selected.get('selected_regime', 0),
        "tax_info.deductions": selected.get('total_deductions', 0),
        "tax_info.tax_liability": selected.get('selected_tax', 0), 
        "tax_info.potential_savings": selected.get('potetial_saving', 0), 
        "tax_info.estimated_tax_saved": existing_tax - selected.get('selected_tax', 0),

        "updatedAt": get_current_dt_in_milliseconds_precision()   
        }

    deducation_summary = {
        "80c_deduction": totals.get('80c', 0),
        "80d_health": totals.get('80d', 0),
        "nps_80ccd": totals.get('nps', 0),
        "home_loan_interest": totals.get('hl', 0),
        "education_loan_interest_80e": otherinvestments.get('education_loan_interest_80e', 0),
        "saving_account_interest": otherinvestments.get('saving_account_interest', 0),
        "donations_80g": otherinvestments.get('donations_80g', 0),
        "total_deductions": selected.get('total_deductions', 0),
        "tax_liability": selected.get('selected_tax', 0),
        "tax_saved": 0,
        "potential_savings": selected.get('potetial_saving', 0),
    }

    mongodb_client.update_one_item_in_collection(
            db_name,
            user_info_collection,
                "user_id",
                user_id,
                update_data
        )

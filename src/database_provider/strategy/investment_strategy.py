import os
from dotenv import load_dotenv
from src.database_provider.mongo_client import MongoDBClient

load_dotenv()

mongodb_client = MongoDBClient()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME')) 

def update_user_investments_in_db(investments: dict, totals: dict, user_id: str):
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


        
    update_data = {
        "investments_info": {
        "section80c" : section80c,
        'total_80c': totals.get('80c'),
        "section80d": section80d,
        'total_80d': totals.get('80d'),
        "section80ccd": section80ccd,
        'total_80ccd': totals.get('nps')  ,   
        "section24b": section24b,
        'total_24b': totals.get('hl'),
        "mutualfund": mutualfund,
        'total_mf': totals.get('mf'),
        "otherinvestments": otherinvestments,
        'total_other': totals.get('other')
        }
        }

    mongodb_client.update_one_item_in_collection(
            db_name,
            user_info_collection,
                "user_id",
                user_id,
                update_data
        )
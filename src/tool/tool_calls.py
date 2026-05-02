import os
from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool
import uuid
from langchain_community.tools import DuckDuckGoSearchResults
from src.tool.pydantic_class import (CalculateNetPayableTax, SuggestTaxSavingInvestments, InternetBasedTaxResearch, 
                                              KnowledgeBaseRetriever, HumanAgentConnection, CheckComplaintStatus, RaiseComplaintRequest)
from typing import Optional
from src.util.calculation_helper import TaxEngine
from src.embedding.ollama_embedding import get_embedding_client
from langchain_community.vectorstores import FAISS
import faiss

tax_engine = TaxEngine()

@tool("calculate_net_payable_tax", args_schema=CalculateNetPayableTax)
def calculate_net_payable_tax(total_income: float, tax_regime: str, deductions: Optional[float] = 0) -> float:
    """Calculate net payable tax based on the total income, tax regime and deductions."""
    tax = tax_engine.calculate_net_tax(total_income, tax_regime, deductions)
    return f"The net payable tax for a total income of {total_income} under the {tax_regime} is {tax}."
    
@tool("suggest_tax_saving_investments", args_schema=SuggestTaxSavingInvestments)
def suggest_tax_saving_investments(query: str, tax_regime: str) -> str:
    """Suggest best tax saving investments to user for maximizing tax savings"""

    tax_regime = tax_regime.lower()

    if tax_regime == "old":
        saving_options = """
                    Based on the Old Tax Regime, you can reduce taxable income using the following investments and deductions:

                    1. ELSS (Equity Linked Savings Scheme) - Section 80C, limit ₹1.5L
                    2. PPF (Public Provident Fund) - Section 80C, long-term tax-free returns
                    3. NPS (National Pension System) - Additional ₹50K deduction under 80CCD(1B)
                    4. Tax Saving Fixed Deposits - Section 80C with 5-year lock-in
                    5. ULIPs - Section 80C with insurance + investment benefits
                    6. Senior Citizen Savings Scheme - Good for retirees
                    7. Sukanya Samriddhi Yojana - For girl child savings
                    8. Life Insurance Premium - Eligible under Section 80C
                    9. Home Loan Principal Repayment - Section 80C
                    10. Health Insurance Premium - Section 80D deduction

                    Maximum deduction possible under 80C: ₹1.5 lakh.
                    """
    else:
        saving_options = """
                    Under the New Tax Regime, most deductions are not allowed.

                    However, you can still consider:

                    1. Employer contribution to NPS (Section 80CCD(2))
                    2. Standard deduction ₹50,000 (available automatically for salaried individuals)
                    3. Employer contribution to EPF
                    4. Some specific allowances depending on employer structure

                    Since deductions are limited in the new regime, investment decisions should focus more on wealth creation rather than tax saving.
                    """
    return saving_options

def decided_which_itr_form_need_to_filed(income_source: str, foreign_assents: Optional[str], type_of_resident: str,
                                         investment_under_80c: str, business_under_presumptive_taxation: bool):
    """This tool is used to help user decide which ITR form is best suited for him based on available information."""
    

def calculate_tax_as_per_indian_new_regime():
    pass

def calculate_tax_as_per_indian_old_regime():
    pass

def decide_best_tax_regime_for_user():
    pass

def explain_tax_saving_options_to_user(query: str):
    pass

def future_tax_planning_for_user():
    pass

def check_any_penalties_or_interest_for_user():
    pass

def form16_analyzer():
    pass

def ais_form_analyzer():
    pass

def bank_statement_analyzer():
    pass

@tool('check_complaint_status', args_schema=CheckComplaintStatus)
def check_complaint_status(complaint_no: str, user_query:str):
    """This tool is used to check current status of user complaint number."""
    status= "in-progress"
    return f"Status of your complaint number: {complaint_no} is {status}"

@tool('raise_complaint_request', args_schema=RaiseComplaintRequest)
def raise_complaint_request(user_query: str, complaint: str):
    """This tool is used to raise a complaint and in return user will get a complaint number for better tracking purpose."""
    complaint_no = "COM" +str(uuid.uuid4())
    return f"Thanks for raising a complaint for {complaint}, we will connect with you shortly. Please note your complaint number: {complaint_no}"

@tool('human_agent_connection', args_schema=HumanAgentConnection)
def human_agent_connection(user_query: str):
    """This tool is used to connect with human agent when a user is not satisfied with answer or wants to connect for other queries."""
    return "You're being connected to our human representative now. Please wait a moment while we establish the connection. Our representative will assist you with your query shortly."

@tool('internet_based_tax_research', args_schema=InternetBasedTaxResearch)
def internet_based_tax_research(query: str) -> str:
    """This tool is used to perform internet based reasearch for up-to-date information on tax laws, regulations and best practices in real time."""
    search = DuckDuckGoSearchResults(output_format="list", num_results=2)
    response = search.invoke(query)
    return response

@tool('knowledge_base_retriever', args_schema=KnowledgeBaseRetriever)
def knowledge_base_retriever(user_query: str):
    """This tool is used to retrieve responses from available knowledge base which contains glossary (meanings of income tax related terms)"""
    embedding_model_name = str(os.getenv("EMBEDDING_MODEL_NAME"))
    embedding = get_embedding_client(model_name=embedding_model_name)
    new_vector_store = FAISS.load_local(
    "faiss_index", embedding, allow_dangerous_deserialization=True
    )
    retriever = new_vector_store.as_retriever(search_type="mmr", 
                                              search_kwargs={"k": 5, "fetch_k": 20})
    response = retriever.invoke(user_query)
    return [doc.page_content for doc in response]


tools = [ calculate_net_payable_tax, suggest_tax_saving_investments, internet_based_tax_research, knowledge_base_retriever, 
         human_agent_connection, check_complaint_status, raise_complaint_request]
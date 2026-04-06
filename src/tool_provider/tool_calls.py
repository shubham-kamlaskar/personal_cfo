from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults
from src.tool_provider.pydantic_class import CalculateNetPayableTax, SuggestTaxSavingInvestments, InternetBasedTaxResearch, KnowledgeBaseRetriever
from typing import Optional
from src.util.calculation_helper import TaxEngine
from src.embedding_provider.ollama_embedding import get_embedding_client
from langchain_community.vectorstores import FAISS
import faiss

tax_engine = TaxEngine()

@tool("calculate_net_payable_tax", args_schema=CalculateNetPayableTax)
def calculate_net_payable_tax(total_income: float, tax_regime: str, deductions: Optional[float] = 0) -> float:
    """Calculate net payable tax based on the total income, tax regime and deductions."""
    tax = tax_engine.calculate_net_tax(total_income, tax_regime, deductions)
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

@tool('internet_based_tax_research', args_schema=InternetBasedTaxResearch)
def internet_based_tax_research(query: str) -> str:
    """This tool is used to perform internet based reasearch for up-to-date information on tax laws, regulations and best practices in real time."""
    search = DuckDuckGoSearchResults(output_format="list", num_results=2)
    response = search.invoke(query)
    return response

@tool('knowledge_base_retriever', args_schema=KnowledgeBaseRetriever)
def knowledge_base_retriever(embedding_model_name: str, user_query: str):
    """This tool is used to retrieve responses from available knowledge base which contains glossary, terms conditions, law and practice."""
    embedding = get_embedding_client(embedding_model_name)
    new_vector_store = FAISS.load_local(
    "faiss_index", embedding, allow_dangerous_deserialization=True
    )
    retriever = new_vector_store.as_retriever(search_type="mmr", 
                                              search_kwargs={"k": 5, "fetch_k": 20})
    response = retriever.invoke(user_query)
    return [doc.page_content for doc in response]


tools = [ calculate_net_payable_tax, suggest_tax_saving_investments, internet_based_tax_research, knowledge_base_retriever]
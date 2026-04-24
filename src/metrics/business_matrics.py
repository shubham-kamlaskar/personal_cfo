import os
from dotenv import load_dotenv

from src.database.infodb.service.mongo_client import MongoDBClient

load_dotenv()

class MatricsCalculator:
    def __init__(self):
        self.mongodb_client = MongoDBClient()
        self.db_name = os.getenv("DB_NAME")
        self.user_info_collection_name = os.getenv("USER_INFO_COLLECTION")
        
    def main_matrics_calculations(self):
        monthly_recurring_revenue = None 
        active_users = None 
        conversation_rate = None 
        monthly_churn = None 
        ltv_cac_ratio = None
        net_promotor_score = None 
        
    def acquisition_matrics(self):
        cac = None 
        organic_vs_paid_split = None
        signup_activated_ratio = None 
        traffic_source = None
        
    def revenue_and_monetization(self):
        monthly_annual_recurring_revenue = None
        average_revenue_per_user = None
        free_to_paid_conversion = None 
        cac_payback_period = None
        
    def retention_metrics(self):
        monthly_churn_rate = None
        annual_churn_rate = None 
        net_revenue_retention = None 
        year2_retention = None 
        
    def product_engagement_metrics(self):
        itr_completion_rate = None 
        ai_chat_interactions_per_User = None
        document_upload_rate = None
        regime_optimizer_usage = None

    def customer_quality_metrics(self):
        net_promoter_score = None 
        support_ticket_rate = None
        refund_notice_rate = None
        average_rating = None 

    def unit_economics(self):
        lifetime_value = None    
        ltv_cac_ratio = None
        gross_margin = None
        ca_assisted_plan_costs = None 
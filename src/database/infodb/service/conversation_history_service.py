import os
from dotenv import load_dotenv

from src.database.infodb.service.mongo_client import MongoDBClient
from src.util.app_constants import VariableConstant

load_dotenv()

class HistoryClient:
    def __init__(self):
        self.mongodb_client = MongoDBClient()

        self.db_name = str(os.getenv('DB_NAME'))
        self.conversation_collection = str(os.getenv("CONVERSATION_COLLETION"))

    def get_user_conversation_history(self, client_id: str, employee_id: str):
        filter_items = {"client_id": client_id, "employee_id": employee_id}
        user_conversation_history = self.mongodb_client.find_many_item_from_collection(
                database_name=self.db_name,
                collection_name=self.conversation_collection,
                filter_items=filter_items
            )
            
        conv_history = []

        for conv in user_conversation_history:
            conv_history.append({
                "title": conv.get("query", "New Chat"),
                "timing": conv.get("createdAt", "Just now")
            })
        
        return conv_history
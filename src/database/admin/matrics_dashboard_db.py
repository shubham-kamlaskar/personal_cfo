import os
from dotenv import load_dotenv
load_dotenv()

from src.database_provider.mongo_client import MongoDBClient

mongodb_client = MongoDBClient()
admin_db_name= os.getenv('ADMIN_DATABASE_NAME')
admin_collection_name= os.getenv("ADMIN_COLLECTION_NAME")
import os
from dotenv import load_dotenv
load_dotenv()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



class MongoDBClient:
    def __init__(self):
        self.uri = os.getenv('MONGODB_CONNECTION_STRING')
        
    def get_mongo_client(self):
        try:
            # Create a new client and connect to the server
            client = MongoClient(self.uri, server_api=ServerApi('1'))
            return client
        except Exception as e:
            raise Exception("An error occured in get_mongo_client call", str(e))
        
    def get_collection_client(self, database_name: str, collection_name: str):
        client = self.get_mongo_client()
        db = client[database_name]
        collection = db.get_collection(collection_name) 
        return collection
    
    def insert_one_item_in_collection(self, database_name: str, collection_name: str, data: dict):
        collection = self.get_collection_client(database_name, collection_name)
        collection.insert_one(data)
        
    def insert_many_item_in_collection(self, database_name: str, collection_name: str, data: list[dict]):
        collection = self.get_collection_client(database_name, collection_name)
        collection.insert_many(data)
        
    def find_one_item_from_collection(self, database_name: str, collection_name: str, search_field: str, search_item: str):
        collection = self.get_collection_client(database_name, collection_name)
        data = collection.find_one({search_field: search_item})
        return data

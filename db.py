from pymongo import MongoClient

def connect_to_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["user_management"]
    collection = db["users"]
    return collection
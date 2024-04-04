from pymongo import MongoClient

# Define your MongoDB connection parameters
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "your_database_name"

def connect_to_db():
    # Connect to the MongoDB database
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db

def add_user(username, email):
    db = connect_to_db()
    collection = db['users']  # Assuming your collection name is 'users'
    user = {"username": username, "email": email}
    collection.insert_one(user)

def get_users():
    db = connect_to_db()
    collection = db['users']
    users = collection.find({})
    return list(users)

def update_user(username, new_username, new_email):
    db = connect_to_db()
    collection = db['users']
    query = {"username": username}
    new_values = {"$set": {"username": new_username, "email": new_email}}
    collection.update_one(query, new_values)

def delete_user(username):
    db = connect_to_db()
    collection = db['users']
    query = {"username": username}
    collection.delete_one(query)

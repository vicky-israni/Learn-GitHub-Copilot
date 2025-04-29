import bcrypt
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["user_database"]
users_collection = db["users"]

def register_user(username, password):
    # Validate input
    if not username or not password:
        return "Username and password cannot be empty."
    
    if users_collection.find_one({"username": username}):
        return "Username already exists."

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Store user in MongoDB
    user_data = {
        "username": username,
        "password": hashed_password.decode('utf-8')
    }
    users_collection.insert_one(user_data)
    return "User registered successfully."

# Example usage
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    print(register_user(username, password))
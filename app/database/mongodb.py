
import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is not configured")

client = MongoClient(
    MONGODB_URI,
    server_api=ServerApi("1")
)

database = client[DATABASE_NAME]

# User collection
users_collection = database["users"]
analysis_collection = database["analysis"]

def test_connection():
    try:
        client.admin.command("ping")
        print("MongoDB connected successfully!")

    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        raise

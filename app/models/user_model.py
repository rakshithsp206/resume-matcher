
from datetime import datetime, timezone

from pymongo.errors import DuplicateKeyError

from app.database.mongodb import users_collection


# Create a unique index on email
users_collection.create_index("email", unique=True)


def create_user(name: str, email: str, hashed_password: str):
    user = {
        "name": name,
        "email": email,
        "password": hashed_password,
        "created_at": datetime.now(timezone.utc)
    }

    try:
        result = users_collection.insert_one(user)
        return str(result.inserted_id)

    except DuplicateKeyError:
        return None


def get_user_by_email(email: str):
    return users_collection.find_one({"email": email})


def get_user_by_id(user_id):
    from bson import ObjectId
    from bson.errors import InvalidId

    try:
        return users_collection.find_one({
            "_id": ObjectId(user_id)
        })
    except InvalidId:
        return None


from app.models.user_model import (
    create_user,
    get_user_by_email
)

# Temporary test data
user_id = create_user(
    name="Test User",
    email="testuser@gmail.com",
    hashed_password="temporary_hash"
)

print("Created User ID:", user_id)

user = get_user_by_email("testuser@gmail.com")

print("Retrieved User:", user)

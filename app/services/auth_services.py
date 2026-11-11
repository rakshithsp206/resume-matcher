from app.models.user_model import (
    create_user,
    get_user_by_email
)
from app.utils.security import hash_password
from datetime import datetime, timezone

def register_user(user_data):
    # Check if the user already exists
    existing_user = get_user_by_email(user_data.email)
    if existing_user:
        raise ValueError("User already exists")

    hashed_password = hash_password(user_data.password)

    # Create a new user
    user_id = create_user(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_password
    )

    if not user_id:
        raise ValueError("Failed to create user")
    
    return {
        "id": user_id,
        "name": user_data.name,
        "email": user_data.email,
        "created_at": datetime.now(timezone.utc)
    }
    
    
from app.utils.security import verify_password
from app.services.token_service import create_access_token


def login_user(user_data):

    # 1. Find user by email
    user = get_user_by_email(user_data.email)

    if not user:
        raise ValueError("Invalid email or password")

    # 2. Verify password
    is_valid = verify_password(
        user_data.password,
        user["password"]
    )

    if not is_valid:
        raise ValueError("Invalid email or password")

    # 3. Generate JWT
    access_token = create_access_token({
        "sub": str(user["_id"])
    })

    # 4. Return token
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

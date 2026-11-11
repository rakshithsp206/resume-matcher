
from fastapi import HTTPException, status

from app.services.auth_services import (
    register_user,
    login_user
)
from app.schemas.user_schema import UserCreate, UserResponse
from app.schemas.auth_schema import TokenResponse,UserLogin

def register_controller(user_data: UserCreate) -> UserResponse:

    try:
        result = register_user(user_data)
        return UserResponse(**result)

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )

def login_controller(user_data: UserLogin) -> TokenResponse:
    try:
        result = login_user(user_data)
        return TokenResponse(**result)

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )

def profile_controller(user):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "created_at": user["created_at"]
    }
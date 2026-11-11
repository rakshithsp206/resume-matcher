from fastapi import APIRouter, Depends
from app.dependencies.auth_dependency import get_current_user
from app.schemas.user_schema import UserCreate, UserResponse
from app.schemas.auth_schema import UserLogin, TokenResponse
from app.controllers.auth_controller import (register_controller, login_controller, profile_controller)

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate):
    return register_controller(user_data)

@router.post("/login", response_model=TokenResponse)
def login(user_data: UserLogin):
    return login_controller(user_data)

@router.get("/profile", response_model=UserResponse)
def get_profile(user:dict = Depends(get_current_user)):
    return profile_controller(user)
    
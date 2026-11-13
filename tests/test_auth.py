
from datetime import datetime, timezone
from unittest.mock import patch

from bson import ObjectId

from app.services.token_service import create_access_token


def test_register_user(client):
    user_id = str(ObjectId())

    with patch(
        "app.services.auth_services.get_user_by_email",
        return_value=None
    ), patch(
        "app.services.auth_services.create_user",
        return_value=user_id
    ):
        response = client.post(
            "/api/auth/register",
            json={
                "name": "Test User",
                "email": "test@example.com",
                "password": "StrongPass123"
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user_id
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"
    assert "password" not in data


def test_register_existing_user(client):
    existing_user = {
        "_id": ObjectId(),
        "name": "Test User",
        "email": "test@example.com"
    }

    with patch(
        "app.services.auth_services.get_user_by_email",
        return_value=existing_user
    ):
        response = client.post(
            "/api/auth/register",
            json={
                "name": "Test User",
                "email": "test@example.com",
                "password": "StrongPass123"
            }
        )

    assert response.status_code == 409


def test_register_invalid_data(client):
    response = client.post(
        "/api/auth/register",
        json={
            "name": "A",
            "email": "invalid-email",
            "password": "123"
        }
    )

    assert response.status_code == 422


def test_login_user(client):
    user_id = str(ObjectId())

    mock_user = {
        "_id": ObjectId(user_id),
        "name": "Test User",
        "email": "test@example.com",
        "password": "$argon2id$mocked_hash"
    }

    with patch(
        "app.services.auth_services.get_user_by_email",
        return_value=mock_user
    ), patch(
        "app.services.auth_services.verify_password",
        return_value=True
    ):
        response = client.post(
            "/api/auth/login",
            json={
                "email": "test@example.com",
                "password": "StrongPass123"
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_password(client):
    mock_user = {
        "_id": ObjectId(),
        "email": "test@example.com",
        "password": "$argon2id$mocked_hash"
    }

    with patch(
        "app.services.auth_services.get_user_by_email",
        return_value=mock_user
    ), patch(
        "app.services.auth_services.verify_password",
        return_value=False
    ):
        response = client.post(
            "/api/auth/login",
            json={
                "email": "test@example.com",
                "password": "WrongPassword123"
            }
        )

    assert response.status_code == 401


def test_login_nonexistent_user(client):
    with patch(
        "app.services.auth_services.get_user_by_email",
        return_value=None
    ):
        response = client.post(
            "/api/auth/login",
            json={
                "email": "unknown@example.com",
                "password": "StrongPass123"
            }
        )

    assert response.status_code == 401


def test_get_profile(client):
    user_id = ObjectId()

    mock_user = {
        "_id": user_id,
        "name": "Test User",
        "email": "test@example.com",
        "created_at": datetime.now(timezone.utc)
    }

    token = create_access_token({"sub": str(user_id)})

    with patch(
        "app.dependencies.auth_dependency.get_user_by_id",
        return_value=mock_user
    ):
        response = client.get(
            "/api/auth/profile",
            headers={"Authorization": f"Bearer {token}"}
        )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == str(user_id)
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"


def test_profile_without_token(client):
    response = client.get("/api/auth/profile")

    assert response.status_code == 401


from unittest.mock import MagicMock

from bson import ObjectId
from pymongo.errors import DuplicateKeyError

import app.models.user_model as user_model


def test_create_user(monkeypatch):
    mock_collection = MagicMock()
    mock_collection.insert_one.return_value.inserted_id = ObjectId()

    monkeypatch.setattr(
        user_model, "users_collection", mock_collection
    )

    user_id = user_model.create_user(
        name="Test User",
        email="test@example.com",
        hashed_password="hashed_password"
    )

    assert user_id is not None
    assert isinstance(user_id, str)

    inserted_user = mock_collection.insert_one.call_args[0][0]

    assert inserted_user["name"] == "Test User"
    assert inserted_user["email"] == "test@example.com"
    assert inserted_user["password"] == "hashed_password"
    assert "created_at" in inserted_user


def test_create_duplicate_user(monkeypatch):
    mock_collection = MagicMock()

    mock_collection.insert_one.side_effect = DuplicateKeyError(
        "Duplicate email"
    )

    monkeypatch.setattr(
        user_model, "users_collection", mock_collection
    )

    user_id = user_model.create_user(
        name="Test User",
        email="test@example.com",
        hashed_password="hashed_password"
    )

    assert user_id is None


def test_get_user_by_email(monkeypatch):
    mock_collection = MagicMock()

    expected_user = {
        "name": "Test User",
        "email": "test@example.com"
    }

    mock_collection.find_one.return_value = expected_user

    monkeypatch.setattr(
        user_model, "users_collection", mock_collection
    )

    user = user_model.get_user_by_email("test@example.com")

    assert user == expected_user

    mock_collection.find_one.assert_called_once_with({
        "email": "test@example.com"
    })


def test_get_user_by_id(monkeypatch):
    mock_collection = MagicMock()
    user_id = str(ObjectId())

    expected_user = {
        "_id": ObjectId(user_id),
        "name": "Test User"
    }

    mock_collection.find_one.return_value = expected_user

    monkeypatch.setattr(
        user_model, "users_collection", mock_collection
    )

    user = user_model.get_user_by_id(user_id)

    assert user == expected_user

    mock_collection.find_one.assert_called_once_with({
        "_id": ObjectId(user_id)
    })


def test_get_user_by_invalid_id(monkeypatch):
    mock_collection = MagicMock()

    monkeypatch.setattr(
        user_model, "users_collection", mock_collection
    )

    user = user_model.get_user_by_id("invalid_id")

    assert user is None
    mock_collection.find_one.assert_not_called()

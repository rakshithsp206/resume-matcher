
import pytest

from app.utils.security import hash_password, verify_password


def test_hash_password():
    password = "StrongPassword123"

    hashed_password = hash_password(password)

    assert hashed_password != password
    assert isinstance(hashed_password, str)
    assert len(hashed_password) > 0


def test_verify_correct_password():
    password = "StrongPassword123"

    hashed_password = hash_password(password)

    assert verify_password(password, hashed_password) is True


def test_verify_incorrect_password():
    password = "StrongPassword123"
    wrong_password = "WrongPassword123"

    hashed_password = hash_password(password)

    assert verify_password(wrong_password, hashed_password) is False


def test_same_password_generates_different_hashes():
    password = "StrongPassword123"

    hash1 = hash_password(password)
    hash2 = hash_password(password)

    # Password hashing should use a random salt.
    assert hash1 != hash2

    # Both hashes should still verify the original password.
    assert verify_password(password, hash1) is True
    assert verify_password(password, hash2) is True

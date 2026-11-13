
from datetime import timedelta

import jwt
import pytest

from app.services.token_service import (
    create_access_token,
    decode_access_token
)


def test_create_access_token():
    token = create_access_token({"sub": "user123"})

    assert isinstance(token, str)
    assert len(token) > 0


def test_decode_valid_token():
    token = create_access_token({"sub": "user123"})

    payload = decode_access_token(token)

    assert payload["sub"] == "user123"
    assert "exp" in payload
    assert "iat" in payload


def test_decode_expired_token():
    token = create_access_token(
        {"sub": "user123"},
        expires_delta=timedelta(seconds=-1)
    )

    with pytest.raises(jwt.ExpiredSignatureError):
        decode_access_token(token)


def test_decode_invalid_token():
    invalid_token = "this.is.not.a.valid.jwt"

    with pytest.raises(jwt.InvalidTokenError):
        decode_access_token(invalid_token)


def test_decode_token_without_subject():
    token = create_access_token({"user_id": "user123"})

    with pytest.raises(jwt.MissingRequiredClaimError):
        decode_access_token(token)

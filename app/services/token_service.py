
import os

import jwt
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta


load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
)

if not SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY is not configured")


def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None
) -> str:

    payload = data.copy()

    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload.update({
        "exp": expire,
        "iat": datetime.now(timezone.utc)
    })

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def decode_access_token(token: str) -> dict:

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM],
        options={
            "require": ["exp", "sub"]
        }
    )

    return payload

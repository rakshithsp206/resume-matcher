
from app.services.token_service import (
    create_access_token,
    decode_access_token
)

# Generate token
token = create_access_token({
    "sub": "user123"
})

print("Generated Token:")
print(token)

# Decode token
payload = decode_access_token(token)

print("\nDecoded Payload:")
print(payload)

# Extract user ID
user_id = payload.get("sub")

print("\nUser ID:", user_id)

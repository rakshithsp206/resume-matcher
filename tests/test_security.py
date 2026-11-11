
from app.utils.security import hash_password, verify_password

password = "mypassword123"

# Generate hash
hashed_password = hash_password(password)

print("Original password:", password)
print("Hashed password:", hashed_password)

# Verify correct password
result1 = verify_password(
    "mypassword123",
    hashed_password
)

print("Correct password:", result1)

# Verify incorrect password
result2 = verify_password(
    "wrongpassword",
    hashed_password
)

print("Incorrect password:", result2)

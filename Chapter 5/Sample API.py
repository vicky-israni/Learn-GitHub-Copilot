def register_user(username: str, email: str, password: str) -> dict:
    if not username or not email or not password:
        raise UserRegistrationError(400, "Missing required fields")
    
    if len(password) < 8:
        raise UserRegistrationError(422, "Password too short")

    if username == "admin":  
        raise UserRegistrationError(403, "Username not allowed")

    return {"user_id": 12345, "message": "Registration successful"}

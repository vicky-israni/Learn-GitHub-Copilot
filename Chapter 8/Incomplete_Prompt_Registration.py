# Create a function to handle user registration

def register_user(username, password, email):
    """
    Handles user registration by validating input and storing user details.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.
        email (str): The email address of the user.

    Returns:
        dict: A dictionary containing the registration status and message.
    """
    if not username or not password or not email:
        return {"status": "error", "message": "All fields are required."}

    if "@" not in email or "." not in email:
        return {"status": "error", "message": "Invalid email address."}

    # Simulate saving user details (e.g., to a database)
    # In a real application, you would hash the password and store it securely
    user_data = {
        "username": username,
        "password": password,  # Never store plain text passwords in production
        "email": email
    }

    # Simulated success response
    return {"status": "success", "message": "User registered successfully.", "user": user_data}
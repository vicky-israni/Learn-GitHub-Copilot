users = {
    "alice": "password123",
    "bob": "qwerty",
    "charlie": "letmein"
}

def login(username, password):
    if username in users:
        if users[username] == password:
            print("Login successful!")
        else:
            print("Incorrect password")
    else:
        print("User does not exists")

username = input("Enter your username: ")
password = input("Enter your password: ")

login(username, password)
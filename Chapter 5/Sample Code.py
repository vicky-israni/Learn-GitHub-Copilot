class User:
    def __init__(self, username):
        self.username = username
        self.state = "New"

    def register(self):
        if self.state == "New":
            self.state = "Registered"

    def verify_email(self):
        if self.state == "Registered":
            self.state = "Verified"

    def activate(self):
        if self.state == "Verified":
            self.state = "Active"

    def suspend(self):
        if self.state == "Active":
            self.state = "Suspended"

    def delete(self):
        if self.state in ["Registered", "Suspended"]:
            self.state = "Deleted"

    def login(self):
        return "Login successful" if self.state == "Active" else "Access denied"


class User:
    def __init__(self):
        self.email = ""
        self.name = ""
        self.password = ""
        self.user_ID = 0
        self.permissions = "Standard"

    def change_password(self, password):
        self.password = password

    def print_user_details(self):
        print(f"Username: {self.username}, Email: {self.email}, Password: {self.password}, User ID: {self.user_ID}, "
              f"Permissions: {self.permissions}")

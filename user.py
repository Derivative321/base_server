
class User:
    def __init__(self):
        self.email = ""
        self.name = ""
        self.password = ""
        self.user_index = 0
        self.permissions = "Standard"

    def change_password(self, password):
        self.password = password

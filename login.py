from user_creation import *
from constants import *
from terminal import start_terminal
from user import User

user = User()


def handle_login(connection, username):
    password = connection.recv(2048)
    encoded = base64.b64encode(password)
    print(f"Login Attempt from username: {username} password: {password}")
    if validate_login(username, encoded):
        connection.sendall(str.encode("success"))
        user.print_user_details()
        start_terminal(connection, user)
    else:
        print("fail")
        connection.sendall(str.encode("fail"))


def validate_login(username, encoded):
    attempts_list = []
    for row in range(2, user_database.max_row + 1):
        usernames = user_database.cell(row, USERNAME_COLUMN).value
        emails = user_database.cell(row, EMAIL_COLUMN).value
        passwords = user_database.cell(row, PASSWORD_COLUMN).value

        if (username == usernames and encoded.decode("utf-8") == passwords) \
                or (emails == username and encoded.decode("utf-8") == passwords):
            if "success" not in attempts_list:
                user.username = user_database.cell(row, USERNAME_COLUMN).value
                user.email = user_database.cell(row, EMAIL_COLUMN).value
                user.password = user_database.cell(row, PASSWORD_COLUMN).value
                user.permissions = user_database.cell(row, PERMISSIONS_COLUMN).value
                user.user_ID = user_database.cell(row, USER_ID_COLUMN).value
                attempts_list.append("success")

    if "success" in attempts_list:
        return True
    else:
        return False



from user_creation import *
from terminal import start_terminal


def handle_login(connection, username):
    password = connection.recv(2048)
    encoded = base64.b64encode(password)
    print(f"Login Attempt from username: {username} password: {password}")
    if validate_login(username, encoded):
        connection.sendall(str.encode("success"))
        start_terminal(connection)
    else:
        print("fail")
        connection.sendall(str.encode("fail"))


def validate_login(username, encoded):
    attempts_list = {}
    for row in range(2, user_database.max_row + 1):
        usernames = user_database.cell(row, 1).value
        emails = user_database.cell(row, 2).value
        passwords = user_database.cell(row, 3).value

        if (username == usernames and encoded.decode("utf-8") == passwords) \
                or (emails == username and encoded.decode("utf-8") == passwords):
            if "success" not in attempts_list:
                attempts_list["success"] = 1

    if "success" in attempts_list:
        return True
    else:
        return False



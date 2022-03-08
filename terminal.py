import base64

import user_creation
from constants import user_database, user_database_file, PASSWORD_COLUMN


def start_terminal(connection, user):
    command = ""

    while command != "quit":
        command = connection.recv(2048).decode("utf-8")
        if user.permissions == "Administrator":
            administrator_commands(connection, command, user)
        else:
            standard_user_commands(connection, command, user)


def standard_user_commands(connection, command, user):
    if command == "passwd":
        old_password = connection.recv(2048)
        encoded = base64.b64encode(old_password)
        while encoded.decode("utf-8") != user.password:
            print("test")
            connection.sendall(str.encode("invalid"))
            old_password = connection.recv(2048)
            encoded = base64.b64encode(old_password)
        else:
            print(f"{old_password}")
            connection.sendall(str.encode("valid"))
            password_data = connection.recv(2048)
            encoded = base64.b64encode(password_data)
            user_database.cell(user.user_ID, PASSWORD_COLUMN).value = encoded
            user_database_file.save("user_data_base.xlsx")
            user.password = encoded.decode("utf-8")
            print(base64.b64decode(encoded.decode("utf-8")))


def administrator_commands(connection, command, user):
    standard_user_commands(connection, command, user)
    if command == "admin":
        print("admin command")

import base64

from constants import *


def get_and_validate_username(connection):
    flag = True
    while flag:
        username = connection.recv(2048).decode("utf-8")
        print(f"Incoming Username: {username}")
        if test_value_in_database(username, USERNAME_COLUMN):
            connection.sendall(str.encode("valid"))
            user_database.cell(database_next_row, USERNAME_COLUMN).value = username
            user_database_file.save("user_data_base.xlsx")
            flag = False
        else:
            connection.sendall(str.encode("invalid"))


def get_and_validate_email(connection):
    flag = True
    while flag:
        email = connection.recv(2048).decode("utf-8")
        print(f"Incoming Email Address: {email}")
        if test_value_in_database(email, EMAIL_COLUMN):
            connection.sendall(str.encode("valid"))
            user_database.cell(database_next_row, EMAIL_COLUMN).value = email
            user_database_file.save("user_data_base.xlsx")
            flag = False
        else:
            connection.sendall(str.encode("invalid"))


def test_value_in_database(value, column):
    value_list = []
    for row in range(2, user_database.max_row + 1):
        values = user_database.cell(row, column).value
        if values not in value_list:
            value_list.append(values)

    for row in range(2, user_database.max_row + 1):
        if value not in value_list:
            return True
        else:
            return False


def get_and_validate_password(connection):
    password_data = connection.recv(2048)
    encoded = base64.b64encode(password_data)
    user_database.cell(database_next_row, PASSWORD_COLUMN).value = encoded
    user_database_file.save("user_data_base.xlsx")
    print(base64.b64decode(encoded.decode("utf-8")))


def user_creation(connection):
    print("User Creation Initiated...")

    get_and_validate_username(connection)
    get_and_validate_email(connection)
    get_and_validate_password(connection)

    user_database.cell(database_next_row, PERMISSIONS_COLUMN).value = "Standard"
    user_database.cell(database_next_row, USER_ID_COLUMN).value = user_database.max_row
    user_database_file.save("user_data_base.xlsx")

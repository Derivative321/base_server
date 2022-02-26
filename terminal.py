

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
        connection.sendall(str.encode("validate"))
        # get current password validation from client


def administrator_commands(connection, command, user):
    standard_user_commands(command, user)
    if command == "admin":
        print("admin command")

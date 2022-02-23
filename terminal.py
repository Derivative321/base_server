

def start_terminal(connection):
    user_input = ""

    while user_input != "quit":
        user_input = connection.recv(2048).decode("utf-8")
        print(user_input)

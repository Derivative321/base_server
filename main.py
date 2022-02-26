import socket
from _thread import *

from login import handle_login
from user_creation import *

server_socket = socket.socket()
host = "127.0.0.1"
port = 1234
thread_count = 0


def grand_base_controller(connection):
    username = connection.recv(2048).decode("utf-8")
    if username == "new-user":
        user_creation(connection)
    else:
        handle_login(connection, username)


def threaded_client(connection):
    while True:
        grand_base_controller(connection)


try:
    server_socket.bind((host, port))
    server_socket.listen(5)
    while True:
        client, address = server_socket.accept()
        print(f"Connected to: {address[0]} : {str(address[1])}")
        start_new_thread(threaded_client, (client,))
        thread_count += 1
        print(f"Thread Number: {str(thread_count)}")
except socket.error as e:
    print(str(e))

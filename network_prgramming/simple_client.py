import socket

client_socket = socket.socket()

client_socket.connect(("127.0.0.1", 5500))

username = input("Username: ")

client_socket.send(username.encode())

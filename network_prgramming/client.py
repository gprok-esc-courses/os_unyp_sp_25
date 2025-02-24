from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread 

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5600))

def read_from_server():
    while True:
        message_bytes = client_socket.recv(1024)
        print(message_bytes.decode('utf-8'))

th = Thread(target=read_from_server)
th.start()

username = input("Type Username: ")
client_socket.send(str.encode(username))

while True:
    message = input("Type Message: ")
    client_socket.send(str.encode(message))



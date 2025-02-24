from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread 


def client_thread(conn):
    username_bytes = conn.recv(1024)
    username = username_bytes.decode('utf-8')
    while True:
        message_bytes = conn.recv(1024)
        print(message_bytes.decode('utf-8'))
        # broadcast to clients
        for client in clients:
            new_message = username + ": " + message_bytes.decode('utf-8')
            client[0].send(str.encode(new_message))



server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5600))

server_socket.listen()
print("Server started on port 5600")

clients = []

while True:
    conn, addr = server_socket.accept()
    print("Connection from", addr)
    print(conn)
    clients.append((conn, addr))
    th = Thread(target=client_thread, args=(conn,))
    th.start()

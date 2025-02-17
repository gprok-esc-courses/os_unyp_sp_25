import socket 

server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 5500))

server_socket.listen()
print("Server started on port 5500")

while True:
    conn, addr = server_socket.accept()
    print("Connection from ", addr)

    username_bytes = conn.recv(1024)
    print(username_bytes.decode('utf-8'))
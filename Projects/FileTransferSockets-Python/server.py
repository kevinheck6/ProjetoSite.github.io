import os
import socket
from os import listdir
from os.path import isfile, join

# Initialize Socket Instance
server = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 8800
host = ''

# binding to the host and port, that`s what define it as a server
server.bind((host, port))

# Accepts up to 10 connections
server.listen(10)
print('Socket is listening...')

while True:
    # Establish connection with the clients.
    client, addr = server.accept()
    print('Connected with ', addr)

    # Files names
    file_names = [f for f in listdir("files") if isfile(join("files", f))]

    # convert it to string, encode it and send it to the Receiver
    client.send(str(file_names).encode())  # 1 Sending

    # Get data from the client
    data = client.recv(1024).decode()  # 1 Received
    path = "files/" + data
    print(data)

    # Send file size to client
    client.send(str(os.path.getsize(path)).encode())  # 2 Sending ----

    done = False
    i = 1
    while not done:
        if i == 1:
            done = client.recv(1024).decode()  # Received 2 4 5
        print(done)
        data = client.recv(1024).decode()  # Received 3 5
        path = "files/" + data
        client.send(str(os.path.getsize(path)).encode())  # 3 Sent
        done = client.recv(1024).decode()  # Received 4
        i = 1
        if done == 'False':
            i = 2

    # Get data from the client
    data = client.recv(1024).decode()  # 5 Received after loop
    path = "files/" + data
    print(data)

    # Read File in binary
    file = open(path, 'rb')
    line = file.read(1024)

    # Keep sending data to the client
    while line:
        client.send(line)  # 3 Sending

        line = file.read(1024)

    file.close()
    print('File has been transferred successfully.')

    client.close()

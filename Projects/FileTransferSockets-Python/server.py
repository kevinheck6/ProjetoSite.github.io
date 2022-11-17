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




    def transfer():
        print(file_names)
        client.send(str(file_names).encode())  # 1 Sending 2
        data = client.recv(1024).decode()  # 1 Received 3
        path = "files/" + data
        print(data)
        client.send(str(os.path.getsize(path)).encode())  # 2 Sending 3
        return path


    done = False
    while not done:
        path = transfer()
        done = client.recv(1024).decode()  # Received 2
        print(done)

    print("it should not be possible")


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

import socket
from os import listdir
from os.path import isfile, join

# Initialize Socket Instance

server = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 8800
host = ''

# binding to the host and port
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
    client.send(str(file_names).encode())
    # Get data from the client
    data = client.recv(1024).decode()
    path = "files/" + data
    print(data)
    # Read File in binary
    file = open(path, 'rb')
    line = file.read(1024)
    # Keep sending data to the client
    while (line):
        client.send(line)
        line = file.read(1024)

    file.close()
    print('File has been transferred successfully.')

    client.close()

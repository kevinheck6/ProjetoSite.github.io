import socket

# Initialize Socket Instance
server = socket.socket()
print ("Socket created successfully.")

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

    # Get data from the client
    data = client.recv(1024)
    print(data.decode())
    # Read File in binary
    file = open('server-file.txt', 'rb')
    line = file.read(1024)
    # Keep sending data to the client
    while(line):
        client.send(line)
        line = file.read(1024)
    
    file.close()
    print('File has been transferred successfully.')

    client.close()
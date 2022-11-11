import socket

# Initialize Socket Instance
server = socket.socket()
print ("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# Connect socket to the host and port
server.connect((host, port))
print('Connection Established.')
# Send a greeting to the server
server.send('A message from the client'.encode())

# Write File in binary
file = open('client-file.txt', 'wb')

# Keep receiving data from the server
line = server.recv(1024)

while(line):
    file.write(line)
    line = server.recv(1024)

print('File has been received successfully.')

file.close()
server.close()
print('Connection Closed.')
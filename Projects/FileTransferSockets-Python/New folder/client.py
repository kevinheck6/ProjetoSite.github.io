import socket

# Initialize Socket Instance
server = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# Connect socket to the host and port
server.connect((host, port))
print('Connection Established.')

# Receiving data from server
data = server.recv(1024).decode('utf-8')
print(f"The files that u can download are: {data}, which one would you like to download?")
data = input('')

# Sending data to the server
server.send(dl_file.encode())

<<<<<<< Updated upstream:Projects/FileTransferSockets-Python/New folder/client.py
=======
# Receiving data size from server
file_size = server.recv(1024).decode('utf-8')
print(f"The size of the file is: {file_size} bytes")


>>>>>>> Stashed changes:Projects/FileTransferSockets-Python/client.py
# Write File in binary
file = open(dl_file, 'wb')

# Keep receiving data from the server
line = server.recv(1024)

while (line):
    file.write(line)
    line = server.recv(1024)

print('File has been received successfully.')

file.close()
server.close()
print('Connection Closed.')

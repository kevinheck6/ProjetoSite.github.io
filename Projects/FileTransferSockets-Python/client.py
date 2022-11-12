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
dl_file = input('')

# Sending data to the server
server.send(data.encode())

# Receiving data size from server
file_size = server.recv(1024).decode('utf-8')
print(f"The size of the file is: {file_size} bytes")

# confirmation
done = False
while not done:
    print(f"Are you sure you want to download it? Type 'y' to download or 'n' to  exit")
    confirmation = input('')
    if confirmation == 'y':
        server.send(data.encode())
        done = True

    elif confirmation == 'n':
        print(f"The files that u can download are: {data}, which one would you like to download?")
        dl_file = input('')

    #### FAZER WHILE NISSO ENQUANTO CONFIRMATION NAO FOR DIFERENTE DE Y FAZER TAL PERGUNTA
server.send(data.encode())

# Write File in binary
file = open(data, 'wb')

# Keep receiving data from the server
line = server.recv(1024)

while line:
    file.write(line)
    line = server.recv(1024)

print('File has been received successfully.')

file.close()
server.close()
print('Connection Closed.')

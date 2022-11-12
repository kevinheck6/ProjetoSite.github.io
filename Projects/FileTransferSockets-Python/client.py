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
file_names = server.recv(1024).decode('utf-8')  # 1 Received
print(f"The files that u can download are: {file_names}, which one would you like to download?")
dl_file = input('')

# Sending data to the server
server.send(dl_file.encode())  # 1 Sent

# Receiving data size from server
file_size = server.recv(1024).decode('utf-8')  # 2 Received ----
print(f"The size of the file is: {file_size} bytes")

# confirmation
done = False
first_response = True
while not done:
    if not first_response:
        server.send(str(done).encode())  # Sent 2 4
        server.send(dl_file.encode())  # sent 3 5
        file_size = server.recv(1024).decode('utf-8')  # 3 Received
        print(f"The size of the file is: {file_size} bytes")
    print(f"Are you sure you want to download it? Type 'y' to download or 'n' to  exit")
    confirmation = input('')
    if confirmation == 'y':
        done = True
        server.send(str(done).encode())  # 2 Sent 4
        server.send(dl_file.encode())  # 3 Sent 5

    elif confirmation == 'n':
        print(f"The files that u can download are: {file_names}, which one would you like to download?")
        dl_file = input('')
        first_response = False

    #### FAZER WHILE NISSO ENQUANTO CONFIRMATION NAO FOR DIFERENTE DE Y FAZER TAL PERGUNTA

# Write File in binary
file = open(dl_file, 'wb')

# Keep receiving data from the server
line = server.recv(1024)  # 3 received

while line:
    file.write(line)
    line = server.recv(1024)

print('File has been received successfully.')

file.close()
server.close()
print('Connection Closed.')

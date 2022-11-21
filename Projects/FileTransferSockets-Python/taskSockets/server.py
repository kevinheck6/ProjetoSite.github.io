import os
import random
import socket
from os import listdir
from os.path import isfile, join


def random_function(type):
    if type in ["energy", "humidity"]:
        number = random.randrange(0, 100, 3)

    elif type == "temp":
        number = random.randrange(-55, 150, 2)

    else:
        number = bool(random.getrandbits(1))

    print(number)
    return number


def check_commands():
    command = client.recv(1024).decode()
    if command == "alarm_tick":
        # print(str(random_function("energ")))
        client.send(str(random_function("temp")).encode())
        client.send(str(random_function("energy")).encode())
        client.send(str(random_function("humidity")).encode())
        #client.send(str(random_function("people")).encode())
        #client.send(str(random_function("door")).encode())
        check_commands()
    if command == "close":
        client.close()


# Initialize Socket Instance
server = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 8800
host = ''

# binding to the host and port, that`s what define it as a server
server.bind((host, port))

# Accepts up to 100 connections
server.listen()
print('Socket is listening...')

while True:
    # Establish connection with the clients.
    client, addr = server.accept()
    print('Connected with ', addr)

    check_commands()
    client.close()

    # # Files names
    # file_names = [f for f in listdir("files") if isfile(join("files", f))]
    #
    # done = "False"
    # while done == "False":
    #     path = transfer()  # getting the final path from function
    #     done = client.recv(1024).decode()  # getting the verification that the loop is over
    #     print(done)

    # Read File in binary
    # file = open(path, 'rb')
    # line = file.read(1024)

    # Keep sending data to the client
    # while line:
    #     client.send(line)  # 3 Sending
    #
    #     line = file.read(1024)
    #
    # file.close()
    # print('File has been transferred successfully.')

# def transfer():
#     print(file_names)
#     client.send(str(file_names).encode())  # server is sending file names
#     data = client.recv(1024).decode()  # server is receiving the file name that he should send back
#     path = "files/" + data
#     print(data)
#     client.send(str(os.path.getsize(path)).encode())  # sending the file size
#     return path

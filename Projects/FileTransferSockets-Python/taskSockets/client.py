import socket
import threading


# def transfer():
#     file_names = server.recv(1024).decode('utf-8')  # getting files names from server
#     print(f"The files that u can download are: {file_names}, which one would you like to download?")
#     dl_file = input('')  # choosing file
#     server.send(dl_file.encode())  # # sending name that should be downloaded
#     file_size = server.recv(1024).decode('utf-8')  # getting file size from server
#     print(f"The size of the file is: {file_size} bytes")
#     print(f"Are you sure you want to download it? Type 'y' to download or 'n' to  exit")
#     return dl_file


def check_limits(value, type):
    temp_limit = 80
    energy_limit = 10
    humidity_limit = 20

    if type == "temp":
        if value > temp_limit:
            print(f"Throw water in the system!! The temperature is equal to {value}! It's on fire!")
    elif type == "humidity":
        if value > humidity_limit:
            print(f"You threw too much water!! The humidity is equal to"
                  f" {value}%! You want the electric system to blow?!?")
    elif type == "energy":
        if value < energy_limit:
            print(f"We are almost out of energy! We only have {value}% left! Do something!!")

    elif type == "change_temperature":
        temp_limit = value
    elif type == "change_energy_limit":
        energy_limit = value
    elif type == "change_humidity_limit":
        humidity = value

    else:  # Error case
        print("There is no command with such name")


def send_tick():
    alarm_tick = "alarm_tick"
    server.send(str(alarm_tick).encode())  # sending alarm tick to server

    # print((server.recv(1024).decode()))
    check_limits(float(server.recv(1024).decode()), "temp")  # checking the temperature
    check_limits(float(server.recv(1024).decode()), "energy")  # checking the energy
    check_limits(float(server.recv(1024).decode()), "humidity")  # checking the humidity
    # check_limits(server.recv(1024), "people")  # checking the people
    # check_limits(server.recv(1024), "door")  # checking the door


def threading_alarm():
    threading.Timer(5.0, threading_alarm).start()
    send_tick()
    print("tick funfando")


server = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# Connect socket to the host and port
server.connect((host, port))
print('Connection Established.')

# threading_alarm()
send_tick()

# done = "False"
# while done == "False":
#     dl_file = transfer()  # getting the name of the file that should be downloaded
#     confirmation = input('')  # confirmation that we should end the loop
#     if confirmation == 'y':
#         done = "True"
#         server.send(str(done).encode())  # 2 sent 4
#         break
#     elif confirmation == 'n':
#         done = "False"
#         server.send(str(done).encode())  # 2 sent 4
#
# # Write File in binary
# file = open(dl_file, 'wb')
#
# # Keep receiving data from the server
# line = server.recv(1024)  # 3 received
#
# while line:
#     file.write(line)
#     line = server.recv(1024)
#
# print('File has been received successfully.')
#
# file.close()
server.close()
print('Connection Closed.')

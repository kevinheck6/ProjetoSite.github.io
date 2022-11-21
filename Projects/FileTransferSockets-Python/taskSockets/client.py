import socket
import sched
import time
import select
import sys

# def transfer():
#     file_names = server.recv(1024).decode('utf-8')  # getting files names from server
#     print(f"The files that u can download are: {file_names}, which one would you like to download?")
#     dl_file = input('')  # choosing file
#     server.send(dl_file.encode())  # # sending name that should be downloaded
#     file_size = server.recv(1024).decode('utf-8')  # getting file size from server
#     print(f"The size of the file is: {file_size} bytes")
#     print(f"Are you sure you want to download it? Type 'y' to download or 'n' to  exit")
#     return dl_file


i = 0


def check_limits(value, type):
    temp_limit = 80
    energy_limit = 10
    humidity_limit = 20

    if type == "temp":
        if int(value) > temp_limit:
            print(f"Throw water in the system!! The temperature is equal to {value}! It's on fire!")
    elif type == "humidity":
        if int(value) > humidity_limit:
            print(f"You threw too much water!! The humidity is equal to"
                  f" {value}%! You want the electric system to blow?!?")
    elif type == "energy":
        if int(value) < energy_limit:
            print(f"We are almost out of energy! We only have {value}% left! Do something!!")

    elif type == "change_temperature":
        temp_limit = value
    elif type == "change_energy_limit":
        energy_limit = value
    elif type == "change_humidity_limit":
        humidity = value

    elif type == "people":
        if value == "False":
            print(f"There are no People taking care of the system!")

    elif type == "door":
        if value == "False":
            print(f"There are no doors open in the system!")

    else:  # Error case
        print("There is no command with such name")


def send_tick():
    global i
    i = i + 1
    print("Report number: " + str(i))
    print(time.ctime())
    alarm_tick = "alarm_tick"
    server.send(str(alarm_tick).encode())  # sending alarm tick to server

    info = server.recv(1024).decode()
    temp, energy, humidity, people, door = info.split(' ')
    check_limits(temp, "temp")
    check_limits(energy, "energy")
    check_limits(humidity, "humidity")
    check_limits(people, "people")
    check_limits(door, "door")


def do_something(sc):
    print("###################################################################")
    print("###################################################################")
    print("   Getting information from the database     ")
    # do your stuff
    send_tick()

    #
    sc.enter(2, 1, do_something, (sc,))


# def timeout_input(timeout, prompt="", timeout_value=None):
#     sys.stdout.write(prompt)
#     sys.stdout.flush()
#     ready, _, _ = select.select([sys.stdin], [], [], timeout)
#     if ready:
#         return sys.stdin.readline().rstrip('\n')
#     else:
#         sys.stdout.write('\n')
#         sys.stdout.flush()
#         return timeout_value


server = socket.socket()

print("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# Connect socket to the host and port
server.connect((host, port))
print('Connection Established.')

s = sched.scheduler(time.time, time.sleep)

s.enter(5, 1, do_something, (s,))
s.run()


server.close()
print('Connection Closed.')

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


# netstat -ano | findstr :8800
# taskkill /PID 17736 /F

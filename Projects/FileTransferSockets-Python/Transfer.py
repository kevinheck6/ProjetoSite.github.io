import os
import socket
from os import listdir
from os.path import isfile, join

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Internet Socket TCP socket
client.connect(("localhost", 9999))  # Can be any port number that`s free

onlyfiles = [f for f in listdir("files") if isfile(join("files", f))]  # check for files names
data = str(onlyfiles).encode()  # convert it to string and encode it
client.send(data)  # send it to the Receiver

file = open("files/images.png", "rb")  # File reading in bytes mode
file_size = os.path.getsize("files/images.png")  # Get the size of the file

client.send("files/received_images.png".encode())  # Send the file name
client.send(str(file_size).encode())  # Send the file size

data = file.read()  # sending all the data
client.sendall(data)
client.send(b"<END>")  # So we know when the file end and everything after is a new file

file.close()
client.close()

import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Internet Socket TCP socket 
client.connect(("localhost", 9999)) # Can be any port number that`s free

file = open("file.txt", "rb") # File reading in bytes mode 
file_size = os.path.getsize("file.txt")# Get the size of the file

client.send("received_file.txt".encode()) # Send the file name 
client.send(str(file_size).encode()) # Send the file size

data = file.read() #sending all the data 
client.sendall(data)
client.send(b"<END>") # So we know when the file end and everthing after is a new file

file.close() 
client.close()
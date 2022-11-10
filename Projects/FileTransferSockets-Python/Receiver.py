import socket
import tqdm

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999)) #when we have a server we bind, when we have a client we connect
server.listen()

#we can use a loop here if we want to send more files 
client, addr = server.accept()

file_name = client.recv(1024).decode()
print(file_name)
file_size = client.recv(1024).decode()
print(file_size)

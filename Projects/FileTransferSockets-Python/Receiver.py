import socket
import tqdm

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))  # when we have a server we bind, when we have a client we connect
server.listen()

# we can use a loop here if we want to send more files
client, addr = server.accept()

print(f"connected to {addr}")
data = client.recv(1024).decode('utf-8')
print(f"The files that u can download are: {data}, which one would you like to download?")


file_name = client.recv(1024).decode()
print(file_name)
file_size = client.recv(1024).decode()
print(file_size)

file = open(file_name, "wb")

file_bytes = b""

done = False

progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))  # progress bar

while not done:  # Check if it`s finished
    data = client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes += data

    progress.update(1024)

file.write(file_bytes)

file.close()
client.close()
server.close()

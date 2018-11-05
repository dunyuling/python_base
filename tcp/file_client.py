import socket

client = socket.socket()
ip_port = ("localhost",8000)
client.connect(ip_port)

with open("socket_client.py","rb") as f:
    for i in f:
        client.send(i)
        data = client.recv(1024)
        # if data == b'success':
        #     continue
    client.send("quit".encode())

client.close()
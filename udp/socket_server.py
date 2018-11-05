import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ("localhost",8000)
server.bind(ip_port)

while True:
    data = server.recv(1024)
    print(data.decode())


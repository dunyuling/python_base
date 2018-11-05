import socket

server = socket.socket()
ip_port = ("localhost",8000)
server.bind(ip_port)
server.listen(5)

while True:
    client,addr = server.accept()
    while True:
        with open("file","ab") as f:
            data = client.recv(1024)
            if data == b'quit':
                break
            f.write(data)
            client.send("success".encode())

    print("接收数据完成")
    client.send("success".encode())


server.close()
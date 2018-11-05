import socket
import random

server = socket.socket()

ip_port = ("localhost", 8000)
server.bind(ip_port)
print(server)
print(socket.socket)
server.listen(5)

while True:
    print("正在等待接收数据...")
    client,addr = server.accept()
    print(client,addr)
    msg = "连接成功"
    client.send(msg.encode())
    while True:
        data = client.recv(1024)
        print(data.decode())
        if data == b'exit':
            break
        client.send(data)
        # client.send(str(random.randint(1,100)).encode())

    client.close()
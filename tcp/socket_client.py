import socket

client = socket.socket()
ip_port = ("127.0.0.1", 8000)
client.connect(ip_port)

while True:
    data = client.recv(1024)
    print(data.decode())

    msg_input = input("请输入您要发送的信息:")
    client.send(msg_input.encode())
    if msg_input == 'exit':
        break

    #TODO 若发送两条消息,可能被合并成一条,但是服务器端当作一条解析,从而导致了客户端与服务器端的不一致
    # data = client.recv(1024)
    # print(data.decode())
client.close()
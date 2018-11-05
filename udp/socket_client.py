import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ("localhost",8000)

while True:
    msg_input = input("请输入需要发送的消息:")
    if msg_input == 'exit':
        break
    client.sendto(msg_input.encode(),ip_port)

client.close()
import socketserver
import random

class MyServer(socketserver.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        conn = self.request
        msg = "hello world"
        conn.send(msg.encode())

        while True:
            data = conn.recv(1024)
            print(data.decode())
            if data == b'exit':
                break

            conn.send(data)
            # conn.send(str(random.randint(1,1000)).encode())

        # conn.close()


    def finish(self):
        pass

if __name__ == '__main__':
    ip_port = ("127.0.0.1",8000)
    server = socketserver.ThreadingTCPServer(ip_port,MyServer)

    server.serve_forever()
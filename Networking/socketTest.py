from socket import socket, AF_INET, SOCK_DGRAM

class socketTest:

    def __init__(self):
        self.UDP_IP = "127.0.0.1"
        self.UDP_PORT = 5005
        self.m = "Hello World!"

        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.sendto(self.m,  (self.UDP_IP, self.UDP_PORT))


if __name__ == "__main__":
    s = socketTest()

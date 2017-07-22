from socket import socket, AF_INET, SOCK_DGRAM

class socketRecTest:

    def __init__(self):

        self.UDP_IP = "127.0.0.1"
        self.UDP_PORT = 5005
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.bind((self.UDP_IP, self.UDP_PORT))

        while True:
            data, addr = self.sock.recvfrom(1024)
            print "message:", data
        


if __name__ == "__main__":
    s = socketRecTest()

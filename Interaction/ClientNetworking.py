import socket

class ServerNetworking:
    def __init__(self):
        self.host = "localhost"
        self.port = 6669
        socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket.bind((host, port))
        socket.listen(1)
        

    
if __name__ == "__main__":
    pass

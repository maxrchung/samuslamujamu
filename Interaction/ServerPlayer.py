class ServerPlayer:
    def __init__(self, uid, name, ip, port):
        self.uid = uid
        self.name = name
        self.ip = ip
        self.port = port
        self.game = None
        self.character = None

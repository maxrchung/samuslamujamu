import PlayerState

class ServerPlayer:
    def __init__(self, uid, name, ip, port, nextAlive):
        self.uid = uid
        self.name = name
        self.ip = ip
        self.port = port
        self.game = None
        self.character = None
        self.nextAlive = nextAlive
        self.state = PlayerState.none

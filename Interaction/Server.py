from Queue import Queue
from ServerCharacter import *
import ServerGame
from ServerPlayer import *
import PacketCommand
import pickle
from Queue import Queue
import socket
import threading

class Server:
    def __init__(self):
        self.inputManagers = []
        # Keyed by ip instead of ID
        # Everything else is keyed by ID
        self.players  = {}
        self.games = {}
        self.matchMaking = Queue()

        self.playerID = 0
        self.gameID = 0
        self.characterID = 0

        self.running = True

	self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	self.sock.bind(("192.168.0.106", 6669))

        self.lock = threading.Lock()
        self.packets = Queue()
        self.networkingThread = threading.Thread(target=self.networking)
        self.networkingThread.daemon = True
        self.networkingThread.start()

        print "Server started"

    def networking(self):
        while self.running:
	    data, addr = self.sock.recvfrom(1024)
            unpickled = pickle.loads(data)
            self.lock.acquire()
	    self.packets.put((unpickled,addr))
            self.lock.release()
        
    def getPlayerID(self):
        self.playerID += 1
        return self.playerID

    def getGameID(self):
        self.gameID += 1
        return self.gameID

    def getCharacterID(self):
        self.characterID += 1
        return self.characterID

    def createPlayer(self, name, ip, port):
        self.player = ServerPlayer(self.getPlayerID(), name, ip, port)
        self.players[self.player.ip] = self.player
        return self.player

    def associatePlayer(self, player, game, character):
        player.character = character
        player.game = game
        character.player = player
        
    def associateGame(self, game, characters):
        game.characters = characters
        for charID, character in characters.items():
            character.game = game
    
    def createGame(self, player1, player2):
        game = ServerGame.ServerGame(self, self.getGameID())
        self.games[game.uid] = game
        
        topPos = [ServerGame.width / 2, 100]
        botPos = [ServerGame.width / 2, ServerGame.height - 100]
        character1 = ServerCharacter(self.getCharacterID(), topPos, player1.name)
        character2 = ServerCharacter(self.getCharacterID(), botPos, player2.name)
        characters = {
            character1.uid: character1,
            character2.uid: character2
        }

        self.associatePlayer(player1, game, character1)
        self.associatePlayer(player2, game, character2)
        
        self.associateGame(game, characters)
        return game
    
    def run(self):
        while self.running:
            while not self.packets.empty() > 0: 
                self.lock.acquire()
                packet = self.packets.get()
                self.lock.release()
                
                command, data = packet[0]
                ip, port = packet[1]

                if command == PacketCommand.name:
                    player = self.createPlayer(data, ip, port)
                    self.matchMaking.put(player)
                    print "Added", ip, "to matchmaking"
                    
                elif command == PacketCommand.inputManager:
                    if ip in self.players:
                        player = self.players[ip]
                        player.character.inputManager = data

            while self.matchMaking.qsize() >= 2:
                player1 = self.matchMaking.get()
                player2 = self.matchMaking.get()
                game = self.createGame(player1, player2)
                print "Game", game.uid, "created"

                gameState = game.getGameState()
                self.sendPacket(PacketCommand.gameStart, [gameState, player1.uid], player1)
                self.sendPacket(PacketCommand.gameStart, [gameState, player2.uid], player2)

            for gameID, game in self.games.items():
                game.run()

    def sendPacket(self, command, data, player):
        pickled = pickle.dumps([command, data])
        self.sock.sendto(pickled, (player.ip, player.port))

if __name__ == "__main__":
    server = Server()
    server.run()

from ClientGame import *
import ClientState
from EventManager import *
from InputManager import *
import PacketCommand
import pickle
import pygame
from pygame.locals import *
from Queue import Queue
import socket
import threading

class Client:
    def __init__(self):
        self.eventManager = EventManager()
        self.running = True

        self.uid = 0
        
        self.game = None
        self.state = ClientState.chooseName
        self.inputManager = InputManager()
        self.gameState = None
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverHost = "192.168.0.106"
        self.serverPort = 6669
        self.clientHost = "192.168.0.106"
        self.clientPort = 5002
        self.sock.bind((self.clientHost, self.clientPort))

        self.lock = threading.Lock()
        self.packets = Queue()
        self.networkingThread = threading.Thread(target=self.networking)
        self.networkingThread.daemon = True
        self.networkingThread.start()

        print "Client started"

    def networking(self):
        while self.running:
            #Receiving Messages from the Server
	    data, addr = self.sock.recvfrom(1024)
            unpickled = pickle.loads(data)
            self.lock.acquire()
	    self.packets.put((unpickled,addr))
            self.lock.release()
        
    def getInput(self):
        self.inputManager.clear()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.inputManager.moveUp = True

        if keys[pygame.K_a]:
            self.inputManager.moveLeft = True
            
        if keys[pygame.K_s]:
            self.inputManager.moveDown = True

        if keys[pygame.K_d]:
            self.inputManager.moveRight = True

        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            self.inputManager.mainAbility = True
            
        self.inputManager.mousePos = pygame.mouse.get_pos()

        self.sendPacket(PacketCommand.inputManager, self.inputManager)

    def run(self):
        while self.running:
            while not self.packets.empty() > 0: 
                self.lock.acquire()
                packet = self.packets.get()
                self.lock.release()

                command, data = packet[0]
                ip, port = packet[1]

                if command == PacketCommand.gameStart:
                    self.state = ClientState.game
                    self.game = ClientGame(self)
                    self.gameState = data[0]
                    self.uid = data[1]
                elif command == PacketCommand.gameState:
                    self.gameState = data
                    
            if self.state == ClientState.chooseName:
                data = str(raw_input("Enter a name: "))
                self.sendPacket(PacketCommand.name, data)
                self.state = ClientState.matchMaking
                print "Waiting for game..."
            elif self.state == ClientState.matchMaking:
                pass
            elif self.state == ClientState.game:
                self.eventManager.update()
                self.getInput()
                self.game.update(self.gameState)
                self.game.draw()

    def sendPacket(self, command, data):
        pickled = pickle.dumps([command, data])
        self.sock.sendto(pickled, (self.serverHost, self.serverPort))
                    
if __name__ == "__main__":
    client = Client()
    client.run()

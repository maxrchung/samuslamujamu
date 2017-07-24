from Client import *
from Server import *
import pygame
from pygame.locals import *

pygame.init()

server = Server()
client = Client()

while True:
    server.run()
    client.run()

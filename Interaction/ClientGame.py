from ClientBullet import *
from ClientCharacter import *
import pygame
import ServerGame
import time

class ClientGame:
    def __init__(self):
        self.windowSize = ServerGame.windowSize
        self.display = pygame.display.set_mode(self.windowSize, pygame.DOUBLEBUF)
        self.bgColor = pygame.Color(100,100,100,255)
        self.frameRate = 1 / 60.0
        self.nextUpdate = 0

        self.characters = {}
        self.bullets = {}

    def run(self, gameState):
        now = time.time()
        if now - self.nextUpdate > self.frameRate:
            self.nextUpdate = now
            self.update(gameState)
            self.draw()
        
    def update(self, gameState):
        self.characters.clear()
        for charID, schar in gameState.characters.items():
            self.characters[charID] = ClientCharacter(self)
            self.characters[charID].pos = schar.pos
            self.characters[charID].rect = schar.rect

        self.bullets.clear()
        for bulletID, bullet in gameState.bullets.items():
            self.bullets[bulletID] = ClientBullet(self)
            self.bullets[bulletID].pos = bullet.pos
            self.bullets[bulletID].rect = bullet.rect

    def draw(self):
        self.display.fill(self.bgColor)
        for charID, character in self.characters.items():
            character.draw()
        for bulletID, bullet in self.bullets.items():
            bullet.draw()
        pygame.display.flip()

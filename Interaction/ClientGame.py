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

    def run(self, gameState):
        now = time.time()
        if now - self.nextUpdate > self.frameRate:
            self.nextUpdate = now
            self.update(gameState)
            self.draw()
        
    def update(self, gameState):
        if len(self.characters) != len(gameState.characters):
            self.characters.clear()
            for charID in gameState.characters:
                self.characters[charID] = ClientCharacter(self)
                
        for charID, schar in gameState.characters.items():
            self.characters[charID].pos = schar.pos
            self.characters[charID].rect = schar.rect

    def draw(self):
        self.display.fill(self.bgColor)
        for charID, character in self.characters.items():
            character.draw()
        pygame.display.flip()

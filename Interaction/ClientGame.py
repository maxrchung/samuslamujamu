from ClientProjectile import *
from ClientCharacter import *
import pygame
import ServerGame
import time

class ClientGame:
    def __init__(self, client):
        self.client = client
        self.windowSize = ServerGame.windowSize
        self.display = pygame.display.set_mode(self.windowSize, pygame.DOUBLEBUF)
        self.bgColor = pygame.Color(100,100,100,255)
        self.frameRate = 1 / 60.0
        self.nextUpdate = 0

        self.characters = []
        self.projectiles = []

    def run(self, gameState):
        now = time.time()
        if now - self.nextUpdate > self.frameRate:
            self.nextUpdate = now
            self.update(gameState)
            self.draw()
        
    def update(self, gameState):
        self.characters = []
        for playerID, rect, health in gameState.charRects:
            character = None
            if self.client.uid == playerID:
                character = ClientCharacter(self, True, rect, health)
            else:
                character = ClientCharacter(self, False, rect, health)
            self.characters.append(character)

        self.projectiles = []
        for playerID, rect in gameState.projectileRects:
            projectile = None
            if self.client.uid == playerID:
                projectile = ClientProjectile(self, True, rect)
            else:
                projectile = ClientProjectile(self, False, rect)
            self.projectiles.append(projectile)

    def draw(self):
        self.display.fill(self.bgColor)
        for character in self.characters:
            character.draw()
        for projectile in self.projectiles:
            projectile.draw()
        pygame.display.flip()

from ClientProjectile import *
from ClientCharacter import *
import ClientState
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

        self.characters = {}
        self.projectiles = {}

    def run(self, gameState):
        now = time.time()
        if now - self.nextUpdate > self.frameRate:
            self.nextUpdate = now
            self.update(gameState)
            self.draw()
        
    def update(self, gameState):
        self.characters.clear()
        for charID, schar in gameState.characters.items():
            if self.client.uid == schar.player.uid:
                self.characters[charID] = ClientCharacter(self, True, schar)
            else:
                self.characters[charID] = ClientCharacter(self, False, schar)

        self.projectiles.clear()
        for projectileID, sprojectile in gameState.projectiles.items():
            if self.client.uid == sprojectile.character.player.uid:
                self.projectiles[projectileID] = ClientProjectile(self, True, sprojectile)
            else:
                self.projectiles[projectileID] = ClientProjectile(self, False, sprojectile)

    def draw(self):
        self.display.fill(self.bgColor)
        for charID, character in self.characters.items():
            character.draw()
        for projectileID, projectile in self.projectiles.items():
            projectile.draw()
        pygame.display.flip()

from ServerGame import *
from InputManager import *
import pygame

width = 50.0
height = 50.0

class ServerCharacter:
    def __init__(self, game, uid, pos):
        # Unique ID associated with character
        self.uid = uid
        self.game = game
        self.pos = pos

        self.health = 1
        
        self.vel = [0.0,0.0]
        # Velocity delta
        self.velDel = [1.5,1.5]
        self.velMax = [10,10]
        # How much the velocity retains per frame
        self.velRed = [0.8,0.8]
        
        self.width = width
        self.height = height
        self.setRect()
        
    def update(self, inputManager):
        self.vel[0] *= self.velRed[0]
        self.vel[1] *= self.velRed[1]

        if inputManager.moveUp:
            self.vel[1] -= self.velDel[1]
        if inputManager.moveLeft:
            self.vel[0] -= self.velDel[0]
        if inputManager.moveDown:
            self.vel[1] += self.velDel[1]
        if inputManager.moveRight:
            self.vel[0] += self.velDel[0]

        if abs(self.vel[0]) > self.velMax[0]:
            if self.vel[0] < 0:
                self.vel[0] = -self.velMax[0]
            else:
                self.vel[0] = self.velMax[0]
        if abs(self.vel[1]) > self.velMax[1]:
            if self.vel[1] < 0:
                self.vel[1] = -self.velMax[1]
            else:
                self.vel[1] = self.velMax[1]

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if inputManager.mainAbility:
            self.game.spawnBullet(self, inputManager.mousePos)

    def setRect(self):
        self.rect = pygame.Rect(self.pos[0] - self.width / 2.0, self.pos[1] - self.height / 2.0, self.width, self.height)

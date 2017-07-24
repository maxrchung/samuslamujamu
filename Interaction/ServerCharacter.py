from Ability import *
from ServerGame import *
from InputManager import *
import PacketCommand
import pygame

width = 50.0
height = 50.0
maxHealth = 1

class ServerCharacter:
    def __init__(self, uid, pos, name):
        # Unique ID associated with character
        self.uid = uid
        self.pos = pos
        self.name = name
        
        self.player = None
        self.game = None

        self.health = maxHealth
        
        self.vel = [0.0,0.0]
        # Velocity delta
        self.velDel = [1.5,1.5]
        self.velMax = [10,10]
        # How much the velocity retains per frame
        self.velRed = [0.8,0.8]
        
        self.width = width
        self.height = height
        self.setRect()

        self.mainAbility = Ability(0.5)
        self.reallySmallNumber = 0.0001
        self.inputManager = InputManager()
        
    def update(self):
        self.vel[0] *= self.velRed[0]
        self.vel[1] *= self.velRed[1]

        if self.inputManager.moveUp:
            self.vel[1] -= self.velDel[1]
        if self.inputManager.moveLeft:
            self.vel[0] -= self.velDel[0]
        if self.inputManager.moveDown:
            self.vel[1] += self.velDel[1]
        if self.inputManager.moveRight:
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

        if self.inputManager.mainAbility:
            if self.mainAbility.ready():
                self.game.spawnProjectile(self, self.inputManager.mousePos)

        self.inputManager.clear()

    def applyDamage(self, damage):
        self.health -= damage
                
    def setRect(self):
        self.rect = pygame.Rect(self.pos[0] - self.width / 2.0, self.pos[1] - self.height / 2.0, self.width, self.height)

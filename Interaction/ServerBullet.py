from Vector import *
import pygame

width = 10.0
height = 10.0

class ServerBullet:
    def __init__(self, bulletID, character, characterPos, mousePos):
        self.uid = bulletID
        self.character = character
        self.startPos = Vector(characterPos)
        self.pos = Vector(characterPos)
        self.endPos = Vector(mousePos)
        self.velMagnitude = 3
        
        self.width = width
        self.height = height
        self.setRect()

        difference = self.endPos.minus(self.startPos)
        self.move = difference.normalize().multiply(self.velMagnitude)

        self.totalDistSquared = self.endPos.minus(self.startPos).lengthSquared()

    def update(self):
        self.pos = self.pos.add(self.move)
        print self.pos.toString()

    def getDistSquared(self):
        dist = self.pos.minus(self.startPos).lengthSquared()
        return dist

    def setRect(self):
        self.rect = pygame.Rect(self.pos.x - self.width / 2.0, self.pos.y - self.height / 2.0, self.width, self.height)

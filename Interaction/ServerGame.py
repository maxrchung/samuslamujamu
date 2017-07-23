from GameState import *
import Global
from ServerBullet import *
from ServerCharacter import *
import pygame
import time

windowSize = width, height = 1280, 720

class ServerGame:
    def __init__(self, uid):
        # Unique ID for game
        self.uid = uid
        self.characters = []

        self.windowSize = windowSize

        self.frameRate = 1 / 60.0
        self.nextUpdate = 0

        self.gameState = None
        self.bullets = {}
        self.bulletID = 0

    def run(self):
        if self.canUpdate():
            self.nextUpdate = time.time()
            self.update()
            Global.gameState = self.gameState

    def canUpdate(self):
        can = (time.time() - self.nextUpdate) > self.frameRate
        return can
        
    def update(self):
        for charID, character in self.characters.items():
            # Wall collision
            self.wallCollision(character)
            character.setRect()

        for bulletID, bullet in self.bullets.items():
            bullet.update()
            bullet.setRect()
        
        removeBulletIDs = []
        for bulletID, bullet in self.bullets.items():
            bullet.update()
            if bullet.getDistSquared() > bullet.totalDistSquared:
                removeBulletIDs += [bullet.uid]

        while len(removeBulletIDs) != 0:
            del self.bullets[removeBulletIDs.pop()]

    def getBulletID(self):
        self.bulletID += 1
        return self.bulletID
        
    def spawnBullet(self, character, mousePos):
        bullet = ServerBullet(self.getBulletID(), character, character.pos, mousePos)
        self.bullets[bullet.uid] = bullet

    def wallCollision(self, character):
        if character.pos[0] - character.width / 2 < 0:
            character.pos[0] = character.width / 2
        elif character.pos[0] + character.width / 2 > self.windowSize[0]:
            character.pos[0] = self.windowSize[0] - character.width / 2
        if character.pos[1] - character.height / 2 < 0:
            character.pos[1] = character.height / 2
        elif character.pos[1] + character.height / 2 > self.windowSize[1]:
            character.pos[1] = self.windowSize[1] - character.height / 2

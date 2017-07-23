from GameState import *
import Global
from ServerProjectile import *
from ServerCharacter import *
from Vector import *
import pygame
from sets import Set
import time

windowSize = width, height = 1280, 720

class ServerGame:
    def __init__(self, uid):
        # Unique ID for game
        self.uid = uid
        self.characters = {}

        self.windowSize = windowSize

        self.frameRate = 1 / 60.0
        self.nextUpdate = 0

        self.gameState = None
        self.projectiles = {}
        self.projectileID = 0

    def run(self):
        if self.canUpdate():
            self.nextUpdate = time.time()
            self.update()
            Global.gameState = self.gameState

    def canUpdate(self):
        can = (time.time() - self.nextUpdate) > self.frameRate
        return can
        
    def update(self):
        self.wallCollision(self.characters)

        removeProjectileIDs = Set()
        for projectileID, projectile in self.projectiles.items():
            projectile.update()
            projectile.setRect()
            self.projectileCollision(self.characters, projectile, removeProjectileIDs)
            
        for projectileID, projectile in self.projectiles.items():
            projectile.update()
            if projectile.getDistSquared() > projectile.totalDistSquared:
                removeProjectileIDs.add(projectile.uid)

        while len(removeProjectileIDs) != 0:
            del self.projectiles[removeProjectileIDs.pop()]

    def getProjectileID(self):
        self.projectileID += 1
        return self.projectileID
        
    def spawnProjectile(self, character, mousePos):
        projectile = ServerProjectile(self.getProjectileID(), character, character.pos, mousePos)
        self.projectiles[projectile.uid] = projectile

    def projectileCollision(self, characters, projectile, removeProjectileIDs):
        for charID, character in characters.items():
            if projectile.character != character:
                diff = Vector(character.pos).minus(projectile.pos)
                if diff.length() < character.width / 2 + projectile.width / 2:
                    removeProjectileIDs.add(projectile.uid)
                    character.applyDamage(projectile.damage)
                
    def wallCollision(self, characters):
        for charID, character in self.characters.items():            
            if character.pos[0] - character.width / 2 < 0:
                character.pos[0] = character.width / 2
            elif character.pos[0] + character.width / 2 > self.windowSize[0]:
                character.pos[0] = self.windowSize[0] - character.width / 2
            if character.pos[1] - character.height / 2 < 0:
                character.pos[1] = character.height / 2
            elif character.pos[1] + character.height / 2 > self.windowSize[1]:
                character.pos[1] = self.windowSize[1] - character.height / 2
            character.setRect()

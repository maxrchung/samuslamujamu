from GameState import *
import PacketCommand
import PlayerState
import pygame
from ServerProjectile import *
from ServerCharacter import *
from sets import Set
import time
from Vector import *

windowSize = width, height = 1280, 720

class ServerGame:
    def __init__(self, server, uid):
        self.server = server
        
        # Unique ID for game
        self.uid = uid
        self.characters = None

        self.windowSize = windowSize

        self.frameRate = 1 / 60.0
        self.nextUpdate = 0

        self.projectiles = {}
        self.projectileID = 0

        self.reallySmallNumber = 0.0001

    def getGameState(self):
        charRects = []
        for charID, character in self.characters.items():
            charRects.append((character.player.uid, character.rect, character.health))

        projectileRects = []
        for projectileID, projectile in self.projectiles.items():
            projectileRects.append((projectile.character.player.uid, projectile.rect))

        return GameState(charRects, projectileRects)
        
    def run(self):
        if self.canUpdate():
            self.nextUpdate = time.time()
            self.update()

    def canUpdate(self):
        can = (time.time() - self.nextUpdate) > self.frameRate
        return can
        
    def update(self):
        for charID, character in self.characters.items():
            character.update()
        
        self.wallCollision(self.characters)

        removeProjectileIDs = Set()
        for projectileID, projectile in self.projectiles.items():
            projectile.update()
            self.projectileCollision(self.characters, projectile, removeProjectileIDs)
            
        for projectileID, projectile in self.projectiles.items():
            projectile.update()
            if projectile.getDistSquared() > projectile.totalDistSquared:
                removeProjectileIDs.add(projectile.uid)

        while len(removeProjectileIDs) != 0:
            del self.projectiles[removeProjectileIDs.pop()]

        gs = self.getGameState()
        
        for characterID, character in self.characters.items():
            self.server.sendPacket(PacketCommand.gameState, self.getGameState(), character.player)

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
                    if character.health < self.reallySmallNumber:
                        print "Game", self.uid, "finished"
                        for characterID, character in characters.items():
                            self.server.sendPacket(PacketCommand.gameEnd, character.player.uid, character.player)
                            self.server.matchMaking.append(character.player)
                            character.player.state = PlayerState.matchMaking
                        self.server.games.pop(self.uid)
                
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

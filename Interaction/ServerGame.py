from GameState import *
import Global
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

    def run(self):
        now = time.time()
        if now - self.nextUpdate > self.frameRate:
            self.nextUpdate = now
            self.update()
            Global.gameState = self.gameState

    def update(self):
        # Movement
        for charID, character in self.characters.items():
            # Update movement
            # Be sure to copy and not save reference
            currentPos = list(character.pos)
            character.pos[0] += character.vel[0]
            character.pos[1] += character.vel[1]

            # Wall collision
            self.wallCollision(currentPos, character)

            character.setRect()

    def wallCollision(self, before, character):
        if character.pos[0] - character.width / 2 < 0:
            character.pos[0] = character.width / 2
        elif character.pos[0] + character.width / 2 > self.windowSize[0]:
            character.pos[0] = self.windowSize[0] - character.width / 2
        if character.pos[1] - character.height / 2 < 0:
            character.pos[1] = character.height / 2
        elif character.pos[1] + character.height / 2 > self.windowSize[1]:
            character.pos[1] = self.windowSize[1] - character.height / 2

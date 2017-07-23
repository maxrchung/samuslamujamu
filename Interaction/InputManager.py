import pygame

from sets import Set

class InputManager:
    def __init__(self, playerID):
        # Player ID this is associated with
        self.playerID = playerID
        self.clear()
        
    def clear(self):
        self.moveUp = False
        self.moveLeft = False
        self.moveDown = False
        self.moveRight = False
        

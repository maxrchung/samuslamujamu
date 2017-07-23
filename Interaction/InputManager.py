import pygame

from sets import Set

class InputManager:
    def __init__(self):
        # Player ID this is associated with
        self.clear()
        
    def clear(self):
        self.moveUp = False
        self.moveLeft = False
        self.moveDown = False
        self.moveRight = False
        self.mainAbility = False
        self.mousePos = [0,0]
        

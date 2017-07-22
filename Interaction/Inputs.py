import pygame

from sets import Set

class Inputs:
    def __init__(self):
        self.clear()
        
    def clear(self):
        self.moveUp = False
        self.moveLeft = False
        self.moveDown = False
        self.moveRight = False
        
    def update(self):
        self.clear()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.moveUp = True

        if keys[pygame.K_a]:
            self.moveLeft = True
            
        if keys[pygame.K_s]:
            self.moveDown = True

        if keys[pygame.K_d]:
            self.moveRight = True
        

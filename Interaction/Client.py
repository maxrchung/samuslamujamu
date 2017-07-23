from ClientGame import *
from EventManager import *
import Global
import pygame
from pygame.locals import *

class Client:
    def __init__(self):
        self.eventManager = EventManager()
        self.running = True

        self.game = ClientGame()
    
    def getInput(self):
        inputManager = Global.inputManager
        inputManager.clear()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            inputManager.moveUp = True

        if keys[pygame.K_a]:
            inputManager.moveLeft = True
            
        if keys[pygame.K_s]:
            inputManager.moveDown = True

        if keys[pygame.K_d]:
            inputManager.moveRight = True

        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            inputManager.mainAbility = True
            
        inputManager.mousePos = pygame.mouse.get_pos()

    def run(self):
#        while self.running:
            self.eventManager.update()
            self.getInput()
            self.game.update(Global.gameState)
            self.game.draw()

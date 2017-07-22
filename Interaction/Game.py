from Character import *
from Events import *
from Inputs import *
import pygame
import time

class Game:
    def __init__(self):
        self.running = True
        self.size = self.width, self.height = 1280, 720
        self.display = pygame.display.set_mode(self.size, pygame.DOUBLEBUF)
        pygame.init()
        
        self.frameRate = 1 / 60.0
        self.nextUpdate = 0

        self.inputs = Inputs()
        self.events = Events()
        
        self.character = Character(self, [400.0,400.0])
        self.dummy = Character(self, [300.0,300.0])

        self.bgColor = pygame.Color(100,100,100,255)
                
    def run(self):
        while self.running:
            now = time.time()
            if now - self.nextUpdate > self.frameRate:
                self.nextUpdate = now
                self.update()
                self.draw()

    def update(self):
        self.events.update()
        self.inputs.update()
        self.character.update(self.inputs)

    def draw(self):
        self.display.fill(self.bgColor)
        self.character.draw()
        self.dummy.draw()
        pygame.display.flip()

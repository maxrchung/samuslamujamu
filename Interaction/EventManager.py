from InputManager import *
import pygame
import sys

class EventManager:
    def __init__(self):
        pass

    def update(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

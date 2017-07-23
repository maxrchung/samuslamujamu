import ServerCharacter
import pygame

class ClientCharacter:
    def __init__(self, game):
        self.game = game
        self.color = pygame.Color(255,255,255,255)
        self.pos = [0,0]
        self.width = ServerCharacter.width
        self.height = ServerCharacter.height
        self.rect = None

    def draw(self):
        pygame.draw.circle(self.game.display, self.color, self.rect.center, self.rect.width / 2)

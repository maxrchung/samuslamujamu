import ServerProjectile
import pygame

class ClientProjectile:
    def __init__(self, game, main, rect):
        self.game = game
        self.rect = rect

        if main:
            self.color = pygame.Color(0,0,200,255)
        else:
            self.color = pygame.Color(200,0,0,255)

    def draw(self):
        pygame.draw.circle(self.game.display, self.color, self.rect.center, self.rect.width / 2)

import ServerBullet
import pygame

class ClientBullet:
    def __init__(self, game):
        self.game = game
        self.color = pygame.Color(200,0,0,0)
        self.pos = [0,0]
        self.width = ServerBullet.width
        self.height = ServerBullet.height
        self.rect = None

    def draw(self):
        pygame.draw.circle(self.game.display, self.color, self.rect.center, self.rect.width / 2)
        

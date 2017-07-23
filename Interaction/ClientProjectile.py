import ServerProjectile
import pygame

class ClientProjectile:
    def __init__(self, game, main, sprojectile):
        self.game = game
        self.main = main
        self.setFromServer(sprojectile)
        
        self.width = ServerProjectile.width
        self.height = ServerProjectile.height

        self.mainColor = pygame.Color(0,0,200,255)
        self.enemyColor = pygame.Color(200,0,0,255)

    def draw(self):
        color = None
        if self.main:
            color = self.mainColor
        else:
            color = self.enemyColor
        pygame.draw.circle(self.game.display, color, self.rect.center, self.rect.width / 2)

    def setFromServer(self, sprojectile):
        self.rect = sprojectile.rect

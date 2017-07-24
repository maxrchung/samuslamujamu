import ServerCharacter
import pygame

class ClientCharacter:
    def __init__(self, game, main, rect, health):
        self.game = game
        self.rect = rect
        self.health = health

        self.maxHealth = ServerCharacter.maxHealth

        if main:
            self.color = pygame.Color(50,50,200,255)
        else:
            self.color = pygame.Color(200,50,50,255)
        
        self.innerHealthColor = pygame.Color(0,200,0,255)
        self.outerHealthOutline = pygame.Color(0,0,0,255)

    def draw(self):
        pygame.draw.circle(self.game.display, self.color, self.rect.center, self.rect.width / 2)

        if self.health > 0:
            healthPercent = self.health / self.maxHealth
            innerHealth = pygame.Rect(self.rect.left, self.rect.top - 20, self.rect.width * healthPercent, 10)
            pygame.draw.rect(self.game.display, self.innerHealthColor, innerHealth)

        outerHealth = pygame.Rect(self.rect.left, self.rect.top - 20, self.rect.width, 10)
        pygame.draw.rect(self.game.display, self.outerHealthOutline, outerHealth, 2)

import ServerCharacter
import pygame

class ClientCharacter:
    def __init__(self, game, main, schar):
        self.game = game
        self.main = main
        self.setFromServer(schar)

        self.width = ServerCharacter.width
        self.height = ServerCharacter.height
        self.maxHealth = ServerCharacter.maxHealth
        
        self.mainColor = pygame.Color(50,50,200,255)
        self.enemyColor = pygame.Color(200,50,50,255)
        
        self.innerHealthColor = pygame.Color(0,200,0,255)
        self.outerHealthOutline = pygame.Color(0,0,0,255)

    def draw(self):
        color = None
        if self.main:
            color = self.mainColor
        else:
            color = self.enemyColor
        pygame.draw.circle(self.game.display, color, self.rect.center, self.rect.width / 2)

        if self.health > 0:
            healthPercent = self.health / self.maxHealth
            innerHealth = pygame.Rect(self.rect.left, self.rect.top - 20, self.rect.width * healthPercent, 10)
            pygame.draw.rect(self.game.display, self.innerHealthColor, innerHealth)

        outerHealth = pygame.Rect(self.rect.left, self.rect.top - 20, self.rect.width, 10)
        pygame.draw.rect(self.game.display, self.outerHealthOutline, outerHealth, 2)

    def setFromServer(self, schar):
        self.rect = schar.rect
        self.health = schar.health

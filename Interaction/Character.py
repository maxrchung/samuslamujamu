from Game import *
import pygame

class Character:
    def __init__(self, game, pos):
        self.health = 1
        self.game = game
        self.pos = pos
        
        self.vel = [0.0,0.0]
        # Velocity delta
        self.velDel = [1.0,1.0]
        self.velMax = [2.0,2.0]
        # How much the velocity reduces per frame
        self.velRed = 0.5

        self.color = pygame.Color(255,255,255,255)
        self.width = 50.0
        self.height = 50.0
        self.setRect()
        
    def update(self, inputs):
        self.vel[0] *= self.velRed
        self.vel[1] *= self.velRed

        if inputs.moveUp:
            self.vel[1] -= self.velMax[1]
            print "u muving son"
        if inputs.moveLeft:
            self.vel[0] -= self.velMax[0]
        if inputs.moveDown:
            self.vel[1] += self.velMax[1]
        if inputs.moveRight:
            self.vel[0] += self.velMax[0]

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.setRect()
        
    def draw(self):
        pygame.draw.rect(self.game.display, self.color, self.rect)

    def setRect(self):
        self.rect = pygame.Rect(self.pos[0] - self.width / 2.0, self.pos[1] - self.height / 2.0, self.width, self.height).copy()

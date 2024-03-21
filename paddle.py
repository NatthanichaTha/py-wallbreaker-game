from constant import *
import pygame

class Paddle:
    def __init__(self):
        self.width = 120
        self.height = 10
        self.x = (SCREEN_WIDTH/2) - (self.width/2)
        self.y = SCREEN_HEIGHT - 50
        self.color = WHITE
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def move(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] and self.x + self.width < SCREEN_WIDTH:
            #move right when press right (until the screen edge)
            self.x += self.speed
        elif key_pressed[pygame.K_LEFT] and self.x > 0: 
            #move left when press left (until the screen edge)
            self.x -= self.speed

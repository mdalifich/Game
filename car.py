import pygame
from pygame import *
import os
import load_image
from load_image import *


class Cars(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x, self.y = x, y
        self.image = load_image('static/car.png')
        self.rect = Rect(self.x, self.y, 150, 95)
        self.screen = screen
        self.vect = 10

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.x >= 650:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.vect = -10
        if self.rect.x < -1:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.vect = 10
        self.rect.x += self.vect
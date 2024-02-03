import pygame
from pygame import *
import os
import load_image
from load_image import *


class Cars(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x, self.y = x, y
        self.image = load_image('data/car.png')
        self.rect = Rect(self.x, self.y, 150, 95)
        self.screen = screen
        self.vect = 20

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.x >= 350:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.vect = -20
        if self.rect.x < 0:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.vect = 20
        self.rect.x += self.vect
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
        self.image = pygame.transform.scale(self.image, (164, 82))
        self.rect = Rect(self.x, self.y, 164, 82)
        self.screen = screen
        self.vect = 10

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        self.rect.x += self.vect
import pygame
from pygame import *
import os
import load_image
from load_image import *


class Bar(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x, self.y = x, y
        self.image = load_image('data/3.png')
        self.rect = Rect(self.x, self.y, 83, 101)
        self.screen = screen

    def draw(self, hp):
        self.image = load_image(f'data/{hp}.png')
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
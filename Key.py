import pygame
from pygame import *
import os
import load_image
from load_image import *
from random import randint


class Key(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x, self.y = x, y
        self.image = load_image('static/key.png')
        self.image = pygame.transform.scale(self.image, (15, 28))
        self.rect = Rect(self.x, self.y, 15, 28)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
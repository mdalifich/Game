import pygame
from pygame import *
import os
import load_image
from load_image import *
from random import randint


class Barrier(pygame.sprite.Sprite):
    def __init__(self, x, y, screen, group):
        super().__init__(group)
        self.x, self.y = x, y
        self.image = load_image('static/wall.png')
        self.image = pygame.transform.scale(self.image, (82, 82))
        self.rect = Rect(self.x, self.y, 82, 82)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.y > 800:
            self.rect.y = 0
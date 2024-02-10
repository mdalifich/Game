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
        self.image = load_image('data/wall.png')
        rot = 90 * randint(0, 1)
        self.image = pygame.transform.scale(self.image, (200, 50))
        self.image = pygame.transform.rotate(self.image, rot)
        if rot == 90:
            self.rect = Rect(self.x, self.y, 50, 200)
        else:
            self.rect = Rect(self.x, self.y, 200, 50)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
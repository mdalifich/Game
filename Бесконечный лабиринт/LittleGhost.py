import pygame
from pygame import *
import os
import load_image
from load_image import *


class LtGhost(pygame.sprite.Sprite):
    def __init__(self, x, y, screen, group):
        super().__init__(group)
        self.x, self.y = x, y
        self.image = load_image('static/LtGhost.png')
        self.image = pygame.transform.scale(self.image, (40, 12))
        self.image = pygame.transform.rotate(self.image, -90.0)
        self.rect = Rect(self.x, self.y, 12, 40)
        self.screen = screen
        self.tick = 0

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.tick == 50:
            self.kill()
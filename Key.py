import pygame
from pygame import *
import os
import load_image
from load_image import *
from random import randint


class Keys(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.x, self.y = -50, 0#randint(-800, 800), randint(-800, 800)
        self.image = load_image('static/Key.png')
        self.image = pygame.transform.scale(self.image, (15, 28))
        self.rect = Rect(self.x, self.y, 15, 28)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
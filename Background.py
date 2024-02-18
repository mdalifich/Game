import pygame
from pygame import *
import os
import load_image
from load_image import *
from random import randint


class Back(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = load_image('static/Trava.jpg')
        self.rect = Rect(0, 0, 800, 800)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
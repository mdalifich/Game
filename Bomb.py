import pygame
from pygame import *
import os
import load_image
from load_image import *
import sys
from sys import *
import random


class Bomb(pygame.sprite.Sprite):

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = load_image("data/bomb.png")
        self.image_boom = load_image("data/boom.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(500)
        self.rect.y = random.randrange(500)

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom
import pygame
from pygame import *
import os
import load_image
from load_image import *
from random import randint


class DDoors(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.x, self.y = 500, 500
        self.image = load_image('static/DoorClose.png')
        self.rect = Rect(self.x, self.y, 166, 187)
        self.screen = screen
        self.flag = False

    def draw(self):
        if self.flag:
            self.image = load_image('static/DoorOpen.png')
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
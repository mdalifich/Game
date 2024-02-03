import pygame
from pygame import *
import os
import load_image
from load_image import *


class GameOverIcon(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x, self.y = x, y
        self.image = load_image('data/GameOver.png')
        self.rect = Rect(self.x, self.y, 800, 800)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.x <= -1:
            self.rect.x += 20
import pygame
from pygame import *
import os
import load_image
from load_image import *
from random import randint


class EnemyGhost(pygame.sprite.Sprite):
    def __init__(self, screen, group):
        super().__init__(group)
        self.x, self.y = randint(-1200, 1200), randint(-1200, 1200)
        self.image = load_image('static/ghost_creepy.png')
        self.image = pygame.transform.scale(self.image, (192, 108))
        self.rect = Rect(self.x, self.y, 192, 108)
        self.screen = screen
        self.speed = 1

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def Intellect(self, Pers):
        if self.rect.x == Pers.rect.x - 82:
            if self.rect.y < Pers.rect.y:
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed
        elif self.rect.y == Pers.rect.y:
            if self.rect.x < Pers.rect.x - 82:
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed
        elif abs(self.rect.x - Pers.rect.x) == abs(self.rect.y - Pers.rect.y):
            if self.rect.x < Pers.rect.x and self.rect.y < Pers.rect.y:
                self.rect.x += self.speed
                self.rect.y += self.speed
            elif self.rect.x < Pers.rect.x and self.rect.y > Pers.rect.y:
                self.rect.x += self.speed
                self.rect.y -= self.speed
            if self.rect.x > Pers.rect.x and self.rect.y < Pers.rect.y:
                self.rect.x -= self.speed
                self.rect.y += self.speed
            elif self.rect.x > Pers.rect.x and self.rect.y > Pers.rect.y:
                self.rect.x -= self.speed
                self.rect.y -= self.speed
        else:
            if abs(self.rect.x - Pers.rect.x) < abs(self.rect.y - Pers.rect.y):
                if self.rect.x < Pers.rect.x - 82:
                    self.rect.x += self.speed
                else:
                    self.rect.x -= self.speed
            else:
                if self.rect.y < Pers.rect.y:
                    self.rect.y += self.speed
                else:
                    self.rect.y -= self.speed

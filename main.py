import pygame
from pygame import *
import os
import load_image
from load_image import *
import curs
from curs import *
import Person
from Person import *
import car
from car import *
import Bomb
from Bomb import *


if __name__ == '__main__':
    pygame.init()
    size = 500
    screen = pygame.display.set_mode((size, size))
    pygame.mouse.set_visible(False)
    NewCurs = Curs(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)
    NewPers = Pers(0, 0, screen)
    NewCar = Cars(0, 300, screen)
    running = True
    Bombes = pygame.sprite.Group()
    for _ in range(50):
        Bomb(Bombes)

    while running:
        # Чтобы экран был черный сюда нада вписать (0, 0, 0)
        screen.fill((255, 255, 255))

        NewPers.draw()
        NewCar.draw()
        Bombes.draw(screen)
        Bombes.update()
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            NewPers.rect.y -= 10
        elif key[pygame.K_DOWN]:
            NewPers.rect.y += 10
        elif key[pygame.K_RIGHT]:
            NewPers.rect.x += 10
        elif key[pygame.K_LEFT]:
            NewPers.rect.x -= 10

        if pygame.mouse.get_focused():
            NewCurs.rect.x, NewCurs.rect.y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            NewCurs.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in Bombes:
                    bomb.update(event)

        pygame.display.update()

        pygame.display.flip()
    pygame.quit()
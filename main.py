import pygame
from pygame import *
import os
import load_image
from load_image import *
import curs
from curs import *
import Person
from Person import *


if __name__ == '__main__':
    pygame.init()
    size = 500
    screen = pygame.display.set_mode((size, size))
    pygame.mouse.set_visible(False)
    NewCurs = Curs(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)
    NewPers = Pers(0, 0, screen)

    while pygame.event.wait().type != pygame.QUIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            key = pygame.key.get_pressed()

            if key[pygame.K_UP]:
                NewPers.rect.y -= 10
            if key[pygame.K_DOWN]:
                NewPers.rect.y += 10
            if key[pygame.K_RIGHT]:
                NewPers.rect.x += 10
            if key[pygame.K_LEFT]:
                NewPers.rect.x -= 10

            pygame.display.update()
        # Чтобы экран был черный сюда нада вписать (0, 0, 0)
        screen.fill((255, 255, 255))

        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            NewPers.rect.y -= 10
        if key[pygame.K_DOWN]:
            NewPers.rect.y += 10
        if key[pygame.K_RIGHT]:
            NewPers.rect.x += 10
        if key[pygame.K_LEFT]:
            NewPers.rect.x -= 10

        NewPers.draw()

        if pygame.mouse.get_focused():
            NewCurs.rect.x, NewCurs.rect.y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            NewCurs.draw()


        pygame.display.flip()
    pygame.quit()
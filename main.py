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
import HpBar
from HpBar import *
import GameOverIcon
from GameOverIcon import *


if __name__ == '__main__':
    pygame.init()
    size = 800
    screen = pygame.display.set_mode((size, size))
    pygame.mouse.set_visible(False)
    NewCurs = Curs(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)
    NewPers = Pers(100, 100, screen)
    NewCar = Cars(0, 300, screen)
    running = True
    HealPoints = 3
    HealBar = Bar(0, 0, screen)
    Immortal = False
    tick = 0
    GameOverer = GameOverIcon(-800, 0, screen)
    Bombes = pygame.sprite.Group()
    for _ in range(10):
        Bomb(Bombes)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in Bombes:
                    bomb.update(event)

        if HealPoints != 0:
            # Чтобы экран был черный сюда нада вписать (0, 0, 0)
            screen.fill((255, 255, 255))
            draw_text(screen, f"Immortal = {Immortal}", 500, 0)
            NewPers.draw()
            NewCar.draw()
            Bombes.draw(screen)
            Bombes.update()
            HealBar.draw(HealPoints)
            for i in Bombes:
                if pygame.sprite.collide_mask(i, NewPers) and i.image != i.image_boom and not Immortal:
                    HealPoints -= 1
                    Immortal = True
            if pygame.sprite.collide_mask(NewCar, NewPers) and not Immortal:
                HealPoints -= 1
                Immortal = True

            if Immortal:
                tick += 1
            if tick == 25:
                tick = 0
                Immortal = False

            key = pygame.key.get_pressed()
            speedPers = 5
            if key[pygame.K_UP]:
                NewPers.rect.y -= speedPers
            elif key[pygame.K_DOWN]:
                NewPers.rect.y += speedPers
            elif key[pygame.K_RIGHT]:
                NewPers.rect.x += speedPers
            elif key[pygame.K_LEFT]:
                NewPers.rect.x -= speedPers

            if pygame.mouse.get_focused():
                NewCurs.rect.x, NewCurs.rect.y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                NewCurs.draw()
        else:
            if pygame.mouse.get_focused():
                NewCurs.rect.x, NewCurs.rect.y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                NewCurs.draw()
            screen.fill((250, 250, 250))
            GameOverer.draw()

        pygame.display.update()

        pygame.display.flip()
    pygame.quit()
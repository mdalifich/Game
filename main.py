import pygame
from pygame import *
from random import randint
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
import Button
from Button import *
import Shipi
from Shipi import *
import Bullet
from Bullet import *


if __name__ == '__main__':
    pygame.init()
    size = 800
    screen = pygame.display.set_mode((size, size))
    pygame.mouse.set_visible(False)
    RemakeBTN = Button('Повторим?', 300, 600, 200, 50, (50, 50, 50))
    reset = True
    running = True
    NewCurs = Curs(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)
    NewPers = Pers(100, 100, screen)
    NewCar = Cars(0, 300, screen)
    HealPoints = 3
    HealBar = Bar(0, 0, screen)
    Immortal = False
    Ship = Shipi(0, 757, screen)
    tick = 0
    Rebullet = 0
    GameOverer = GameOverIcon(-800, 0, screen)
    Bombes = pygame.sprite.Group()
    Bull = pygame.sprite.Group()
    for _ in range(10):
        Bomb(Bombes)
    EndGame = False

    while running:
        if reset:
            Rebullet = 0
            NewCurs = Curs(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)
            NewPers = Pers(100, 100, screen)
            NewCar = Cars(0, 300, screen)
            running = True
            HealPoints = 3
            HealBar = Bar(0, 0, screen)
            Immortal = False
            tick = 0
            Ship = Shipi(0, 757, screen)
            GameOverer = GameOverIcon(-800, 0, screen)
            Bombes = pygame.sprite.Group()
            Bull = pygame.sprite.Group()
            for _ in range(10):
                Bomb(Bombes)
            reset = False
            EndGame = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in Bombes:
                    bomb.update(event)
                if RemakeBTN.is_over(pos) and EndGame:
                    reset = True

        if HealPoints != 0:
            # Чтобы экран был черный сюда нада вписать (0, 0, 0)
            screen.fill((255, 255, 255))
            Rebullet += 1
            if Rebullet == 25:
                Bullet(randint(0, 800), 0, screen, Bull)
                Rebullet = 0
            draw_text(screen, f"Immortal = {Immortal}", 500, 0)
            NewPers.draw()
            NewCar.draw()
            Bombes.draw(screen)
            Bombes.update()
            HealBar.draw(HealPoints)
            Ship.draw()
            Bull.draw(screen)
            for i in Bull:
                if not pygame.sprite.collide_mask(i, Ship):
                    i.rect.y += 20
                else:
                    i.tick += 1
                if pygame.sprite.collide_mask(i, Ship):
                    i.kill()
                if pygame.sprite.collide_mask(i, NewPers):
                    HealPoints -= 1
                    i.kill()
                    Immortal = True
            for i in Bombes:
                if pygame.sprite.collide_mask(i, NewPers) and i.image != i.image_boom and not Immortal:
                    HealPoints -= 1
                    Immortal = True
            if pygame.sprite.collide_mask(NewCar, NewPers) and not Immortal:
                HealPoints -= 1
                Immortal = True
            if pygame.sprite.collide_mask(Ship, NewPers) and not Immortal:
                HealPoints -= 1
                Immortal = True

            if Immortal:
                tick += 1
            if tick == 50:
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
            screen.fill((250, 250, 250))
            GameOverer.draw()
            RemakeBTN.draw(screen, (100, 100, 100))
            if pygame.mouse.get_focused():
                NewCurs.rect.x, NewCurs.rect.y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                NewCurs.draw()
            EndGame = True

        pygame.display.update()

        pygame.display.flip()
    pygame.quit()
import pygame
from pygame import *
from random import randint, randrange
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
import wall
from wall import *


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
    speedPersRight = 5
    speedPersLeft = 5
    speedPersUp = 5
    speedPersDown = 5
    GameOverer = GameOverIcon(-800, 0, screen)
    Bombes = pygame.sprite.Group()
    Bull = pygame.sprite.Group()
    Walls = pygame.sprite.Group()
    for _ in range(10):
        Bomb(Bombes)
    for _ in range(1):
        Barrier(randint(0, 700), randint(0, 700), screen, Walls)
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
            speedPersRight = 5
            speedPersLeft = 5
            speedPersUp = 5
            speedPersDown = 5
            for _ in range(20):
                Bomb(Bombes)
            reset = False
            EndGame = False
            for _ in range(5):
                Barrier(randint(0, 600), randint(0, 600), screen, Walls)

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
            Walls.draw(screen)
            for i in Bull:
                if not pygame.sprite.collide_mask(i, Ship):
                    i.rect.y += 10
                else:
                    i.tick += 1
                if pygame.sprite.collide_mask(i, Ship):
                    i.kill()
                if pygame.sprite.collide_mask(i, NewPers):
                    HealPoints -= 1
                    i.kill()
                    Immortal = True
            for i in Bombes:
                for j in Bombes:
                    if i != j:
                        while pygame.sprite.collide_mask(i, j):
                            i.rect.x = random.randrange(800)
                            i.rect.y = random.randrange(800)
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
            if key[pygame.K_UP]:
                speedPersRight = 5
                speedPersLeft = 5
                speedPersDown = 5
                NewPers.rect.y -= speedPersUp
                for i in Walls:
                    if pygame.sprite.collide_mask(i, NewPers):
                        speedPersUp = 0
                        print(2)
            elif key[pygame.K_DOWN]:
                speedPersRight = 5
                speedPersLeft = 5
                speedPersUp = 5
                NewPers.rect.y += speedPersDown
                for i in Walls:
                    if pygame.sprite.collide_mask(i, NewPers):
                        speedPersDown = 0
                        print(3)
            elif key[pygame.K_RIGHT]:
                speedPersLeft = 5
                speedPersUp = 5
                speedPersDown = 5
                NewPers.rect.x += speedPersRight
                for i in Walls:
                    if pygame.sprite.collide_mask(i, NewPers):
                        speedPersRight = 0
                        print(4)
            elif key[pygame.K_LEFT]:
                speedPersRight = 5
                speedPersUp = 5
                speedPersDown = 5
                NewPers.rect.x -= speedPersLeft
                for i in Walls:
                    if pygame.sprite.collide_mask(i, NewPers):
                        speedPersLeft = 0
                        print(1)

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
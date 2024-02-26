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
import Cam
from Cam import *
import Background
from Background import *
import Key
from Key import *
import Doors
from Doors import *
import Enemy
from Enemy import *


size = width, height = (800, 800)
if __name__ == '__main__':
    pygame.init()
    size = width, height = (800, 800)
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)
    RemakeBTN = Button('Повторим?', 300, 600, 200, 50, (50, 50, 50))
    PlayBTN = Button('Играть', 300, 200, 200, 50, (50, 50, 50))
    ExitBTN = Button('Выйти', 300, 600, 200, 50, (50, 50, 50))
    BackBTN = Button('Выйти в меню', 300, 800, 200, 50, (50, 50, 50))
    reset = True
    running = True
    NewCurs = Curs(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)
    NewPers = Pers(400, 400, screen)
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
    camera = Camera()
    door = DDoors(screen)
    level = 1
    start = False
    ClickToKey = False
    BaseCollideCoord = tuple()
    for _ in range(10):
        Bomb(Bombes)
    EndGame = False
    background = Back(screen)
    MyKey = Keys(screen)
    Minimizade = 0
    Enemys = pygame.sprite.Group()
    for _ in range(5):
        EnemyGhost(screen, Enemys)
    isPause = False


    def generate_level(lvl):
        new_player, x, y = None, None, None
        global NewPers, NewCar
        for y in range(len(lvl)):
            for x in range(len(lvl[y])):
                if lvl[y][x] == '@':
                    Barrier(x * 82, y * 82, screen, Walls)
                elif lvl[y][x] == '#':
                    NewCar = Cars(x * 82, y * 82, screen)
                elif lvl[y][x] == '$':
                    pass
                elif lvl[y][x] == 'P':
                    NewPers = Pers(x * 82, y * 82, screen)
        # вернем игрока, а также размер поля в клетках
        return new_player, x, y


    while running:
        if reset:
            level = 1
            Rebullet = 0
            MyKey = Keys(screen)
            NewCurs = Curs(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)
            running = True
            HealPoints = 3
            HealBar = Bar(0, 0, screen)
            Immortal = False
            tick = 0
            door = DDoors(screen)
            Ship = Shipi(0, 757, screen)
            GameOverer = GameOverIcon(-800, 0, screen)
            Bombes = pygame.sprite.Group()
            Walls = pygame.sprite.Group()
            Bull = pygame.sprite.Group()
            Enemys = pygame.sprite.Group()
            speedPersRight = 5
            speedPersLeft = 5
            speedPersUp = 5
            speedPersDown = 5
            background = Back(screen)
            ClickToKey = False
            BaseCollideCoord = tuple()
            Minimizade = 0
            for _ in range(1):
                EnemyGhost(screen, Enemys)
            isPause = False

            for _ in range(20):
                Bomb(Bombes)
                for i in Bombes:
                    for j in Bombes:
                        if i != j:
                            while pygame.sprite.collide_mask(i, NewPers):
                                i.rect.x = random.randrange(800)
                                i.rect.y = random.randrange(800)
            reset = False
            EndGame = False
            generate_level(load_level(f'level{str(level)}.txt'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in Bombes:
                    bomb.update(event)
                if RemakeBTN.is_over(pos) and EndGame:
                    reset = True
                if BackBTN.is_over(pos) and EndGame or BackBTN.is_over(pos) and isPause:
                    start = False
                if PlayBTN.is_over(pos) and not start:
                    reset = True
                    start = True
                if ExitBTN.is_over(pos) and not start:
                    running = False
                if pygame.sprite.collide_mask(NewCurs, MyKey):
                    ClickToKey = True
                    BaseCollideCoord = pos
            if event.type == pygame.MOUSEBUTTONUP:
                ClickToKey = False
            if event.type == pygame.WINDOWMINIMIZED:
                Minimizade += 1

            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                isPause = not isPause


        if not start:
            screen.fill((255, 255, 255))
            col = (100, 100, 100)
            PlayBTN.draw(screen, col)
            ExitBTN.draw(screen, col)


        if HealPoints != 0 and start and not isPause:
            # Чтобы экран был черный сюда нада вписать (0, 0, 0)
            screen.fill((255, 255, 255))
            Rebullet += 1
            if Rebullet == 25:
                Bullet(randint(0, 800), 0, screen, Bull)
                Rebullet = 0
            background.draw()
            NewPers.draw()
            NewCar.draw()
            Bombes.draw(screen)
            Bombes.update()
            HealBar.draw(HealPoints)
            Ship.draw()
            Bull.draw(screen)
            Walls.draw(screen)
            Enemys.draw(screen)
            door.draw()
            MyKey.draw()
            for Ghost in Enemys:
                Ghost.Intellect(NewPers)
            HealBar.draw(HealPoints)
            draw_text(screen, f"Immortal = {Immortal}", 500, 0)
            draw_text(screen, f"Minimizade = {Minimizade}", 500, 100)
            camera.update(NewPers)
            for sprite in Bombes:
                camera.apply(sprite)
            for sprite in Walls:
                camera.apply(sprite)
            for sprite in Bull:
                camera.apply(sprite)
            for sprite in Enemys:
                camera.apply(sprite)
            camera.apply(Ship)
            camera.apply(NewCar)
            camera.apply(NewPers)
            camera.apply(MyKey)
            camera.apply(door)
            pos = pygame.mouse.get_pos()

            if ClickToKey and pygame.sprite.collide_mask(MyKey, NewCurs):
                MyKey.rect.x += pos[0] - BaseCollideCoord[0]
                MyKey.rect.y += pos[1] - BaseCollideCoord[1]
                BaseCollideCoord = pos

            if not pygame.mouse.get_focused():
                ClickToKey = False

            if pygame.sprite.collide_mask(door, MyKey):
                door.flag = True
                ClickToKey = False
                MyKey.kill()

            for i in Enemys:
                if pygame.sprite.collide_mask(NewPers, i):
                    HealPoints = 0

            for i in Walls:
                if pygame.sprite.collide_mask(MyKey, i):
                    ClickToKey = False
                    MyKey.rect.x += 90
                    if pygame.sprite.collide_mask(MyKey, i):
                        MyKey.rect.y += 90

            if pygame.sprite.collide_mask(door, NewPers):
                if door.flag:
                    reset = True
                    level += 1
                    if level == 4:
                        level = 1

            for i in Bull:
                if not pygame.sprite.collide_mask(i, Ship):
                    i.rect.y += 10
                else:
                    i.tick += 1
                for j in Walls.sprites():
                    if pygame.sprite.collide_mask(i, j):
                        i.kill()
                if pygame.sprite.collide_mask(i, Ship):
                    i.kill()
                if pygame.sprite.collide_mask(i, NewPers):
                    HealPoints -= 1
                    i.kill()
                    Immortal = True
            for i in Bombes:
                for j in Bombes:
                    if i != j:
                        while pygame.sprite.collide_mask(i, j) or 800 < i.rect.x or i.rect.x < 0 or 800 < i.rect.y or 0 > i.rect.y:
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

            if door.rect.y > 1200:
                door.rect.y = -1200
            if door.rect.y < -1200:
                door.rect.y = 1200
            if door.rect.x > 1200:
                door.rect.x = -1200
            if door.rect.x < -1200:
                door.rect.x = 1200

            for i in Walls:
                if i.rect.y > 800:
                    i.rect.y = -82
                if i.rect.y < -82:
                    i.rect.y = 800
                if i.rect.x > 800:
                    i.rect.x = -82
                if i.rect.x < -82:
                    i.rect.x = 800
                if pygame.sprite.collide_mask(i, NewCar):
                    NewCar.image = pygame.transform.flip(NewCar.image, 1, 0)
                    NewCar.vect = -1 * NewCar.vect

            key = pygame.key.get_pressed()
            if key[pygame.K_UP]:
                speedPersRight = 5
                speedPersLeft = 5
                speedPersDown = 5
                NewPers.rect.y -= speedPersUp
                for i in Walls:
                    if pygame.sprite.collide_mask(i, NewPers):
                        speedPersUp = 0
                        NewPers.rect.y += 5

            elif key[pygame.K_DOWN]:
                speedPersRight = 5
                speedPersLeft = 5
                speedPersUp = 5
                NewPers.rect.y += speedPersDown
                for i in Walls:
                    if pygame.sprite.collide_mask(i, NewPers):
                        speedPersDown = 0
                        NewPers.rect.y -= 5
            elif key[pygame.K_RIGHT]:
                speedPersLeft = 5
                speedPersUp = 5
                speedPersDown = 5
                NewPers.rect.x += speedPersRight
                for i in Walls:
                    if pygame.sprite.collide_mask(i, NewPers):
                        speedPersRight = 0
                        NewPers.rect.x -= 5
            elif key[pygame.K_LEFT]:
                speedPersRight = 5
                speedPersUp = 5
                speedPersDown = 5
                NewPers.rect.x -= speedPersLeft
                for i in Walls:
                    if pygame.sprite.collide_mask(i, NewPers):
                        speedPersLeft = 0
                        NewPers.rect.x += 5
        else:
            if HealPoints == 0:
                screen.fill((250, 250, 250))
                GameOverer.draw()
                RemakeBTN.draw(screen, (100, 100, 100))
                BackBTN.draw(screen, (100, 100, 100))
                EndGame = True
            else:
                BackBTN.draw(screen, (100, 100, 100))
        if pygame.mouse.get_focused():
            NewCurs.rect.x, NewCurs.rect.y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            NewCurs.draw()

        pygame.display.update()

        pygame.display.flip()
    pygame.quit()
import pygame
from pygame import *
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Curs(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x, self.y = x, y
        self.image = load_image('data/cursor.png')
        self.rect = Rect(self.x, self.y, 42, 42)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        print(234)


if __name__ == '__main__':
    pygame.init()
    size, box = [int(i) for i in input().split()]
    screen = pygame.display.set_mode((size, size))
    pygame.mouse.set_visible(False)

    while pygame.event.wait().type != pygame.QUIT:
        # Чтобы экран был черный сюда нада вписать (0, 0, 0)
        screen.fill((255, 255, 255))
        if pygame.mouse.get_focused():
            NewCurs = Curs(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            NewCurs.draw()

        pygame.display.flip()
    pygame.quit()
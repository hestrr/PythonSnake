'''Ваша задача написать код анимации квадрата, который перемещается от
левой границе к правой, касается ее, но не исчезает за ней. После этого
возвращается назад – от правой границы к левой, касается ее, опять двигается
вправо. Циклы движения квадрата повторяются до завершения программы.'''

import pygame as pg
import sys

pg.init()
WIN_WIDTH = 600
WIN_HEIGHT = 400
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0)
clock = pg.time.Clock()
sc = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption('aaa')

w_rect = 50
h_rect = 50
x = WIN_WIDTH // 2
y = WIN_HEIGHT // 2

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT or (i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                x -= 10
            elif i.key == pg.K_RIGHT:
                x += 10
            elif i.key == pg.K_UP:
                y -= 10
            elif i.key == pg.K_DOWN:
                y += 10
    sc.fill(BLACK)
    pg.draw.rect(sc, ORANGE, (x, y, w_rect, h_rect))
    pg.display.update()

    clock.tick(60)

'''Ваша задача написать код анимации квадрата, который перемещается от
левой границе к правой, касается ее, но не исчезает за ней. После этого
возвращается назад – от правой границы к левой, касается ее, опять двигается
вправо. Циклы движения квадрата повторяются до завершения программы.'''

import pygame as pg
import sys
from matrix import Matrix

pg.init()
x = 40
y = 30
clock = pg.time.Clock()
matrix = Matrix(x, y)
matrix.showPoint(x, y)

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT or (i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                x -= 1
            elif i.key == pg.K_RIGHT:
                x += 1
            elif i.key == pg.K_UP:
                y -= 1
            elif i.key == pg.K_DOWN:
                y += 1
            matrix.showPoint(x, y)
    clock.tick(60)

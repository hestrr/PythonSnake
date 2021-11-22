'''Ваша задача написать код анимации квадрата, который перемещается от
левой границе к правой, касается ее, но не исчезает за ней. После этого
возвращается назад – от правой границы к левой, касается ее, опять двигается
вправо. Циклы движения квадрата повторяются до завершения программы.'''

import pygame as pg
import sys
from matrix import Matrix
from dot import Dot

pg.init()
clock = pg.time.Clock()
matrix = Matrix()
dot = Dot(matrix, 40, 30)
clock.tick(60)


while True:
    for i in pg.event.get():
        if i.type == pg.QUIT or (i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                dot.left()
            elif i.key == pg.K_RIGHT:
                dot.right()
            elif i.key == pg.K_UP:
                dot.up()
            elif i.key == pg.K_DOWN:
                dot.down()

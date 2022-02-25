import sys
import pygame as pg
from matrix import Matrix
from dot import Dot
#from snake import Snake

pg.init()
clock = pg.time.Clock()
matrix = Matrix('Точка')
dot = Dot(matrix, 60, 40)

RIGHT = "right"
LEFT = "left"
UP = 'up'
DOWN = 'down'
STOP = "stop"
motion = STOP

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT or (i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                motion = LEFT
            elif i.key == pg.K_RIGHT:
                motion = RIGHT
            elif i.key == pg.K_UP:
                motion = UP
            elif i.key == pg.K_DOWN:
                motion = DOWN
        elif i.type == pg.KEYUP:
            if i.key in [pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN]:
                motion = STOP

    if motion == LEFT:
        dot.left()
    elif motion == RIGHT:
        dot.right()
    elif motion == UP:
        dot.up()
    elif motion == DOWN:
        dot.down()

    clock.tick(60)

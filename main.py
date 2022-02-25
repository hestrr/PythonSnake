import sys
import pygame as pg
from matrix import Matrix
from dot import Dot
from time import sleep
#from snake import Snake

pg.init()
clock = pg.time.Clock()
matrix = Matrix('Точка', 70, 50)
dot = Dot(matrix, 70, 50)

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
        sleep(0.05)
    elif motion == RIGHT:
        dot.right()
        sleep(0.05)
    elif motion == UP:
        dot.up()
        sleep(0.05)
    elif motion == DOWN:
        dot.down()
        sleep(0.05)

    clock.tick(60)

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

r = 30
x = WIN_WIDTH // 2
y = WIN_HEIGHT // 2

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT or (i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()
    sc.fill(BLACK)
    pg.draw.circle(sc, ORANGE, (x, y), r)
    pg.display.update()

    if x >= WIN_WIDTH + r:
        x = 0 - r
    else:
        x += 2

    clock.tick(60)

import pygame as pg
import time


class Matrix:
    def __init__(self, x, y):
        pg.init()
        WIN_WIDTH = 600
        WIN_HEIGHT = 400
        self.ORANGE = (255, 150, 100)
        self.BLACK = (0, 0, 0)
        self.sc = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pg.display.set_caption('aaa')

        self.w_rect = 50
        self.h_rect = 50

    def showPoint(self, x, y):
        pg.draw.rect(self.sc, self.ORANGE,
                     (x*10, y*10, self.w_rect, self.h_rect))
        pg.display.update()

    def hidePoint(self, x, y):
        pg.draw.rect(self.sc, self.BLACK,
                     (x*10, y*10, self.w_rect, self.h_rect))
        pg.display.update()

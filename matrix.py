import pygame as pg


class Matrix:
    def __init__(self, headerText):
        pg.init()
        WIN_WIDTH = 800
        WIN_HEIGHT = 420
        self.ORANGE = (255, 150, 100)
        self.BLACK = (0, 0, 0)
        self.GREY = (200, 200, 200)
        self.sc = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pg.draw.rect(self.sc, self.GREY,
                     (84, 4, WIN_WIDTH-189, WIN_HEIGHT-10), 10)
        pg.display.update()
        pg.display.set_caption(headerText)

        self.w_rect = 10
        self.h_rect = 10
        self.quotient = 10

    def showPoint(self, x, y):
        pg.draw.rect(self.sc, self.ORANGE,
                     (x*self.quotient+90, y*self.quotient+10, self.w_rect, self.h_rect))
        pg.display.update()

    def hidePoint(self, x, y):
        pg.draw.rect(self.sc, self.BLACK,
                     (x*self.quotient+90, y*self.quotient+10, self.w_rect, self.h_rect))
        pg.display.update()

    '''def showSnake(self, x, y, length):
        for i in range(0, length):
            pg.draw.rect(self.sc, self.WHITE,
                         (x*self.quotient, y*self.quotient, self.w_rect, self.h_rect))
            x += 1'''

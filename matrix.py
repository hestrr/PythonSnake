import pygame as pg


class Matrix:
    def __init__(self, headerText, size_x, size_y):
        pg.init()
        self.w_rect = self.h_rect = self.quotient = 10
        self.margin = 10
        self.border = 10
        WIN_WIDTH = (size_x+self.margin*2)*self.quotient
        WIN_HEIGHT = size_y*self.quotient+self.border*2
        self.ORANGE = (255, 150, 100)
        self.BLACK = (0, 0, 0)
        self.GREY = (192, 192, 192)
        self.sc = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pg.draw.rect(self.sc, self.GREY,
                     ((WIN_WIDTH-size_x*self.quotient)//2-6, self.border//2-1,
                      size_x*self.quotient+self.border+1, size_y*self.quotient+self.border),
                     self.border)
        pg.display.update()
        pg.display.set_caption(headerText)

    def showPoint(self, x, y):
        pg.draw.rect(self.sc, self.ORANGE,
                     ((x+self.margin-self.border)*self.quotient, (y+self.margin)*self.quotient,
                      self.w_rect, self.h_rect))
        pg.display.update()

    def hidePoint(self, x, y):
        pg.draw.rect(self.sc, self.BLACK,
                     ((x+self.margin-self.border)*self.quotient, (y+self.margin)*self.quotient, self.w_rect, self.h_rect))
        pg.display.update()

    '''def showSnake(self, x, y, length):
        for i in range(0, length):
            pg.draw.rect(self.sc, self.WHITE,
                         (x*self.quotient, y*self.quotient, self.w_rect, self.h_rect))
            x += 1'''

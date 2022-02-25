class Dot:
    def __init__(self, matrix, size_x, size_y):
        self.matrix = matrix
        self.size_x = size_x
        self.size_y = size_y
        self.x = self.x_old = size_x//2
        self.y = self.y_old = size_y//2
        matrix.showPoint(self.x, self.y)

    def left(self):
        if self.x == 0:
            return
        self.x -= 1
        self.__refresh__()

    def right(self):
        if self.x == self.size_x-1:
            return
        self.x += 1
        self.__refresh__()

    def up(self):
        if self.y == 0:
            return
        self.y -= 1
        self.__refresh__()

    def down(self):
        if self.y == self.size_y-1:
            return
        self.y += 1
        self.__refresh__()

    def __refresh__(self):
        self.matrix.hidePoint(self.x_old, self.y_old)
        self.matrix.showPoint(self.x, self.y)
        self.x_old = self.x
        self.y_old = self.y

class Dot:
    def __init__(self, matrix, x_start, y_start, size_x, size_y):
        matrix.showPoint(x_start, y_start)

        self.matrix = matrix
        self.x = self.x_old = x_start
        self.y = self.y_old = y_start
        self.size_x = size_x
        self.size_y = size_y

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

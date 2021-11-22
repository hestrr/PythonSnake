class Dot:
    def __init__(self, matrix, x_start, y_start):
        matrix.showPoint(x_start, y_start)

        self.matrix = matrix
        self.x = self.x_old = x_start
        self.y = self.y_old = y_start

    def left(self):
        self.x -= 1
        self.__refresh__()

    def right(self):
        self.x += 1
        self.__refresh__()

    def up(self):
        self.y -= 1
        self.__refresh__()

    def down(self):
        self.y += 1
        self.__refresh__()

    def __refresh__(self):
        self.matrix.hidePoint(self.x_old, self.y_old)
        self.matrix.showPoint(self.x, self.y)
        self.x_old = self.x
        self.y_old = self.y

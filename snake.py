class Snake:
    def __init__(self, matrix, x, y, length):
        matrix.showSnake(x, y, 5, length)
        self.body = [0]*length

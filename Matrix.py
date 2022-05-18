import random


class Matrix:

    def __init__(self, size_x=1, size_y=1, rnd=100):
        self.matrix = [[0] * size_y for i in range(size_x)]
        self.rnd = rnd

    def random_filling(self):
        for i in range(0, self.size_x):
            for j in range(0, self.size_y):
                self.matrix[i][j] = random.randint(0, self.rnd)

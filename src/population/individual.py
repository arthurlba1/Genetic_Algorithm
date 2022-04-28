"""Handles individual of algorithm"""


class Individual:

    def __init__(
        self,
        x1: float,
        x2: float,
        x3: float,
        x4: float,
        x5: float,
    ):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.fitness = (self.x5**5)+(self.x4**4)+(self.x3**3)+(self.x2**2)+(self.x1**1)

    def __str__(self):
        return f'Individual = x1: {self.x1} - ' \
               f'x2: {self.x2} - ' \
               f'x3: {self.x3} - ' \
               f'x4: {self.x4} - ' \
               f'x5: {self.x5} - ' \
               f'Fitness: {self.fitness}'

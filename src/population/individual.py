"""Handles individual of algorithm"""


class Individual:

    def __init__(
        self,
        x1: int,
        x2: int,
        x3: int,
        x4: int,
        x5: int,
    ):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.fitness = (self.x5**5)+(self.x4**4)+(self.x3**3)+(self.x2**2)+(self.x1**1)

    def __str__(self):
        return f'Individual = {self.fitness}'

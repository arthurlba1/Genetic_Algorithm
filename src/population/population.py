"""Handles individual of algorithm"""
import random

from individual import Individual


class Population(Individual):


    def generate_population(size: int):
        cont = 0
        population = []
        while cont < size:
            x1 = random.random()
            x2 = random.random()
            x3 = random.random()
            x4 = random.random()
            x5 = random.random()
            population.append(Individual(x1, x2, x3, x4, x5).__str__())
            cont = cont + 1
        return population




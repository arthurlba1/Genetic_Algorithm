"""Handles individual of algorithm"""
import random
from typing import List

from pyrfc3339 import generate

from individual import Individual


class Population(Individual):


    def generate_population(size: int) -> List[str]:
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
            population.sort(reverse = True)
        return population

    def three_best_individuals(array: List[str]) -> List[str]:
        three_best = []
        
        for i in range(3):   
            three_best.append(array[i])
        
        return three_best

    def new_generation():
        population = []

population = Population.generate_population(10)
population_elite = Population.three_best_individuals(population)
print(population_elite)
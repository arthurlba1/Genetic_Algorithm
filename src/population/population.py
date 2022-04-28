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
            population.append(Individual(x1, x2, x3, x4, x5))
            cont = cont + 1
            population.sort(key=lambda individual: individual.fitness, reverse=True)
        return population

    
    def three_best_individuals(array: List[str]) -> List[str]:
        three_best = []
        
        for i in range(3):   
            three_best.append(array[i])
        
        return three_best

    def new_generation(
        best: List[str],
        mutation_list: List[str],
        crossover_list: List[str]
        ) -> List[str]:
        population = best + mutation_list + crossover_list
        return population

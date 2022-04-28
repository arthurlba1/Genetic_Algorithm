"""Handles individual of algorithm"""
import random
from typing import List


from src.population.individual import Individual


class Population(Individual):

    @staticmethod
    def generate_population(size: int) -> List[Individual]:
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

    @staticmethod
    def three_best_individuals(array: List[str]) -> List[str]:
        three_best = []
        
        for i in range(3):   
            three_best.append(array[i])
        
        return three_best

    @staticmethod
    def new_generation(best: List[str], mutation_list: List[str], crossover_list: List[str]) -> List[str]:
        population = best + mutation_list + crossover_list
        return population

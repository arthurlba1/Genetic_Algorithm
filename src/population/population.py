"""Handles individual of algorithm"""
import random
from typing import List


from src.population.individual import Individual


class Population(Individual):

    @staticmethod
    def generate_population(size: int, interval: List[int]) -> List[Individual]:
        cont = 0
        population = []
        while cont < size:
            x1 = random.uniform(interval[0], interval[1])
            x2 = random.uniform(interval[0], interval[1])
            x3 = random.uniform(interval[0], interval[1])
            x4 = random.uniform(interval[0], interval[1])
            x5 = random.uniform(interval[0], interval[1])
            population.append(Individual(x1, x2, x3, x4, x5))
            cont = cont + 1
            population.sort(key=lambda individual: individual.fitness, reverse=True)
        return population

    @staticmethod
    def three_best_individuals(array: List[Individual]) -> List[Individual]:
        three_best = []
        for i in range(3):   
            three_best.append(array[i])
        return three_best

    @staticmethod
    def new_generation(best: List[Individual], mutation_list: List[Individual], crossover_list: List[Individual]) -> List[Individual]:
        population = best + mutation_list + crossover_list
        return population

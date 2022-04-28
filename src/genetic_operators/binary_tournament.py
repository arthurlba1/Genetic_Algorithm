"""Create a tournament of two individuals"""
from typing import List
import random

from src.helpers.mutation_case import MutationCase
from src.population.individual import Individual
from src.population.population import Population


class BinaryTournament:
    
    def select_tournament(population: Population, mutation_rate: int) -> List[str]:
        crossover_individuals = []
        for i in range(int(len(population-3)*(100-mutation_rate)/100)):
            individual_one = random.choice(population)
            individual_two = random.choice(population)
            x1 = individual_one.x1
            x2 = individual_one.x2
            x3 = individual_one.x3
            x4 = individual_two.x4
            x5 = individual_two.x5
            crossover_individuals.append(Individual(x1, x2, x3, x4, x5))
        return crossover_individuals
    
    def mutation(population: Population, mutation_rate):
        mutation_list = []
        for i in range(int(len(population-3)*mutation_rate/100)):
            individual = random.choice(population)
            mutation_one = random.randint(1,5)
            print(f'{individual} before')
            individual = MutationCase.mutation_case_elseif(mutation_one, individual)
            print(f'{individual} after')
            mutation_list.append(individual)
        return mutation_list

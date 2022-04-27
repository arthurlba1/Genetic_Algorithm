"""handles mutation case"""
import random

from src.population.individual import Individual


class MutationCase:

    @staticmethod
    def mutation_case_elseif(comparator: int, individual: Individual):
        if comparator == 1:
            individual.x1 = random.random()
            return individual
        elif comparator == 2:
            individual.x2 = random.random()
            return individual
        elif comparator == 3:
            individual.x3 = random.random()
            return individual
        elif comparator == 4:
            individual.x4 = random.random()
            return individual
        elif comparator == 5:  
            individual.x5 = random.random()
            return individual

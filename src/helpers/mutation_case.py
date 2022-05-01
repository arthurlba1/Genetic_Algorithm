"""handles mutation case"""
from typing import List
import random

from src.population.individual import Individual


class MutationCase:

    @staticmethod
    def mutation_case_elseif(comparator: int, individual: Individual, interval: List[int]) -> Individual:
        if comparator == 1:
            individual.x1 = random.uniform(interval[0], interval[1])
            individual.fitness = (individual.x5**5)+(individual.x4**4)+(individual.x3**3)+(individual.x2**2)+(individual.x1**1)
            return individual
        elif comparator == 2:
            individual.x2 = random.uniform(interval[0], interval[1])
            individual.fitness = (individual.x5**5)+(individual.x4**4)+(individual.x3**3)+(individual.x2**2)+(individual.x1**1)
            return individual
        elif comparator == 3:
            individual.x3 = random.uniform(interval[0], interval[1])
            individual.fitness = (individual.x5**5)+(individual.x4**4)+(individual.x3**3)+(individual.x2**2)+(individual.x1**1)
            return individual
        elif comparator == 4:
            individual.x4 = random.uniform(interval[0], interval[1])
            individual.fitness = (individual.x5**5)+(individual.x4**4)+(individual.x3**3)+(individual.x2**2)+(individual.x1**1)
            return individual
        elif comparator == 5:  
            individual.x5 = random.uniform(interval[0], interval[1])
            individual.fitness = (individual.x5**5)+(individual.x4**4)+(individual.x3**3)+(individual.x2**2)+(individual.x1**1)
            return individual

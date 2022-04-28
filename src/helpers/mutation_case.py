"""handles mutation case"""
import random


class MutationCase:

    @staticmethod
    def mutation_case_elseif(comparator: int, individual: str):
        if comparator == 1:
            individual.x1 = random.random()
            individual.fitness = (individual.x5**5)+(individual.x4**4)+(individual.x3**3)+(individual.x2**2)+(individual.x1**1)
            return individual
        elif comparator == 2:
            individual.x2 = random.random()
            individual.fitness = (individual.x5**5)+(individual.x4**4)+(individual.x3**3)+(individual.x2**2)+(individual.x1**1)
            return individual
        elif comparator == 3:
            individual.x3 = random.random()
            individual.fitness = (individual.x5**5)+(individual.x4**4)+(individual.x3**3)+(individual.x2**2)+(individual.x1**1)
            return individual
        elif comparator == 4:
            individual.x4 = random.random()
            individual.fitness = (individual.x5**5)+(individual.x4**4)+(individual.x3**3)+(individual.x2**2)+(individual.x1**1)
            return individual
        elif comparator == 5:  
            individual.x5 = random.random()
            individual.fitness = (individual.x5**5)+(individual.x4**4)+(individual.x3**3)+(individual.x2**2)+(individual.x1**1)
            return individual

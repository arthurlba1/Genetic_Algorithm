""" Genetic Algorithm to find maximum point of a function. """
#import matplotlib.pyplot as plt

from src.function.input import InputAlgorithm
from src.genetic_operators.binary_tournament import BinaryTournament
from src.population.population import Population


class GeneticAlgorithm:
    """Genetic algorithm."""

    @staticmethod
    def start_population(
        population=InputAlgorithm.POPULATION_SIZE,
        mutation_rate=InputAlgorithm.MUTATION_RATE,
        number_generations=InputAlgorithm.NUMBER_GENERATIONS
    ):

        current_generation = Population.generate_population(population)
        best_generation = []
        for i in range(number_generations):
            three_best = Population.three_best_individuals(current_generation)
            best_generation.append(three_best[0].fitness)
            print(three_best[0].__str__())
            crossover = BinaryTournament.select_tournament(population=current_generation, mutation_rate=mutation_rate)
            mutation = BinaryTournament.mutation(population=current_generation, mutation_rate=mutation_rate)
            current_generation = Population.new_generation(
                best=three_best,
                mutation_list=mutation,
                crossover_list=crossover
            )


GeneticAlgorithm.start_population()

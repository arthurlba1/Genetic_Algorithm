""" Genetic Algorithm to find maximum point of a function. """
import sys
sys.path.insert(0, '../src/genetic_operators')

from input import InputAlgorithm
from src.genetic_operators.binary_tournament import BinaryTournament
from population.population import Population


class GeneticAlgorithm:
    """Genetic algorithm."""

    def start_population(
        population: int,
        mutation_rate: int,
        number_generations: int,
    ):
        population = InputAlgorithm.POPULATION_SIZE
        mutation_rate = InputAlgorithm.MUTATION_RATE
        number_generations = InputAlgorithm.NUMBER_GENERATIONS

        current_generation = Population.generate_population(population)
        best_generation = []
        for i in range(number_generations):
            three_best = Population.three_best_individuals(current_generation)
            best_generation.append(three_best[0].fitness)
            print(three_best[0].__str__())
            crossover = BinaryTournament.select_tournament(current_generation, mutation_rate)
            mutation = BinaryTournament.mutation(current_generation, mutation_rate)
            current_generation = Population.new_generation( three_best, mutation, crossover)
        
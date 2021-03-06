""" Genetic Algorithm to find maximum point of a function. """

from src.function.input import InputAlgorithm
from src.function.render_graphic.plot_graphic import GraphFunctionGeneticAlgorithm
from src.genetic_operators.binary_tournament import BinaryTournament
from src.population.population import Population


class GeneticAlgorithm:
    """Genetic algorithm."""

    @staticmethod
    def start_population(
        population=InputAlgorithm.POPULATION_SIZE,
        mutation_rate=InputAlgorithm.MUTATION_RATE,
        number_generations=InputAlgorithm.NUMBER_GENERATIONS,
        search_interval=InputAlgorithm.SEARCH_RANGE
    ):

        current_generation = Population.generate_population(size=population, interval=search_interval)
        history = []
        for i in range(number_generations):
            elitism = Population.elitism_of_three(current_generation)
            history.append(elitism[0].fitness)
            print(elitism[0].__str__())
            crossover = BinaryTournament.select_tournament(population=current_generation, mutation_rate=mutation_rate)
            mutation = BinaryTournament.mutation(
                population=current_generation,
                mutation_rate=mutation_rate,
                interval=search_interval
            )
            current_generation = Population.new_generation(
                best=elitism,
                mutation_list=mutation,
                crossover_list=crossover
            )
        GraphFunctionGeneticAlgorithm.plot_fx_graph(arr=history)


GeneticAlgorithm.start_population()

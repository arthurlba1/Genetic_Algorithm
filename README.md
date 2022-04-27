# Genetic Algorithm

Genetic Algorithms to find the maximum point of a
function in the form _F(x1,x2,x3,x4,x5) = y_.

##### Genetic algorithm inputs
- Search range
- Mutation rate
- Population
- Number of genetions

>Function must be entered at implementation level.

>Search Range: the same applied for all values ​​of x.

##### Algorithm output
- Function _F(x)_
- _x1, x2, x3,x4_ and _x5_ of the best individual in each generation

## Binary tournament selection
Two individuals are drawn at random, their aptitudes are compared and the fittest of these two is selected. This procedure is repeated for
each individual to be selected.

## Crossover
The crossover system takes two individuals from the generation and changes their 'DNA' or in this case their function values.
As there are 5 values, it's divided in half and creates a child with half of each parent individual

~~~python
    crossover_individuals = []
        for i in range(int(len(population)*(100-mutation_rate)/100)):
            individual_one = random.choice(population)
            individual_two = random.choice(population)
            x1 = individual_one.x1
            x2 = individual_one.x2
            x3 = individual_one.x3
            x4 = individual_two.x4
            x5 = individual_two.x5
            crossover_individuals.append(Individual(x1, x2, x3, x4, x5))
~~~

## Mutation
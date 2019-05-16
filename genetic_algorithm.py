# Copyright (C) 2019 "Daniel Bramblett" <daniel.r.bramblett@gmail.com>

import numpy as np
import random
from board_state import BoardState


# The instance that is the genetic algorithm which manages the population each generation and performs the crossover
# and mutation operation.
class GeneticAlgorithm:
    # The size of the population each generation.
    population_size = 0
    # The number of rows of the N-Queens problem. Note that this also the number of of columns.
    number_of_rows = 8
    # The list of the average fitness score for each generation.
    average_fitness_per_generation = list()
    # The list containing each member of the population.
    population = None
    # The list containing the new members generated during the current generation.
    new_population = None
    # The weight of the mutation rate used to weight the random pick.
    weights = None
    # The number of members checked for the tournament selection.
    tournament_size = 4

    # Initializes the fields in the class using the default or passed-in parameters. The initial population is then
    # randomly generated.
    def __init__(self, pop_size=100, mutation_rate=0.01, row_numb=8, tournament_size=4):
        self.population_size = pop_size
        self.number_of_rows = row_numb
        self.weights = [1 - mutation_rate, mutation_rate]
        self.generation_samples = list()
        self.tournament_size = tournament_size

        self.population = [BoardState(number_of_rows=self.number_of_rows) for _ in range(self.population_size)]
        self.population.sort(reverse=True)

    # Mutation operator that takes two indexes in the permutation and swaps them.
    def __mutation_operator__(self, child):
        swap_targets = random.sample(range(self.number_of_rows), 2)
        temp = child.state[swap_targets[0]]
        child.state[swap_targets[0]] = child.state[swap_targets[1]]
        child.state[swap_targets[1]] = temp

    # This function takes a state for the children. It then randomly decides if the child gets mutated or not. If the
    # child is going to be mutated, the child is initialized and passed into the mutation operator to perform the
    # mutation. Otherwise, the child is initialized and added to the new population without being mutated.
    def __consider_mutate__(self, child_state):
        if random.choices([0, 1], self.weights, k=1)[0]:
            child = BoardState(child_state)
            self.__mutation_operator__(child)
            self.new_population.append(child)
        else:
            self.new_population.append(BoardState(child_state))

    # Crossover operator that generates two new children using two parents from the current generation.
    def __crossover_operator__(self, parent_a, parent_b):
        first_child_state = parent_a.state.copy()
        second_child_state = parent_b.state.copy()
        indices_used = list()

        for current_index in range(self.number_of_rows):
            if current_index in indices_used:
                break
            if first_child_state[current_index] == second_child_state[current_index]:
                indices_used.append(current_index)
                break
            index_order = list()
            value_order = list()
            index_order.append(current_index)
            value_order.append(first_child_state[current_index])
            search_value = second_child_state[current_index]
            while search_value != value_order[0]:
                found = np.where(first_child_state == search_value)[0][0]
                index_order.append(found)
                value_order.append(search_value)
                search_value = second_child_state[found]
            for current in range(len(index_order) - 1):
                first_child_state[index_order[current + 1]] = second_child_state[index_order[current - 1]] = value_order[current]

            first_child_state[index_order[0]] = value_order[-1]
            second_child_state[index_order[len(index_order) - 2]] = value_order[-1]

            while len(index_order) > 0:
                indices_used.append(index_order.pop(0))

        self.__consider_mutate__(first_child_state)
        self.__consider_mutate__(second_child_state)

    # Uses tournament selection to select a member of the population as a parent.
    def __select_parent__(self):
        return self.population[min(random.sample(range(self.population_size), self.tournament_size))]

    # Uses the current generation to generate the next generation.
    def generate_next_generation(self):
        self.new_population = list()
        while len(self.new_population) < self.population_size:
            self.__crossover_operator__(self.__select_parent__(), self.__select_parent__())
        if len(self.new_population) > self.population_size:
            self.new_population.pop()
        self.population = self.new_population
        self.population.sort(reverse=True)

    # Current generation statistics.
    def generation_statistics(self):
        average_fitness = 0
        max_fitness = 0
        # Goes through each member of the population and calculates the average fitness while keeping track of the
        # highest fitness score observed.
        for current_member in self.population:
            average_fitness += current_member.fitness_value
            if current_member.fitness_value > max_fitness:
                max_fitness = current_member.fitness_value
        return average_fitness / self.population_size, max_fitness

    # This function finds the member of the population with the highest fitness score and returns it.
    def top_member(self):
        # Initially assumes that the first member of the population has the highest fitness score and saves its index
        # and fitness score.
        current_top_fitness = self.population[0].fitness_value
        current_top_index = list()
        current_top_index.append(0)
        # Goes through each member of the population and checks there fitness score against the current top. If it's
        # higher, the current member becomes the new top member and the fitness score and list of top indexes is
        # updated.
        # If the fitness score is equal to the top fitness score, the index is saved as a tie for the top fitness score.
        for current_member in range(1, self.population_size):
            if current_top_fitness < self.population[current_member].fitness_value:
                current_top_index.clear()
                current_top_index.append(current_member)
                current_top_fitness = self.population[current_member].fitness_value
            elif current_top_fitness == self.population[current_member].fitness_value:
                current_top_index.append(current_member)
        # From the list of top fitness score members, one is randomly chosen to be returned as a reference.
        return self.population[random.choice(current_top_index)]
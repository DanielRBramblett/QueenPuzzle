# Copyright (C) 2019 "Daniel Bramblett" <daniel.r.bramblett@gmail.com>

from genetic_algorithm import GeneticAlgorithm
import matplotlib.pyplot as plt

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 6:
        print("Please run this program with 5 parameters: population size, mutation rate, N, tournament size,\n")
        print("and number of generations.")
        exit()
    ga = GeneticAlgorithm(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    average_fitness_list = list()
    max_fitness_list = list()

    # Generation 0 statistics.
    average_fit, max_fit = ga.generation_statistics()
    average_fitness_list.append(average_fit)
    max_fitness_list.append(max_fit)

    # Generates each generation and calculates the average and max fitness score of the generation.
    for _ in range(int(sys.argv[5])):
        ga.generate_next_generation()
        average_fit, max_fit = ga.generation_statistics()
        average_fitness_list.append(average_fit)
        max_fitness_list.append(max_fit)

    x = list(range(int(sys.argv[5]) + 1))
    plt.plot(x, average_fitness_list, '-b')
    plt.plot(x, max_fitness_list, '-r')
    plt.show()

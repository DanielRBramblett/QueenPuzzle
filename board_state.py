# Copyright (C) 2019 "Daniel Bramblett" <daniel.r.bramblett@gmail.com>

import numpy as np


# The class representing a given board state of the N-Queens problem.
class BoardState:
    # The N-length array representing the location of a queen on each row.
    state = None
    # The fitness value of this state calculated by the fitness function.
    fitness_value = 0
    # The size of N.
    row_size = 0

    # This is the fitness function used to calculate the fitness for a given state. The chosen fitness function
    # checks each connection between each queen to make sure they are aren't diagonal nor on the same row/column. For
    # each connection that this is true, the fitness score increase by one.
    def __fitness_calculate__(self):
        self.fitness_value = 0
        for current_row in range(self.row_size - 1):
            for test_row in range(current_row + 1, self.row_size):
                if self.state[current_row] != self.state[test_row] and abs(test_row - current_row) != abs(
                        self.state[test_row] - self.state[current_row]):
                    self.fitness_value += 1

    # The constructor of the current state which can take in a given state (an array representing where the queen is
    # on each row) and the number of rows. If no state is provided, a random one is generated. For both, the fitness
    # score is calculated with the fitness function.
    def __init__(self, new_state=None, number_of_rows=8):
        if new_state is not None:
            if isinstance(new_state,np.ndarray):
                self.state = new_state
            else:
                self.state = np.array(new_state)
            self.row_size = len(self.state)
        else:
            self.state = np.arange(number_of_rows)
            np.random.shuffle(self.state)
            self.row_size = number_of_rows

        self.__fitness_calculate__()

    # This function prints the board of the given state out to the user.
    def print_board(self):
        for current_row in range(self.row_size):
            temp = ''
            for print_row in range(self.row_size):
                if print_row == self.state[current_row]:
                    temp += '1'
                else:
                    temp += '0'
            print(temp)

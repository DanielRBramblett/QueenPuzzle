# Copyright (C) 2019 "Daniel Bramblett" <daniel.r.bramblett@gmail.com>

from unittest import TestCase
from board_state import BoardState
import numpy as np


class TestBoardStates(TestCase):
    def setUp(self):
        # Generates a board that is a solution to the N-Queens Problem.
        np.random.seed(1028)
        self.perfect_board = BoardState()

        # Generates a board that all the queens are on the main diagonal.
        np.random.seed(34090)
        self.imperfect_board = BoardState()

        # Generates a smaller board.
        np.random.seed(1000)
        self.smaller_board = BoardState(number_of_rows=4)

        # Generates a larger board.
        np.random.seed(42)
        self.larger_board = BoardState(number_of_rows=9)

        # Generates a 4-by-4 board given a state.
        self.set_board = BoardState(new_state=[2, 4, 1, 3])


class TestConstructor(TestBoardStates):
    def test_state(self):
        self.assertListEqual(self.perfect_board.state.tolist(), [5, 2, 4, 6, 0, 3, 1, 7])
        self.assertListEqual(self.imperfect_board.state.tolist(), [0, 1, 2, 3, 4, 5, 6, 7])
        self.assertListEqual(self.smaller_board.state.tolist(), [2, 1, 0, 3])
        self.assertListEqual(self.larger_board.state.tolist(), [7, 1, 5, 0, 8, 2, 4, 3, 6])
        self.assertListEqual(self.set_board.state.tolist(), [2, 4, 1, 3])

    def test_fitness_value(self):
        self.assertEqual(self.perfect_board.fitness_value, 28)
        self.assertEqual(self.imperfect_board.fitness_value, 0)
        self.assertEqual(self.smaller_board.fitness_value, 2)
        self.assertEqual(self.larger_board.fitness_value, 30)
        self.assertEqual(self.set_board.fitness_value, 6)

    def test_row_size(self):
        self.assertEqual(self.perfect_board.row_size, 8)
        self.assertEqual(self.imperfect_board.row_size, 8)
        self.assertEqual(self.smaller_board.row_size, 4)
        self.assertEqual(self.larger_board.row_size, 9)
        self.assertEqual(self.set_board.row_size, 4)

    def test_greater_then(self):
        self.assertTrue(
            self.larger_board > self.perfect_board > self.set_board > self.smaller_board > self.imperfect_board)
        self.assertFalse(self.perfect_board > self.larger_board)

    def test_less_then(self):
        self.assertTrue(
            self.imperfect_board < self.smaller_board < self.set_board < self.perfect_board < self.larger_board)
        self.assertFalse(self.larger_board < self.perfect_board)

    def test_equality(self):
        self.assertTrue(self.imperfect_board == self.imperfect_board)
        self.assertFalse(self.imperfect_board == self.larger_board)
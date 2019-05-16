# QueenPuzzle
Solving the N-Queen Problem using a genetic algorithm with permutation chromosomes.

## Instructions Using main.py
The file main.py is setup to take in the parameters for the genetic algorithm and graph the statistics on each generation. To run this program this way requires the following steps:
1. Clone the repository.
2. Run the file using the command <code> python main.py [population size] [mutation rate] [size of N] [tournament sizes] [number of generations] </code>
    
    For example, to attempt to solve the 50-Queens Problem with a population of 100, 5% mutation rate, tournament sizes of 10, and 1000 generations, the command would look like:
    <code> python main.py 100 0.05 50 10 1000 </code>
    
    Currently, all five parameters must be inputted.

## Instructions Without main.py
The GeneticAlgorithm class be instantiated using a constructor that uses default or provided parameters. The methods available to be used are:

<code>generate_next_generation()</code> -Generates the next generation using the parameters.
<code>generation_statistics()</code> -Returns the average fitness score and maximum fitness score of the current generation as a tuple.
<code>top_member()</code> -Returns a reference to the board state with the highest fitness score. Ties are broken at random.

## Further Detail About Algorithm
### Fitness Function
The fitness function used to score each member calculated the number of edges between queens that isn't along diagonals, rows, or columns of the board. This means the maximum fitness for a given N-Queens Problem would be (-n + n^2)/2.

For example, a solution to the classic 8-Queens Problem would have a fitness score of 28.
### Parent Selection
Parents are selected using tournament selection with the hyperparameter of the size of the tournament. 
### Crossover Operator
To preserve information about both parents, cycles are created using indices and queen locations from both parents. Starting with the first row that hasn't been compared, both parent's location of the queen on that row is compared. 
If it's the same, both children will also have the queen on that location. Otherwise, a cycle is created by finding the location in the first parent of the queen on that column that the second parent had.
Then the value the second parent has at that location is used to repeat the process till the first value is found. This will create a cycle. One child has all the values on this cycle shifted clockwise while the other is shifted counterclockwise.
### Mutation Operator
Two random indices in the permutation are picked and then flipped.

## Copyright ##
Copyright (C) 2018 "Daniel Bramblett" <code>&lt;daniel.r.bramblett@gmail.com&gt;</code>
import timeit


class PuzzleStatistics(object):

    def __init__(self, puzzle_world):
        self.world = puzzle_world

    def bulk_solve(self, number_of_puzzles, h_type):
        """
        Perform a simulation of solving many puzzles at once (using given h type).
        """
        # Prepare timer
        timer_start = timeit.default_timer()
        # Do simulation
        solved_n = 0
        for i in range(1,number_of_puzzles+1):
            print("ITERATION %d") % i
            if self.world.solve_random_puzzle(h_type):
                solved_n += 1
        # Count execution time
        timer_stop = timeit.default_timer()
        timer_duration = round(timer_stop - timer_start,3)
        # Show statistics
        print('=====h%s: BULK RUN STATS=====') % h_type
        print('Total execution time: ' + str(timer_duration) + ' s')
        print('Total puzzles: %d') % number_of_puzzles
        print('Total solved puzzles: %d') % solved_n
        effectivity = (float(solved_n)/number_of_puzzles)*100
        print('Percentual efficiency of the algorithm: '+str(effectivity)+' %')

    def solve_and_compare_bulk(self, number_of_puzzles):
        """
        Compare both heuristics by performing a simulation.
        """
        # Prepare timer
        timer_start = timeit.default_timer()
        # Prepare variables
        solved_data = []
        min_moves = []
        # h1
        solved_data.append([])          # index 0
        solved_data[0].append([])
        solved_data[0].append([])
        solved_data[0][0] = 0.0         # Solved puzzles count
        solved_data[0][1] = 0.0         # Sum of number of moves count
        min_moves.append(float('inf'))  # min. number of moves for solution
        # h2
        solved_data.append([])          # index 1
        solved_data[1].append([])
        solved_data[1].append([])
        solved_data[1][0] = 0.0         # Solved puzzles count
        solved_data[1][1] = 0.0         # Sum of number of moves count
        min_moves.append(float('inf'))
        # Do a simulation
        for i in range(1,number_of_puzzles+1):
            print("ITERATION %d") % i
            # Generate a random start state
            puzzle = self.world.generate_start_state();
            # h1
            solution_path = self.world.solve_given_puzzle(puzzle, 1)
            if solution_path:
                sol_path_len = len(solution_path)-1
                solved_data[0][0] += 1
                solved_data[0][1] += sol_path_len
                if sol_path_len < min_moves[0]:
                    min_moves[0] = sol_path_len
            # h2
            solution_path = self.world.solve_given_puzzle(puzzle, 2)
            if solution_path:
                sol_path_len = len(solution_path)-1
                solved_data[1][0] += 1
                solved_data[1][1] += sol_path_len
                if sol_path_len < min_moves[1]:
                    min_moves[1] = sol_path_len
        # Count execution time
        timer_stop = timeit.default_timer()
        timer_duration = round(timer_stop - timer_start,3)
        # Calculate statistics
        print('=======BULK COMPARE=======')
        print('Total execution time: ' + str(timer_duration) + ' s')
        # h1
        print('===H1===')
        solved_percentage = round((solved_data[0][0]/number_of_puzzles) * 100, 2)
        print('Solved percentage: %d/%d = ' + str(solved_percentage) + ' %%') % (solved_data[0][0], number_of_puzzles)
        if int(solved_data[0][0]) == 0:
            avg_efficiency = 0
        else:
            avg_efficiency = int(solved_data[0][1]/solved_data[0][0])
        print('Average efficiency: %d/%d = ' + str(avg_efficiency) + ' moves') % (solved_data[0][1], solved_data[0][0])
        if min_moves[0] == float('inf'):
            min_moves[0] = 0
        print('Minimal number of moves to a solution: %d') % min_moves[0]
        # h2
        print('===H2===')
        solved_percentage = round((solved_data[1][0]/number_of_puzzles) * 100, 2)
        print('Solved percentage: %d/%d = ' + str(solved_percentage) + ' %%') % (solved_data[1][0], number_of_puzzles)
        if int(solved_data[1][0]) == 0:
            avg_efficiency = 0
        else:
            avg_efficiency = int(solved_data[1][1]/solved_data[1][0])
        print('Average efficiency: %d/%d = ' + str(avg_efficiency) + ' moves') % (solved_data[1][1], solved_data[1][0])
        if min_moves[1] == float('inf'):
            min_moves[1] = 0
        print('Minimal number of moves to a solution: %d') % min_moves[1]

from QueenHeuristic import QueenHeuristic
from StatesCreator import StatesCreator


class ChessQueenWorld(object):

    def __init__(self, file_paths):
        # Absolute file paths to input and output directories.
        self.file_paths = file_paths
        # Heuristic object
        self.heuristic = QueenHeuristic()
        # States creator object
        self.states_creator = StatesCreator()
        # Constants
        self.max_iter_count = 500

    def bulk_solve(self, boards_n):
        # Prepare variables for statistics
        steps_sum = 0.0
        solved_n = 0
        unsolved_boards = []
        # Generate and solve some boards
        for i in range(0, boards_n):
            print('=====Board n. %d=====') % boards_n
            (sol_path, start_state) = self.solve_random_board()
            self.heuristic.show_board(start_state)
            if sol_path:
                solved_n += 1
                steps_sum += len(sol_path)
            else:
                unsolved_boards.append(start_state)
        # Show statistics
        avg_steps_c = steps_sum / boards_n
        percent_solved = (float(solved_n) / boards_n) * 100
        print('Number of generated boards: %d') % boards_n
        print('Number of solved boards: %d ... ' + str(percent_solved) + ' %%') % solved_n
        print('Average number of steps for solution: ' + str(avg_steps_c))


    def solve_random_board(self):
        gen_state = self.states_creator.generate_random_start_state()
        #self.heuristic.show_board(gen_state)
        sol_path = self._solve_given_board(gen_state)
        if sol_path:
            solution = sol_path
        else:
            solution = False
        #self._show_solution(sol_path)
        return solution, gen_state

    def solve_sample_board(self, num):
        gen_state = self.states_creator.get_sample_start_state(num)[0]
        sol_path = self._solve_given_board(gen_state)
        self._show_solution(sol_path)

    def _show_solution(self, solution_path):
        print('>>>>Solution<<<<')
        print('Number of iterations: %d') % (len(solution_path) - 1)
        print('Final state: ')
        self._show_board(solution_path[-1])
        print('{n. of conflists: %d}') % self.heuristic.count_total_conflicts(solution_path[-1])

    def _solve_given_board(self, start_state):
        # Prepare variables
        solution_path = []
        current_state = start_state
        conf_count = self.heuristic.count_total_conflicts(current_state)
        solution_path.append(current_state)
        # Repeat until there are no conflicts.
        iter_n = 0
        while conf_count > 0:
            if iter_n > self.max_iter_count:
                return False
            iter_n += 1
            print ('========iter. %d========') % iter_n
            # Create a new state from current state.
            new_state = self.heuristic.choose_min_conflict_positions(current_state)
            # Check if the new state is alredy in solution path.
            if new_state in solution_path:
                continue # If yes, re-run the method.
            # If not, it's part of solution.
            conf_count = self.heuristic.count_total_conflicts(new_state)
            solution_path.append(new_state)
            current_state = new_state
        # Show solution
        return solution_path

    def _show_board(self, state):
        for row in state:
            print row
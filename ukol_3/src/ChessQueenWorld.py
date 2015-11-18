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

    def solve_random_board(self):
        gen_state = self.states_gen.generate_random_start_state()
        return self._solve_given_board(gen_state)

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
        solution_path.append(current_state)
        # Repeat until there are no conflicts.
        iter_n = 0
        while self.heuristic.count_total_conflicts(current_state) > 0:
            iter_n += 1
            print ('========iter. %d========') % iter_n
            # Get a new state.
            current_state = self.heuristic.choose_min_conflict_positions(current_state)
            # Check if the new state is alredy in solution path.
            if current_state in solution_path:
                continue    # If yes, re-run the method.
            # If not, add it to solution path.
            solution_path.append(current_state)
        # Show solution
        return solution_path

    def _show_board(self, state):
        for row in state:
            print row
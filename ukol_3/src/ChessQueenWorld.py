from QueenHeuristic import QueenHeuristic


class ChessQueenWorld(object):

    def __init__(self, file_paths):
        # Absolute file paths to input and output directories.
        self.file_paths = file_paths
        # Heuristic object
        self.heuristic = QueenHeuristic()
        # Solution path
        self.solution_path = []

    def solve_random_board(self):
        gen_state = self._generate_start_state()
        #self._show_board(gen_state)
        return self._solve_given_board(gen_state)

    def _solve_given_board(self, start_state):
        #print self.heuristic.count_total_conflicts(start_state)
        current_state = start_state
        self.solution_path.append(current_state)
        # Repeat until there are no conflicts.
        while self.heuristic.count_total_conflicts(current_state) > 0:
            pass

    def _move_queen(self, state, start_position, direction, number_of_steps):
        pass

    def _generate_start_state(self):
        state_a = [
            [0,0,0,0,1,0,0,0],
            [1,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0,0],
            [0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0],
            [0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1],
        ]
        return state_a

    def _show_board(self, state):
        for row in state:
            print row
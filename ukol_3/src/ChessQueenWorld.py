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

    def solve_random_board(self):
        gen_state = self.states_creator.generate_random_start_state()
        (sol_path, total_steps) = self._solve_given_board(gen_state)
        solution = sol_path if sol_path else False
        return solution, gen_state, total_steps

    def solve_sample_board(self, num):
        gen_state = self.states_creator.get_sample_start_state(num)[0]
        (sol_path, total_steps) = self._solve_given_board(gen_state)
        self._show_solution(sol_path)

    def _show_solution(self, solution_path):
        print('>>>>Solution<<<<')
        if not solution_path:
            exit('No solution found.')
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
        total_steps = 0
        # Show board
        self._show_board(start_state)
        print('Number of conflicts: %d') % conf_count
        # Repeat until there are no conflicts.
        iter_n = 0
        while conf_count > 0:
            if iter_n > self.max_iter_count:
                return False, 0
            iter_n += 1
            #print ('========iter. %d========') % iter_n
            # Create a new state from current state.
            (new_state, performed_steps) = self.heuristic.choose_min_conflict_positions(current_state)
            # Check if the new state is alredy in solution path.
            if new_state in solution_path:
                continue # If yes, re-run the method.
            # If not, it's part of solution.
            conf_count = self.heuristic.count_total_conflicts(new_state)
            solution_path.append(new_state)
            current_state = new_state
            total_steps += len(performed_steps)
        # Show solution
        print  # blank line
        if solution_path:
            print('>>>Solved in %d steps.') % total_steps
            self._show_board(solution_path[-1])
        else:
            print('<<<NOT solved after %d iterations.') % self.max_iter_count
        # result
        return solution_path, total_steps

    def _show_board(self, state):
        for row in state:
            print row

    def bulk_solve(self, boards_n):
        # Prepare variables for statistics
        steps_sum = 0.0
        solved_n = 0
        unsolved_boards = {}
        solved_stats = {}   # key is number of conflicts in start board
        # Generate and solve some boards
        for i in range(1, boards_n+1):
            print('======Board n. %d======') % i
            # Get and solve random board.
            (sol_path, start_state, total_steps) = self.solve_random_board()
            conf_count = self.heuristic.count_total_conflicts(start_state)
            #self._show_board(start_state)
            # Check if a solution was found.
            if sol_path:
                # Increment common values.
                solved_n += 1
                steps_sum += total_steps
                # Save values for initial conflicts count.
                if conf_count in solved_stats:
                    solved_stats[conf_count][0] += 1
                    solved_stats[conf_count][1] += total_steps
                else:
                    solved_stats[conf_count] = []
                    solved_stats[conf_count].append(1.0)
                    solved_stats[conf_count].append(total_steps)
            else:
                if conf_count in unsolved_boards:
                    unsolved_boards[conf_count].append(start_state)
                else:
                    unsolved_boards[conf_count] = [start_state]
            # blank line
            print
        # Show basic statistics
        avg_steps_c = round(steps_sum / boards_n, 2)
        percent_solved = (float(solved_n) / boards_n) * 100
        print('======BASIC STATS======')
        print('Number of generated boards: %d') % boards_n
        print('Number of solved boards: %d ... ' + str(round(percent_solved, 2)) + ' %%') % solved_n
        print('Average number of steps for solution: ' + str(avg_steps_c))
        # Show detailed statistics
        print('======DETAILED STATS======')
        for conf_count, (solved_count, steps_sum) in sorted(solved_stats.iteritems()):
            print('===%d conflicts===') % conf_count
            avg_steps_c = round(steps_sum / solved_count, 2)
            total_boards = solved_count + len(unsolved_boards.get(solved_count, []))
            percent_solved = (float(solved_count) / total_boards) * 100
            print('Generated boards: %d') % total_boards
            print('Solved boards: %d ... ' + str(round(percent_solved, 2)) + ' %%') % solved_count
            print('Average steps: ' + str(avg_steps_c))

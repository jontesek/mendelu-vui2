import random

from PuzzleHeuristics import PuzzleHeuristics
from PuzzleStatistics import PuzzleStatistics


class PuzzleWorld(object):

    def __init__(self):
        """
        Defines a goal state and initializes basic objects (heuristics, statistics).
        """
        # State representation: tile value => (x,y)
        self.goal_state = {
            'tiles': {
                1: (1,1), 2: (1,2), 3: (1,3),
                8: (2,1), 0: (2,2), 4: (2,3),
                7: (3,1), 6: (3,2), 5: (3,3)
            },
            'moved_tile': None,
            'h_value': 0
        }
        # Basic objects
        self.heuristics = PuzzleHeuristics(self.goal_state)
        self.statistics = PuzzleStatistics(self)

    # MAIN PUBLIC methods
    def solve_given_puzzle(self, start_state, h_type):
        """
        Tries to solve a given puzzle with the selected heuristic.
        Args:
            start_state (Hash)
            h_type (int):
                1 ... MIN number of tiles on wrong positions.
                2 ... MIN sum of manhattan distances from goal posisitions.
        Returns:
            boolean: Whether a solution from the start state has been found or not.
        """
        # Reset solution path (start state -> goal state).
        solution_path = []
        # Add start state to the path.
        solution_path.append(start_state)
        current_state = solution_path[0]
        current_state['h_value'] = self.heuristics.calculate_value(h_type,current_state)
        # Search for a solution.
        while current_state['tiles'] != self.goal_state['tiles']:
            #print "======CUR STATE======"
            #self._show_state(current_state)
            # Find possible moves towards zero tile.
            possible_moves = self._find_possible_moves(current_state)
            # For every move create a new state.
            new_states = self._create_states_from_moves(current_state, possible_moves)
            # Check if the states are valid.
            valid_states = self._get_valid_states(new_states, solution_path)
            if not valid_states:
                print('No solution found in %d moves (using h%d).') % (len(solution_path)-1, h_type)
                return False
            # Calculate heuristics value for every new state.
            for state in valid_states:
                state['h_value'] = self.heuristics.calculate_value(h_type,state)
            # Choose state with the lowest heuristics value.
            best_state = self._get_best_state(valid_states)
            solution_path.append(best_state)
            current_state = best_state
        # Goal state was reached
        print('The goal state was reached in %d moves (using h%d).') % (len(solution_path)-1,h_type)
        #print(solution_path)
        return solution_path

    def solve_random_puzzle(self, h_type):
        """
        Solve a randomly generated puzzle (using given h type).
        """
        result = self.solve_given_puzzle(self.generate_start_state(), h_type)
        return result

    def generate_start_state(self):
        """
        Generates a random start state.
        """
        state_a = {
            'tiles': {
                5: (1,1), 4: (1,2), 0: (1,3),
                6: (2,1), 1: (2,2), 8: (2,3),
                7: (3,1), 3: (3,2), 2: (3,3)
            },
            'moved_tile': None,
            'h_value': None
        }
        random_tiles = {i: None for i in range(0,9)}
        positions_used = []
        i = 0
        while i < 9:
            r_pos = (random.randint(1,3), random.randint(1,3))
            if r_pos not in positions_used:
                positions_used.append(r_pos)
                random_tiles[i] = r_pos
                i += 1
        r_state = {
            'tiles': random_tiles, 'moved_tile': None, 'h_value': None
        }
        print random_tiles
        return r_state

    # PRIVATE working methods
    def _find_possible_moves(self, current_state):
        """
        Returns tiles with which the zero tile can change its position.
        Args:
            current_state (Hash)
        Returns:
            list
        """
        # Get zero tile coordinates
        tile_zero = current_state['tiles'][0]
        # Count new coordinates for 4 movements.
        x_up = tile_zero[0] - 1
        x_down = tile_zero[0] + 1
        y_left = tile_zero[1] - 1
        y_right = tile_zero[1] + 1
        #print tile_zero, x_down, x_up, y_left, y_right
        # Check coordinates
        movable_tiles= []
        if x_up > 0 and x_up <= 3:
            movable_tiles.append((x_up, tile_zero[1]))
        if x_down > 0 and x_down <= 3:
            movable_tiles.append((x_down, tile_zero[1]))
        if y_left > 0 and y_left <= 3:
            movable_tiles.append((tile_zero[0],y_left))
        if y_right > 0 and y_right <= 3:
            movable_tiles.append((tile_zero[0],y_right))
        # Result
        return movable_tiles

    def _create_states_from_moves(self, current_state, possible_moves):
        """
        Create new states from given moves.
        Args:
            current_state (Hash)
            possible_moves: List of tiles with which the zero tile can change its position.
        Returns:
            list: new states
        """
        new_states = []
        zero_tile = current_state['tiles'][0]
        for moved_tile in possible_moves:
            new_zero = moved_tile
            new_move_tile = zero_tile
            new_state = {}
            new_state['tiles'] = current_state['tiles'].copy()
            new_state['tiles'][0] = new_zero
            new_state['tiles'][self._get_tile_name_by_coordinates(current_state, moved_tile)] = new_move_tile
            new_state['moved_tile'] = moved_tile
            new_states.append(new_state)
        # result
        return new_states

    def _get_valid_states(self, new_states, solution_path):
        """
        Eliminate all already visited states (in solution path).
        """
        valid_states = []
        for new_state in new_states:
            ok = True
            for sel_state in solution_path:
                if sel_state['tiles'] == new_state['tiles']:
                    ok = False
                    break
            if ok:
                valid_states.append(new_state)
        # result
        return valid_states

    def _get_best_state(self, valid_states):
        """
        Select a state with the lowest h value.
        [Not implemented: If there are more states with same value, choose the one which will place a non-zero title on the right place.]
        """
        return min(valid_states, key=lambda x: x['h_value'])

    # PUBLIC statistic methods
    def bulk_solve(self, number_of_puzzles, h_type):
        """
        Perform a simulation of solving many puzzles at once (using given h type).
        """
        self.statistics.bulk_solve(number_of_puzzles, h_type)

    def bulk_solve_compare(self, number_of_puzzles):
        """
        Compare both heuristics by performing a simulation.
        """
        self.statistics.solve_and_compare_bulk(number_of_puzzles)

    # HELPER functions
    def _get_tile_name_by_coordinates(self, state, coordinates):
        """
        Given x and y, return tile name from the given state.
        """
        for t_name, xy in state['tiles'].iteritems():
            if xy == coordinates:
                return t_name

    def _show_state(self, state):
        """
        A nice matrix representation of the state could be shown, but it's difficlut :).
        """
        print(state)


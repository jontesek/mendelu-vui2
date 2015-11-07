from Queue import LifoQueue
import random

from PuzzleHeuristics import PuzzleHeuristics


class PuzzleWorld(object):

    def __init__(self):
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
        # Path from start state to goal state
        self.solution_path = []
        # Heuristics type
        #self.h_type = 1 # MIN number of tiles on wrong positions.
        self.h_type = 2 # MIN sum of manhattan distances from goal posisitions.
        self.heuristics = PuzzleHeuristics(self.goal_state)



    def _solve_given_puzzle(self, start_state):
        # Reset solution path (start state -> goal state).
        self.solution_path = []
        # Add start state to the path.
        self.solution_path.append(start_state)
        current_state = self.solution_path[-1]
        current_state['h_value'] = self.heuristics.calculate_value(self.h_type,current_state)
        # Search for a solution.
        while current_state['tiles'] != self.goal_state['tiles']:
            #print "======CUR STATE======"
            #self._show_state(current_state)
            # Find possible moves against zero tile.
            possible_moves = self._find_possible_moves(current_state)
            # For every move create a new state.
            new_states = self._create_states_from_moves(current_state, possible_moves)
            # Check if the states are valid.
            valid_states = self._get_valid_states(new_states)
            if not valid_states:
                print('No solution found in %d moves.') % len(self.solution_path)
                return False
            # Calculate heuristics value for every new state.
            for state in valid_states:
                state['h_value'] = self.heuristics.calculate_value(self.h_type,state)
            # Choose state with the lowest heuristics value.
            best_state = self._find_best_state(valid_states)
            self.solution_path.append(best_state)
            current_state = best_state
            """
            # Check if the best state has a lower or the same h value than the current state.
            # If yes, another step in solution was found.
            if best_state['h_value'] <= current_state['h_value']:
                self.solution_path.append(best_state)
                current_state = best_state
            # If no, the puzzle has no solution - end the program.
            else:
                print('No solution found in %d moves.') % len(self.solution_path)
                return False
                #print(self.solution_path)
                exit()
            """
        # Goal state was reached
        print('The goal state was reached in %d moves.') % len(self.solution_path)
        #print(self.solution_path)
        return True

    def solve_random_puzzle(self):
        result = self._solve_given_puzzle(self._generate_start_state())
        return result

    def bulk_solve(self, number_of_puzzles):
        # Do simulation
        solved_n = 0
        for i in range(1,number_of_puzzles+1):
            print("ITERATION %d") % i
            if self.solve_random_puzzle():
                solved_n += 1
        # Show statistics
        print('=====BULK RUN STATS=====')
        print('Total puzzles: %d') % number_of_puzzles
        print('Total solved puzzles: %d') % solved_n
        effectivity = (float(solved_n)/number_of_puzzles)*100
        print('Percentual effectivity of the algorithm: '+str(effectivity)+' %')


    def _generate_start_state(self):
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

    def _get_tile_name_by_coordinates(self, state, coordinates):
        for t_name, xy in state['tiles'].iteritems():
            if xy == coordinates:
                return t_name


    def _show_state(self, state):
        print state

    def _find_best_state(self, valid_states):
        """
        Select a state with the lowest h value.
        If there are more states with same value, choose the one which will place a non-zero title on the right place.
        """
        if not valid_states:
            exit(valid_states)
        return min(valid_states, key=lambda x: x['h_value'])

    def _get_valid_states(self, new_states):
        """
        Eliminate all already selected states (in solution path).
        """
        valid_states = []
        for new_state in new_states:
            ok = True
            for sel_state in self.solution_path:
                if sel_state['tiles'] == new_state['tiles']:
                    ok = False
                    break
            if ok:
                valid_states.append(new_state)
        # result
        return valid_states


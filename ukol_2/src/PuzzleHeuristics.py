

class PuzzleHeuristics(object):
    """
    Class for calculating heuristics values.
    """

    def __init__(self, goal_state):
        """
        Constructor - set a goal state (necessary for heuristics to work).
        """
        self.goal_state = goal_state

    def calculate_value(self, h_type, state):
        """
        Public method for calculating h value using selected heuristic.
        """
        if h_type == 1:
            return self._calc_wrong_tiles_c(state)
        else:
            return self._calc_manhattan_d(state)

    def _calc_wrong_tiles_c(self, state):
        """
        Calculate number of wrongly placed tiles in a state.
        """
        count = 0
        for g_tile_name, g_tile_coord in self.goal_state['tiles'].iteritems():
            #print g_tile_name, g_tile_coord, state[g_tile_name]
            if state['tiles'][g_tile_name] != g_tile_coord:
                count += 1
        return count

    def _calc_manhattan_d(self, state):
        """
        Calculate a sum of Manhattan distances for all tiles (between current and goal position).
        """
        h_sum = 0
        for g_tile_name, (g_x, g_y) in self.goal_state['tiles'].iteritems():
            #print g_tile_name, g_tile_coord, state[g_tile_name]
            man_d = abs(g_x - state['tiles'][(g_tile_name)][0]) + abs(g_y - state['tiles'][g_tile_name][1])
            #print("%s: %d | ") % (g_tile_name, man_d),
            h_sum += man_d
        return h_sum









class PuzzleHeuristics(object):

    def __init__(self, goal_state):
        self.goal_state = goal_state

    def calculate_value(self, h_type, state):
        if h_type == 1:
            return self._calc_wrong_tiles_c(state)
        elif h_type == 2:
            return self._calc_manhattan_d(state)

    def _calc_wrong_tiles_c(self, state):
        count = 0
        for g_tile_name, g_tile_coord in self.goal_state['tiles'].iteritems():
            #print g_tile_name, g_tile_coord, state[g_tile_name]
            if state['tiles'][g_tile_name] != g_tile_coord:
                count += 1
        return count

    def _calc_manhattan_d(self, state):
        h_sum = 0
        for g_tile_name, (g_x, g_y) in self.goal_state['tiles'].iteritems():
            #print g_tile_name, g_tile_coord, state[g_tile_name]
            man_d = abs(g_x - state['tiles'][(g_tile_name)][0]) + abs(g_y - state['tiles'][g_tile_name][1])
            #print("%s: %d | ") % (g_tile_name, man_d),
            h_sum += man_d
        return h_sum







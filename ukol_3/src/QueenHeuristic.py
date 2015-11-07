

class QueenHeuristic(object):

    def count_total_conflicts(self, state):
        """
        Count number of conflict in the given state.
        """
        total_c = 0
        for row in state:
            for j in row:
                if j == 1:
                   total_c += self._count_conflicts_for_queen(state, row, j)
        return total_c

    def _count_conflicts_for_queen(self, state, i, j):
        print i,j
        return 0
        conf_c = 0
        # Go up and down
        # Go left and right
        # Go diagonally up-left and down-right

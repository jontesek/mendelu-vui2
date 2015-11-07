

class QueenHeuristic(object):

    def count_total_conflicts(self, state):
        """
        Count number of conflicts in the given state.
        """
        return self._count_conflicts_for_queen(state, (7,7))
        total_c = 0
        for i, row in enumerate(state):
            for j, tile in enumerate(row):
                if tile == 1:
                   total_c += self._count_conflicts_for_queen(state, (i, j))
        return total_c

    def _count_conflicts_for_queen(self, state, queen_pos):
        print queen_pos
        # Go up and down
        vertical_c = self._check_area_vertically(state, queen_pos)
        # Go left and right
        horizontal_c = self._check_area_horizontally(state, queen_pos)
        # Go diagonally
        diagonal_c = self._check_area_diagonally(state, queen_pos)
        print diagonal_c
        exit()
        # result
        total_count = vertical_c + horizontal_c + diagonal_c
        return total_count

    def _check_area_vertically(self, state, queen_pos):
        queens_count = 0
        # Browse through all rows.
        for row in state:
            # Check if the queen's column contains any other queens.
            if row[queen_pos[1]] == 1:
                queens_count += 1
        # result
        return queens_count - 1

    def _check_area_horizontally(self, state, queen_pos):
        queens_count = 0
        # Check if the queen's row contains any other queens.
        queen_row = state[queen_pos[0]]
        for square in queen_row:
            if square == 1:
                queens_count += 1
        # result
        return queens_count - 1

    def _check_area_diagonally(self, state, queen_pos):
        queens_count = 0
        # Check L->R diagonal.
        # Get border position from where to start search.
        coord_dif = queen_pos[0] - queen_pos[1]
        if coord_dif == 0:
            start_pos = (0,0)
        elif coord_dif > 0:
            start_pos = (coord_dif, 0)
        else:
            start_pos = (0, abs(coord_dif))
        # Search the line
        print start_pos
        j = start_pos[1]
        for i, row in enumerate(state[start_pos[0]:8]):
            if j > 7:
                break
            #print i,j,row[j]
            if row[j] == 1:
                queens_count += 1
            j += 1
        # result
        queens_count = 0
        # Check R->L diagonal.

        return queens_count - 1

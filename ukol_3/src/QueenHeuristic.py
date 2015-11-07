

class QueenHeuristic(object):

    def count_total_conflicts(self, state):
        """
        Count number of conflicts in the given state.
        One conflict = two queens in conflict.
        """
        #print self._count_conflicts_for_queen(state,(3,3))
        #exit()
        total_c = 0
        for i, row in enumerate(state):
            for j, square in enumerate(row):
                if square == 1:
                    total_c += self._count_conflicts_for_queen(state,(i, j))
        return total_c/2

    def _count_conflicts_for_queen(self, state, queen_pos):
        # Check if the given position contains a queen.
        if state[queen_pos[0]][queen_pos[1]] == 0:
            return False
        #print queen_pos
        # Go up and down
        vertical_c = self._check_area_vertically(state, queen_pos)
        # Go left and right
        horizontal_c = self._check_area_horizontally(state, queen_pos)
        # Go diagonally L->R
        diagonal_lr = self._check_area_diagonally_lr(state, queen_pos)
        diagonal_rl = self._check_area_diagonally_rl(state, queen_pos)
        # result
        #print vertical_c, horizontal_c, diagonal_lr, diagonal_rl
        total_count = vertical_c + horizontal_c + diagonal_lr + diagonal_rl
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

    def _check_area_diagonally_lr(self, state, queen_pos):
        queens_count = 0
        # Get border position from where to start the search.
        coord_dif = queen_pos[0] - queen_pos[1]
        if coord_dif == 0:
            start_pos = (0,0)
        elif coord_dif > 0:
            start_pos = (coord_dif, 0)
        else:
            start_pos = (0, abs(coord_dif))
        # Search the line
        j = start_pos[1]
        for i, row in enumerate(state[start_pos[0]:8]):
            if j > 7:
                break
            #print i,j,row[j]
            if row[j] == 1:
                queens_count += 1
            j += 1
        # result - minus the original queen
        return queens_count - 1

    def _check_area_diagonally_rl(self, state, queen_pos):
        queens_count = 0
        # up
        j = queen_pos[1]
        for i in range(queen_pos[0],-1,-1):
            if j > 7:
                break
            #print i,j,state[i][j]
            if state[i][j] == 1:
                queens_count += 1
            j += 1
        # bottom
        j = queen_pos[1]
        for i in range(queen_pos[0],8,1):
            if j < 0:
                break
            #print i,j,state[i][j]
            if state[i][j] == 1:
                queens_count += 1
            j -= 1
        # result - minus the original queen
        return queens_count - 2

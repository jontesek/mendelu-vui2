import copy
import random


class QueenHeuristic(object):

    def choose_min_conflict_positions(self, original_state):
        column_state = copy.deepcopy(original_state)
        # For every column
        for j in range(0,8):
            print ('====col. %s====') % j
            # Get current position of the queen in a column.
            queen_i = self._get_queen_pos_in_col(column_state,j)
            # Get current conflict count.
            current_cc = self.count_total_conflicts(column_state)
            # Try to place a queen in every row.
            queen_positions = {}
            for i in range(0,8):
                row_state = copy.deepcopy(column_state)
                # Move the current queen to this place and check conflicts count.
                if row_state[i][j] == 0:
                    row_state[i][j] = 1
                    row_state[queen_i][j] = 0
                    #self._show_board(row_state)
                    queen_positions[i] = self.count_total_conflicts(row_state)
            # Choose position with minimal conflicts count.
            min_cc = min(queen_positions.values())
            min_rows = [row_n for row_n, cc in queen_positions.iteritems() if cc == min_cc]
            new_queen_i = random.choice(min_rows)
            # Check conflict count
            if min_cc > current_cc:
                print('skip')
                continue    # skip the column
            # Edit the current state
            column_state[new_queen_i][j] = 1
            column_state[queen_i][j] = 0
            #self._show_board(column_state)
        # return last state
        return column_state

    def _get_queen_pos_in_col(self, state, col_n):
        for i in range(0,8):
            if state[i][col_n] == 1:
                return i

    def count_total_conflicts(self, state):
        """
        Count number of conflicts in the given state.
        One conflict = two queens in a conflict.
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

    def show_board(self, state):
        print('==============')
        for row in state:
            print row
        print('conflicts count: %d') % self.count_total_conflicts(state)
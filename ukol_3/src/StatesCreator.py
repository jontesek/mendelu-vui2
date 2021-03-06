from random import randint
from QueenHeuristic import QueenHeuristic


class StatesCreator(object):

    def __init__(self):
        self.qh = QueenHeuristic()

    def generate_random_start_state(self):
        # Default state
        state = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
        ]
        # Loop until a conflict is reached.
        conf_found = False
        while not conf_found:
            # Populate columns
            for j in range(0, 8):
                rand_i = randint(0, 7)  # Select random row in the column.
                state[rand_i][j] = 1    # Place queen there.
            # Check if there are any conflicts.
            conf_c = self.qh.count_total_conflicts(state)
            if conf_c > 0:
                return state

    def get_sample_start_state(self, num):
        # lecture example 1
        if num == 0:
            state = [
                [0,0,0,0,1,0,0,0],
                [1,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,0,0],
                [0,0,0,1,0,0,0,0],
                [0,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1],
            ]
            conflicts_n = 1
        # lecture example 2
        elif num == 1:
            state = [
                [1,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,1,0,0,0],
                [0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,1],
            ]
            conflicts_n = 28
        # https://thewalnut.io/app/release/14/#time=9
        elif num == 2:
            state = [
                [0,0,0,0,0,1,0,0],
                [0,0,0,1,0,0,0,0],
                [0,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,0],
                [0,0,1,0,1,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0],
            ]
            conflicts_n = 1
        # http://www.aiai.ed.ac.uk/~gwickler/eightqueens.html
        elif num == 3:
            state = [
                [1,0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0],
                [0,1,0,0,0,0,0,0],
                [0,0,0,0,0,1,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,1,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,1],
            ]
            conflicts_n = 1
        elif num == 4:
            state = [
                [1,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,0,0],
                [0,0,0,0,0,0,0,1],
            ]
            conflicts_n = 1

        return (state, conflicts_n)

    def get_sample_final_state(self, number):
        conflicts_n = 0
        if number == 1:
            state = [
                [1,0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,0,1,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,1,0],
                [0,1,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0],
            ]
        elif number == 2:
            state = [
                [0,0,0,0,1,0,0,0],
                [0,1,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,1,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,0,1,0,0],
                [1,0,0,0,0,0,0,0],
            ]
        elif number == 3:
            state = [
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,1,0],
                [0,0,0,0,1,0,0,0],
                [0,0,1,0,0,1,0,0],
                [1,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1],
                [0,1,0,1,0,0,0,0],
            ]

        return (state, conflicts_n)


    def get_sample_inter_state(self, number):
        if number == 1:
            state = [
                [0,0,0,0,1,0,0,0],
                [0,1,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,1],
                [0,0,0,0,0,0,1,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,0,1,0,0],
                [1,0,0,0,0,0,0,0],
            ]
            conflicts_n = 3
        elif number == 2:
            state = [
                [1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1]
            ]
            conflicts_n = 3

        return (state, conflicts_n)

"""
state = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]
"""
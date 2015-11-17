#from ..src.QueenHeuristic import QueenHeuristic
#from ..src.StatesCreator import StatesCreator


class QueenHeuristicTest(object):

    def __init__(self, qh, sc):
        self.q_heuristic = qh
        self.s_creator = sc

    def test_lecture_state(self):
        state = self.s_creator.get_lecture_state()
        res_exp = 1
        res_real = self.q_heuristic.count_total_conflicts(state)
        return res_exp == res_real

    def test_sample_state(self, number):
        data = self.s_creator.get_sample_start_state(number)
        res_exp = data[1]
        res_real = self.q_heuristic.count_total_conflicts(data[0])
        return res_real == res_exp

    def test_final_state(self, number):
        data = self.s_creator.get_sample_final_state(number)
        res_exp = data[1]
        res_real = self.q_heuristic.count_total_conflicts(data[0])
        return res_real == res_exp

    def test_inter_state(self, number):
        data = self.s_creator.get_sample_inter_state(number)
        res_exp = data[1]
        res_real = self.q_heuristic.count_total_conflicts(data[0])
        return res_real == res_exp







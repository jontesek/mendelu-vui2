from tests.QueenHeuristicTest import QueenHeuristicTest
from src.QueenHeuristic import QueenHeuristic
from src.StatesCreator import StatesCreator

qh = QueenHeuristic()
sc = StatesCreator()

qht = QueenHeuristicTest(qh, sc)

print qht.test_sample_state(0)
#print qht.test_final_state(2)
#print qht.test_inter_state(2)

#print sc.generate_random_start_state()
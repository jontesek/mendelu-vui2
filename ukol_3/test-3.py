import os

from src.ChessQueenWorld import ChessQueenWorld

file_paths = {
    'input_dir': os.path.abspath('input'),
    'output_dir': os.path.abspath('output')
}
cqw = ChessQueenWorld()

#cqw.solve_sample_board(4)
#cqw.solve_random_board()
cqw.bulk_solve(10)
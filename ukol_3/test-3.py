import os

from src.ChessQueenWorld import ChessQueenWorld

file_paths = {
    'input_dir': os.path.abspath('input'),
    'output_dir': os.path.abspath('output')
}
cqw = ChessQueenWorld(file_paths)

cqw.solve_random_board()

#my = [15,27,37,48]
#print my[0:3]
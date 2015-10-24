import sys
from src.MissionaryWorld import MissionaryWorld

# read command line arguments
args = sys.argv     # {2,3,4} AND {'BFS,'DFS'}
# If there are no arguments, set default values.
if len(args) == 1:
    can_number = 3
    search_type = 'BFS'
else:
    can_number = long(args[1])
    search_type = args[2]

# Create the main object
world = MissionaryWorld(can_number)
# Find the solution
world.generate_tree(search_type)

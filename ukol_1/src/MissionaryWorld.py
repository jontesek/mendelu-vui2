import Queue


class MissionaryWorld(object):
    """The main class for the solution of "Missionaries and cannibals" problem."""

    def __init__(self, number_of_cannibals):
        """Object constructor

        Keyword arguments:
        number of cannibals --integer: same as number of missionaries (2,3,4)
        """
        # Graph representation of the state space: nodes = states, edges = operators
        self.state_tree = {'nodes': {}}
        # Transportation of people by the boat (1 or 2 persons possible)
        self.operators = [(1,0),(2,0),(0,1),(0,2),(1,1)] # (number of missionaries, number of cannibals)
        # State representation: left bank, right bank: (number of missionaries, number of cannibals, number of boats)
        if number_of_cannibals == 3:
            self.start_state = ((3,3,1),(0,0,0))
            self.target_state = ((0,0,0),(3,3,1))
        elif number_of_cannibals == 2:
            self.start_state = ((2,2,1),(0,0,0))
            self.target_state = ((0,0,0),(2,2,1))
        elif number_of_cannibals == 4:
            self.start_state = ((4,4,1),(0,0,0))
            self.target_state = ((0,0,0),(4,4,1))
        # Max level depth for DFS
        self.dfs_max_depth = 100

    def generate_tree(self, search_type):
        """Create a tree using the selected method and find the first solution.
        BFS finds the optimal solution, while DFS might or might not.

        Keyword arguments:
        search_type --string: BFS or DFS
        """
        # Create a data structure for nodes list
        if search_type == 'BFS':
            nodes_list_structure = Queue.Queue()     # FIFO
        else:
            nodes_list_structure = Queue.LifoQueue() # LIFO
        # Create and insert root node
        root_node = {'left': self.start_state[0], 'right': self.start_state[1], 'parent_id': None, 'id': 0, 'level': 0, 'used_op': None}
        self.state_tree['nodes'][0] = root_node
        nodes_list_structure.put(root_node)
        # Build a tree
        node_id = 1
        while not nodes_list_structure.empty():
            # Get node from the structure
            examined_node = nodes_list_structure.get()
            #print('==========examined node %d===========') % examined_node['id']
            #print(examined_node)
            # Generate new possible states from the node.
            new_children = self._generate_tree_level(examined_node)
            # Add new nodes to the graph.
            for child_node in new_children:
                # Assign a new node ID and level number
                child_node['id'] = node_id
                child_node['level'] = examined_node['level'] + 1
                #print('++++child added:'+str(child_node))
                # Add child to the graph
                self.state_tree['nodes'][node_id] = child_node
                # increment node ID
                node_id = node_id + 1
                # Check if it is a target node.
                if child_node['left'] == self.target_state[0] and child_node['right'] == self.target_state[1]:
                    #print('->OK: found solution: '+str(child_node))
                    self._show_solution(child_node)
                    return # Target state reached - end the script.
            # For DFS - check if the level is not too deep.
            if search_type == 'DFS' and new_children and new_children[0]['level'] > self.dfs_max_depth:
                continue # do not add more children
            # Add new nodes to the structure.
            for child_node in new_children:
                nodes_list_structure.put(child_node)

    def _generate_tree_level(self, current_state):
        """Generate new nodes (children) for all possibilities."""
        new_nodes = []
        for op in self.operators:
            new_state = self._check_new_state(current_state, op)
            #print('operator: ' + str(op) + str(new_state))
            if new_state:
                new_nodes.append(new_state)
        return new_nodes

    def _check_new_state(self, current_state, op):
        """Check the state and operator, if it does not violate given conditions."""
        # Choose a departure bank
        if current_state['left'][2] == 1:
            departure_bank = current_state['left']
            arrival_bank = current_state['right']
        else:
            departure_bank = current_state['right']
            arrival_bank = current_state['left']
        # Check there are enough people on the departure bank for transport according to operator.
        if op[0] > departure_bank[0] or op[1] > departure_bank[1]:
            return False
        # Check that after the transport, there are no more cannibals than missionaries on the both banks.
        if (departure_bank[0] - op[0]) > 0:
            dep_ok = (departure_bank[0] - op[0]) >= (departure_bank[1] - op[1])
        else:
            dep_ok = True
        if (arrival_bank[0] + op[0]) > 0:
            arr_ok = (arrival_bank[0] + op[0]) >= (arrival_bank[1] + op[1])
        else:
            arr_ok = True
        if (not dep_ok or not arr_ok):
            return False    # do nothing
        else:
            # Recount banks states
            departure_state = (departure_bank[0] - op[0], departure_bank[1] - op[1], 0)
            arrival_state = (arrival_bank[0] + op[0], arrival_bank[1] + op[1], 1)
            # Choose which is left and which is right state.
            if current_state['left'][2] == 1:
                left_state = departure_state
                right_state = arrival_state
            else:
                left_state = arrival_state
                right_state = departure_state
            # Create a new total state
            new_state = {'left': left_state, 'right': right_state, 'parent_id': current_state['id'], 'used_op': op}
            # Check that the new state is not the same as the previous state of the current state.
            if current_state['parent_id'] is not None:
                previous_state = self.state_tree['nodes'][current_state['parent_id']]
                if new_state['left'] == previous_state['left'] and new_state['right'] == previous_state['right']:
                    return False    # do nothing
            # Check that the new state is not the same as the root state.
            if new_state['left'] == self.state_tree['nodes'][0]['left'] and new_state['right'] == self.state_tree['nodes'][0]['right']:
                return False
            # return result
            return new_state

    def _show_solution(self, target_node):
        # Find the path created by sequence of nodes from the target node to the root node.
        nodes_path = []
        examined_node = target_node
        while examined_node['parent_id'] is not None:
            nodes_path.append(examined_node)
            examined_node = self.state_tree['nodes'][examined_node['parent_id']]
        # Add root node
        nodes_path.append(self.state_tree['nodes'][0])
        # Show the path.
        nodes_path.reverse()
        print("=========Solution=========")
        for state in nodes_path:
            print('%d. (%d): %s, %s <- %s') % (state['level'], state['id'], state['left'], state['right'], state['used_op'])
        # Show the number of steps.
        print
        print('The lowest number of steps for the problem solution: %d') % (len(nodes_path) - 1)

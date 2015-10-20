import Queue


class MissionaryWorld(object):
    """The main class for the solution of "Missionaries and cannibals" problem."""

    def __init__(self):
        """Constructor"""
        # later choose 2+2, 3+3, 4+4
        # Graph representation of the state space: nodes = states, edges = operators
        self.state_tree = {'root': None, 'nodes': {}, 'edges': {}}
        # Transportation of people by the boat (1 or 2 persons possible)
        self.operators = [(1,0),(2,0),(0,1),(0,2),(1,1)] # (number of missionaries, number of cannibals)
        # State representation: left bank, right bank: (number of missionaries, number of cannibals, number of boats)
        self.start_state = ((3,3,1),(0,0,0))
        self.target_state = ((0,0,0),(3,3,1))
        self.max_depth = 100
        self.solutions_ids = []

    def generate_bfs_tree(self):
        """Create a tree for BFS"""
        bfs_queue = Queue.Queue()
        # Create and insert root node
        root_node = {'left': self.start_state[0], 'right': self.start_state[1], 'parent_id': None, 'visited': None, 'id': 1, 'level': 1}
        self.state_tree['root'] = root_node
        self.state_tree['nodes'][1] = root_node
        bfs_queue.put(root_node)
        # Build a tree
        node_id = 2
        step_id = 1
        while not bfs_queue.empty():
            queue_cont = False
            # Get node from the queue
            examined_node = bfs_queue.get()
            print('==========examined node %d===========') % examined_node['id']
            print(examined_node)
            # Generate new possible states from the node.
            new_children = self.generate_tree_level(examined_node)
            # Add new nodes to the graph.
            for child_node in new_children:
                # Assign a new node ID and level number
                child_node['id'] = node_id
                child_node['level'] = examined_node['level'] + 1
                print('++++child added:'+str(child_node))
                # Add child to the graph
                self.state_tree['nodes'][node_id] = child_node
                self.state_tree['edges'][(examined_node['id'], child_node['id'])] = True
                # increment node number
                node_id = node_id + 1
                # Check if it is a target node.
                if child_node['left'] == self.target_state[0] and child_node['right'] == self.target_state[1]:
                    print('->OK: found solution: '+str(child_node))
                    queue_cont = True
                    self.solutions_ids.append(child_node['id'])
                    break
            # Target state reached.
            if queue_cont:
                continue
            # Check if the level is not too deep.
            if new_children and new_children[0]['level'] > self.max_depth:
                continue # do not add more children
            # Add new nodes to the queue.
            for child_node in new_children:
                bfs_queue.put(child_node)
            # increment step number
            step_id = step_id + 1
            if step_id > 100:
                    pass #exit()
        # print solutions count
        print('====solutions====')
        print len(self.solutions_ids)


    def get_shortest_solution(self):
        min_level = 999999999999999
        min_node = None
        for node_id in self.solutions_ids:
            node = self.state_tree['nodes'][node_id]
            if node['level'] < min_level:
                min_node = node
                min_level = node['level']
        print min_node


    def generate_tree_level(self, current_state):
        """Generate new nodes (children) for all possibilities."""
        new_nodes = []
        for op in self.operators:
            new_state = self.check_new_state(current_state, op)
            print('operator: ' + str(op) + str(new_state))
            if new_state:
                new_nodes.append(new_state)
        return new_nodes

    def check_new_state(self, current_state, op):
        """Check the state and operator, if it does not violate given conditions."""
        # 1. Choose a departure bank
        if current_state['left'][2] == 1:
            departure_bank = current_state['left']
            arrival_bank = current_state['right']
        else:
            departure_bank = current_state['right']
            arrival_bank = current_state['left']
        # Check there are enough people on the departure bank for transport according to operator.
        if op[0] > departure_bank[0] or op[1] > departure_bank[1]:
            return False
        # 2. Check that after the transport, there are no more cannibals than missionaries on the both banks.
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
            #if current_state['parent_id']:
                #print self.state_tree['nodes'][current_state['parent_id']]['right']
            new_state = {'left': left_state, 'right': right_state, 'visited': None, 'parent_id': current_state['id']}
            # 3. Check that the new state is not the same as the previous state of the current state.
            if current_state['parent_id']:
                previous_state = self.state_tree['nodes'][current_state['parent_id']]
                print('new state: '+str(new_state))
                print('prev state: '+str(previous_state))
                if new_state['left'] == previous_state['left'] and new_state['right'] == previous_state['right']:
                    return False    # do nothing
            # return result
            return new_state


    def get_node(self, node_id):
        pass #return self.state_tree['nodes'][node['id']]


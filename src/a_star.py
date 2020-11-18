import time
from node import Node
from puzzle import Puzzle
from search_algorithm import SearchAlgorithm

class AStar(SearchAlgorithm):
    def __init__(self, puzzle, heuristic, algorithm_name="astar"):
        super().__init__(puzzle, heuristic=heuristic, algorithm_name="astar") 

    def search(self):
        print(f"Searching using {self.get_algorithm_name()} with heuristic {self.heuristic}")
        start = time.time()

        # Start node
        self.initial_node = Node(puzzle=self.puzzle, parent=None, arriving_move=None,
                                 move_cost=0, moved_tile=0, cost_to_reach=0, heuristic_function=self.heuristic)

        # Add start node to open list
        self.open_nodes.append(self.initial_node)

        while(self.open_nodes[0].is_goal() == False and time.time() < start + self.timeout):
            # Pop node
            self.pop_node()

        if self.open_nodes[0].is_goal():
            print(f"Found solution {self.open_nodes[0]}")
            self.generate_solution_path()
            self.solution_found = True

        else:
            print(f"No solution")

        self.exec_time = time.time() - start
        self.total_cost = self.open_nodes[0].cost_to_reach
        self.search_path = self.closed_nodes
        print(f"Execution time {self.exec_time}")

        self.generate_output_files()

    # Override
    def generate_solution_path(self):
        current_node = self.open_nodes[0]
        self.solution_path.append(current_node)
        while (current_node is not None):
            if current_node.parent is None:
                break
            parent_node = current_node.parent
            self.solution_path.append(parent_node)
            current_node = parent_node


    # Override
    def sort(self):
        self.open_nodes = sorted(self.open_nodes, key=lambda n: n.f_n)

    # Override
    def pop_node(self):
        n = self.open_nodes[0]
        # Get children of the node
        n.expand()
        # Pop first node from open list
        self.open_nodes.pop(0)
        # Append popped node to closed list
        self.closed_nodes.append(n)
        # Add child nodes of the popped node to open list and sort
        for child_node in n.child_nodes:

            # If s is already in closed
            if self.replace_if_lower(child_node, self.closed_nodes, remove_node=True):
                continue
            elif self.replace_if_lower(child_node, self.open_nodes, remove_node=False):
                continue
            else:                          
                self.open_nodes.append(child_node)

        self.sort()


    def replace_if_lower(self, child_node, node_list, remove_node):
        for i, node in enumerate(node_list, start=0):
            if child_node.puzzle.current_setup == node.puzzle.current_setup:
                if child_node.f_n < node.f_n:
                    self.open_nodes[i] = child_node
                    if remove_node:
                       del self.closed_nodes[i]
                    return True
        return False                    
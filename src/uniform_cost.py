from node import Node
from puzzle import Puzzle
from search_algorithm import SearchAlgorithm
import time

class UniformCost(SearchAlgorithm):
    def __init__(self, puzzle, algorithm_name="ucs", heuristic=None):
        super().__init__(puzzle, algorithm_name="ucs", heuristic=None) 

    # Override 
    def search(self):
        print(f"Searching using {self.get_algorithm_name()} algorithm...")
        start = time.time()

        # Start node
        self.initial_node = Node(puzzle=self.puzzle,parent=None, arriving_move=None, move_cost=0,moved_tile=0, cost_to_reach=0 )

        # Add start node to open list
        self.open_nodes.append(self.initial_node)

        while(self.open_nodes[0].is_goal() == False and time.time() < start + self.timeout ):
            # Pop node
            self.pop_node()

        if self.open_nodes[0].is_goal():
            print (f"Found solution {self.open_nodes[0]}")
            self.generate_solution_path()
           
        else:
            print (f"No solution")

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




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
        n = Node(puzzle=self.puzzle,parent=None, arriving_move=None, move_cost=0,moved_tile=0, cost_to_reach=0 )

        # Add start node to open list
        self.open_nodes.append(n)

        while(self.open_nodes[0].is_goal() == False and time.time() < start + self.timeout ):
            # Pop node
            self.pop_node()

        if self.open_nodes[0].is_goal():
            print (f"Found solution {self.open_nodes[0]}")
        else:
            print (f"No solutuion")

        self.exec_time = time.time() - start
        print(f"Execution time {self.exec_time}")





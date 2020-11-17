from node import Node
from puzzle import Puzzle
from search_algorithm import SearchAlgorithm


class UniformCost(SearchAlgorithm):
    def __init__(self, puzzle, algorithm_name="ucs", heuristic=None):
        super().__init__(puzzle, algorithm_name="ucs", heuristic=None) 

    # Override 
    def search(self):
        print(f"Running {self.get_algorithm_name()} algorithm")
        # Start node
        n = Node(puzzle=self.puzzle,parent=None, arriving_move=None, move_cost=0,moved_tile=0, cost_to_reach=0 )

        # Add start node to open list
        self.open_nodes.append(n)

        i = 0
        while(self.open_nodes[0].is_goal() == False):
            # Pop node
            self.pop_node()
            print(self.open_nodes[0])
            i += 1
        print (f"Found solution {self.open_nodes[0]}")




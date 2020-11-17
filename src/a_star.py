from node import Node
from puzzle import Puzzle
from search_algorithm import SearchAlgorithm

class AStar(SearchAlgorithm):
    def __init__(self, puzzle, algorithm_name="astar", heuristic=None):
        super().__init__(puzzle, algorithm_name="astar", heuristic=None) 

    # Override 
    def search(self):
        print(f"Running {self.get_algorithm_name()} algorithm")
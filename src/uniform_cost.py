from node import Node
from puzzle import Puzzle
from search_algorithm import SearchAlgorithm

class UniformCost(SearchAlgorithm):
    def __init__(self, puzzle, algorithm_name="ucs", heuristic=None):
        super().__init__(puzzle, algorithm_name="ucs", heuristic=None) 

    # Override 
    def search(self):
        print(f"Running {self.get_algorithm_name()} algorithm")
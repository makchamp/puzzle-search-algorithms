from node import Node
from puzzle import Puzzle
from search_algorithm import SearchAlgorithm

class AStar(SearchAlgorithm):
    def __init__(self, puzzle, heuristic, algorithm_name="astar"):
        super().__init__(puzzle, heuristic=heuristic, algorithm_name="astar") 

    # Override 
    def search(self):
        print(f"Searching using {self.get_algorithm_name()} algorithm with heuristic {self.heuristic}")
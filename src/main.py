import sys
from puzzle import Puzzle

from uniform_cost import UniformCost
from greedy_best_first import GreedyBestFirst
from a_star import AStar

def load_puzzles(puzzles_file=None):
    """
    Loads puzzles from disc
    """
    if puzzles_file == None:  # Retrieve puzzles from default file
        puzzles_file = "puzzles.txt"

    with open(puzzles_file) as pf:
        lines = [line.rsplit() for line in pf]  # Each line represents a puzzle

    puzzles = []
    num_of_rows = 2
    for i, line in enumerate(lines, start=1):
        # Convert entries from 'str' to 'int'
        puzzles.append(Puzzle(rows=num_of_rows, setup=[int(i) for i in line], puzzle_number=i))

    print(f"Loaded {len(puzzles)} puzzles from disc:")
    for puzzle in puzzles:
        print(f"Puzzle {puzzle.get_puzzle_num()}: [{puzzle}]")
    return puzzles


if __name__ == "__main__":
    puzzles = []  # The input puzzles  
    try:
        if len(sys.argv) == 1:  # No argument passed, get puzzles from default puzzles file
            puzzles = load_puzzles()
        else:
            puzzles = load_puzzles(sys.argv[1])
    except Exception as e:
        print(e)
        print("Error trying to load puzzles from disc")
        sys.exit()        

    # Run each search algorithm on each puzzle
    for puzzle in puzzles:
        print(f"\nPuzzle {puzzle.get_puzzle_num()}:")



        ucs = UniformCost(puzzle)
        ucs.search()

        gbfs_h1 = GreedyBestFirst(puzzle, heuristic="h1")
        gbfs_h1.search()

        gbfs_h2 = GreedyBestFirst(puzzle, heuristic="h2")
        gbfs_h2.search()

        astar_h1 = AStar(puzzle, heuristic="h1")
        astar_h1.search()

        astar_h2 = AStar(puzzle, heuristic="h2")
        astar_h2.search()




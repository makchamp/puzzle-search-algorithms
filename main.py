import sys
from puzzle import Puzzle


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
    for line in lines:
        # Convert entries from 'str' to 'int'
        puzzles.append(Puzzle(rows=num_of_rows, setup=[int(i) for i in line]))

    print(f"Loaded {len(puzzles)} puzzles from disc:")
    for i, puzzle in enumerate(puzzles, start=1):
        print(f"Puzzle {i}: [{puzzle}]")
    return puzzles


if __name__ == "__main__":

    try:
        if len(sys.argv) == 1:  # No argument passed, get puzzles from default puzzles file
            load_puzzles()
        else:
            load_puzzles(sys.argv[1])
    except:
        sys.exit()

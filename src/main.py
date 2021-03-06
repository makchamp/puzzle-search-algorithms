import csv
import sys
from puzzle import Puzzle

from uniform_cost import UniformCost
from greedy_best_first import GreedyBestFirst
from a_star import AStar
import json

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

    results = {
      "ucs": {
        "solution_path_list": [],
        "search_path_list": [],
        "no_solution_count": 0,
        "cost_list": [],
        "exec_time_list": []
      },
      "gbfs_h1": {
        "solution_path_list": [],
        "search_path_list": [],
        "no_solution_count": 0,
        "cost_list": [],
        "exec_time_list": []
      },
      "gbfs_h2": {
        "solution_path_list": [],
        "search_path_list": [],
        "no_solution_count": 0,
        "cost_list": [],
        "exec_time_list": []
      },
      "astar_h1": {
        "solution_path_list": [],
        "search_path_list": [],
        "no_solution_count": 0,
        "cost_list": [],
        "exec_time_list": []
      },
      "astar_h2": {
        "solution_path_list": [],
        "search_path_list": [],
        "no_solution_count": 0,
        "cost_list": [],
        "exec_time_list": []
      }
    }

    # Run each search algorithm on each puzzle
    for puzzle in puzzles:
        print(f"\nPuzzle {puzzle.get_puzzle_num()}:")

        # Create and store the results of Uniform Cost Search
        ucs = UniformCost(puzzle)
        ucs.search()
        if ucs.solution_found:
            results['ucs']['solution_path_list'].append(len(ucs.solution_path))
            results['ucs']['cost_list'].append(ucs.total_cost)
            results['ucs']['exec_time_list'].append(ucs.exec_time)
        else:
            results['ucs']['no_solution_count'] += 1
        results['ucs']['search_path_list'].append(len(ucs.search_path))


        # Create and store the results of Greedy Best First with H1
        gbfs_h1 = GreedyBestFirst(puzzle, heuristic="h1")
        gbfs_h1.search()

        if gbfs_h1.solution_found:
            results['gbfs_h1']['solution_path_list'].append(len(gbfs_h1.solution_path))
            results['gbfs_h1']['cost_list'].append(gbfs_h1.total_cost)
            results['gbfs_h1']['exec_time_list'].append(gbfs_h1.exec_time)
        else:
            results['gbfs_h1']['no_solution_count'] += 1
        results['gbfs_h1']['search_path_list'].append(len(gbfs_h1.search_path))


        # Create and store the results of Greedy Best First with H2
        gbfs_h2 = GreedyBestFirst(puzzle, heuristic="h2")
        gbfs_h2.search()

        if gbfs_h2.solution_found:
            results['gbfs_h2']['solution_path_list'].append(len(gbfs_h2.solution_path))
            results['gbfs_h2']['cost_list'].append(gbfs_h2.total_cost)
            results['gbfs_h2']['exec_time_list'].append(gbfs_h2.exec_time)
        else:
            results['gbfs_h2']['no_solution_count'] += 1
        results['gbfs_h2']['search_path_list'].append(len(gbfs_h2.search_path))


        # Create and store the results of A* with H1
        astar_h1 = AStar(puzzle, heuristic="h1")
        astar_h1.search()

        if astar_h1.solution_found:
            results['astar_h1']['solution_path_list'].append(len(astar_h1.solution_path))
            results['astar_h1']['cost_list'].append(astar_h1.total_cost)
            results['astar_h1']['exec_time_list'].append(astar_h1.exec_time)
        else:
            results['astar_h1']['no_solution_count'] += 1
        results['astar_h1']['search_path_list'].append(len(astar_h1.search_path))


        # Create and store the results of A* with H2
        astar_h2 = AStar(puzzle, heuristic="h2")
        astar_h2.search()

        if astar_h2.solution_found:
            results['astar_h2']['solution_path_list'].append(len(astar_h2.solution_path))
            results['astar_h2']['cost_list'].append(astar_h2.total_cost)
            results['astar_h2']['exec_time_list'].append(astar_h2.exec_time)
        else:
            results['astar_h2']['no_solution_count'] += 1
        results['astar_h2']['search_path_list'].append(len(astar_h2.search_path))


    # store the results to csv file
    with open('results.csv', 'w') as results_csv:
        writer = csv.writer(results_csv)
        for method, method_dict in results.items():
            for key, value in method_dict.items():
                writer.writerow([method, key, value])

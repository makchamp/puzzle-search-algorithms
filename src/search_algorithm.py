from node import Node
from puzzle import Puzzle

class SearchAlgorithm:

    def __init__(self, puzzle, algorithm_name=None, heuristic=None):

        self.puzzle = puzzle
        self.puzzle_number = puzzle.get_puzzle_num()
        self.initial_node = Node(puzzle, None, None, None, None, None)
        self.open_nodes = [self.initial_node]
        self.closed_nodes = []
        self.search_path = []
        self.solution_path = []
        self.algorithm_name = algorithm_name
        self.heuristic = heuristic

        # total cost of the solution path
        self.total_cost = 0

        # execution time for the search algorithm
        self.exec_time = 0

    def search(self):
        # Add the code for the search algorithm here
        # you should calculate the execution time and the total cost of the solution path
        # you also should store the search and solution paths
        pass

    def generate_solution_path(self):
        # after finding the goal state, traverse the search tree to find the solution path
        pass

    def generate_output_files(self):
        # generate output files
        self.generate_solution_path_output_file()
        self.generate_search_path_output_file()


    def generate_search_path_output_file(self):
        # generate search path file
        file_name = self.puzzle_number + '_'
        file_name += '' if self.heuristic is None else '-' + self.heuristic

        search_path_file_name = file_name + '_search'

        search_path_file_content = ''

        for node in self.search_path:
            search_path_file_content += f'{node.f_n} {node.g_n} {node.h_n} {node.puzzle}\n'

        # write search_path file content into the search
        search_path_file = open(search_path_file_name, "w")
        search_path_file.write(search_path_file_content)
        search_path_file.close()

    def generate_solution_path_output_file(self):
        # generate search path file
        file_name = self.puzzle_number + '_'
        file_name += '' if self.heuristic is None else '-' + self.heuristic

        solution_path_file_name = file_name + '_solution.txt'

        solution_path_file_content = ''

        for index, node in enumerate(self.search_path,  start=0):
            if index == 0:
                solution_path_file_content += f'0 0 {node.puzzle}\n'
            else:
                solution_path_file_content += f'{node.moved_tile} {node.move_cost} {node.puzzle}\n'

        solution_path_file_content += f'{self.total_cost} {self.exec_time}'

        # write search_path file content into the search
        solution_path_file = open(solution_path_file_name, "w")
        solution_path_file.write(solution_path_file_name)
        solution_path_file.close()

    def get_algorithm_name(self):
        return self.algorithm_name
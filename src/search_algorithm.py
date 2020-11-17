from node import Node
from puzzle import Puzzle

class SearchAlgorithm:

    def __init__(self, puzzle, algorithm_name=None, heuristic=None):

        self.puzzle = puzzle
        self.puzzle_number = puzzle.get_puzzle_num()
        self.initial_node = None
        self.open_nodes = []
        self.closed_nodes = []
        self.search_path = []
        self.solution_path = []
        self.algorithm_name = algorithm_name
        self.heuristic = heuristic

        # total cost of the solution path
        self.total_cost = 0

        # execution time for the search algorithm
        self.exec_time = 0

        # Time to stop execution(with no solution found)
        self.timeout = 60 # 60 seconds

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
        output_dir = "solution_files/"
        # generate search path file
        file_name = str(self.puzzle_number) + '_' + self.algorithm_name + '_'
        file_name += '' if self.heuristic is None else '-' + str(self.heuristic) + '_'

        search_path_file_name = file_name + 'search'

        search_path_file_content = ''

        for node in self.search_path:
            search_path_file_content += f'{node.f_n} {node.g_n} {node.h_n} {node.puzzle}\n'

        # write search_path file content into the search
        search_path_file = open(output_dir + search_path_file_name, "w")
        search_path_file.write(search_path_file_content)
        search_path_file.close()

    def generate_solution_path_output_file(self):
        output_dir = "solution_files/"
        # generate search path file
        file_name = str(self.puzzle_number) + '_' + self.algorithm_name + '_'
        file_name += '' if self.heuristic is None else '-' + str(self.heuristic) + '_'

        solution_path_file_name = file_name + 'solution.txt'

        solution_path_file_content = ''

        for node in self.solution_path:
            solution_path_file_content += f'{node.moved_tile} {node.move_cost} {node.puzzle}\n'

        solution_path_file_content += f'{self.total_cost} {self.exec_time}\n'

        # write search_path file content into the search
        solution_path_file = open(output_dir + solution_path_file_name, "w")
        solution_path_file.write(solution_path_file_content)
        solution_path_file.close()


    def sort(self):
        # Sorts by cost by default, override to sort by heuristic
        self.open_nodes = sorted(self.open_nodes, key=lambda n: n.move_cost)


    def pop_node(self):
        n = self.open_nodes[0]
        # Get children of the node
        n.expand()
        # Pop first node from open list
        self.open_nodes.pop(0)
        # Append popped node to closed list
        self.closed_nodes.append(n)
        # Add child nodes of the popped node to open list and sort
        for child_node in n.child_nodes:
            # Check if node has already been visited
            if child_node.puzzle.current_setup not in self.closed_puzzles():
                self.open_nodes.append(child_node)

            # Replace node if cost is lower
                for i, node in enumerate(self.open_nodes, start=0):
                    if child_node.puzzle.current_setup == node.puzzle.current_setup and child_node.cost_to_reach < node.cost_to_reach:
                        self.open_nodes[i] = child_node
        self.sort()


    def closed_puzzles(self):
        puzzles = []
        for node in self.closed_nodes:
            puzzles.append(node.puzzle.current_setup)
        return puzzles


    def get_algorithm_name(self):
        return self.algorithm_name
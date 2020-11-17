from puzzle import Puzzle


class Node:
    # this is a node in the tree on which we will apply a search algorithm

    # this will be a static variable to store all the previously visited setups
    # visited_setups = []

    def __init__(self, puzzle: Puzzle, parent, arriving_move, move_cost, moved_tile, heuristic_function=None):

        self.puzzle = puzzle
        self.parent = parent
        self.arriving_move = arriving_move
        self.move_cost = move_cost
        self.moved_tile = moved_tile

        # record the depth of the node
        self.depth = 0
        if parent is not None:
            self.depth = 1 + self.parent.depth

        # the total cost needed to reach this node
        self.total_cost = 0
        if parent is not None:
            self.total_cost = move_cost + self.parent.total_cost

        self.child_nodes = []

        self.heuristic_function = heuristic_function

        # h(n) or the heuristic value of the node
        self.h_n = self.puzzle.get_heuristic(heuristic_function)
        
        # the cost of the immediate step that made us arrive at this node

        # self.g_n = move_cost
        # self.f_n = self.h_n + self.g_n

    def expand(self):
        # This method will expand the current node by applying all the possible moves to the puzzle and it
        # will create child nodes using the new setups

        successor_puzzle_tuples = self.puzzle.get_successors()

        for puzzle_tuple in successor_puzzle_tuples:
            puzzle = puzzle_tuple[0]

            # check if puzzle has been visited before
            # TODO: check for the visited setups (or nodes) in the algorithm
            # if puzzle.current_setup in self.visited_setups:
            #     continue

            arriving_move = puzzle_tuple[1]
            move_cost = puzzle_tuple[2]
            moved_tile = puzzle_tuple[3]
            child_node = Node(puzzle, self, arriving_move, move_cost, moved_tile, self.heuristic_function)
            self.child_nodes.append(child_node)

        return self.child_nodes

    def __eq__(self, other):
        # check if two nodes are equal

        if self.puzzle.current_setup == self.puzzle.current_setup \
                and self.puzzle.rows == self.puzzle.rows:
            return True

        return False

    def is_goal(self):
        # return true if the puzzle is goal else false
        return self.puzzle.is_goal()

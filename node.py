from puzzle import Puzzle


class Node:
    # this is a node in the tree on which we will apply a search algorithm

    # this will be a static variable to store all the previously visited setups
    visited_setups = []

    def __init__(self, puzzle: Puzzle, parent, arriving_move, move_cost):

        self.puzzle = puzzle
        self.parent = parent
        self.arriving_move = arriving_move
        self.move_cost = move_cost  # the cost of the immediate step that made us arrive at this node

        # record the depth of the node
        self.depth = 0
        if parent is not None:
            self.depth = 1 + self.parent.depth

        # the total cost needed to reach this node
        self.total_cost = 0
        if parent is not None:
            self.total_cost = move_cost + self.parent.total_cost

        self.child_nodes = []

    def expand(self):
        # This method will expand the current node by applying all the possible moves to the puzzle and it
        # will create child nodes using the new setups

        successor_puzzle_tuples = self.puzzle.get_successors()

        for puzzle_tuple in successor_puzzle_tuples:
            puzzle = puzzle_tuple[0]

            # check if puzzle has been visited before
            if puzzle.current_setup in self.visited_setups:
                continue

            arriving_move = puzzle_tuple[1]
            move_cost = puzzle_tuple[2]
            child_node = Node(puzzle, self, arriving_move, move_cost)
            self.child_nodes.append(child_node)

        return self.child_nodes

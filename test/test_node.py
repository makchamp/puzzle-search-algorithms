import sys
sys.path.insert(0, 'src')

from node import Node
from puzzle import Puzzle


def test_node_creation():
    setup_1 = [0, 2, 3, 1, 4, 6, 7, 5]
    setup_2 = [1, 2, 3, 0, 4, 6, 7, 5]
    setup_3 = [1, 2, 3, 4, 0, 6, 7, 5]
    setup_4 = [1, 2, 3, 4, 5, 6, 7, 0]
    setup_5 = [1, 2, 3, 4, 5, 0, 7, 6]

    node = Node(Puzzle(2, setup_1), None, None, None)
    assert node.puzzle.current_setup == setup_1

    node_2 = Node(Puzzle(2, setup_2), node, 'move_up', 1)
    assert node_2.puzzle.current_setup == setup_2
    assert node_2.parent == node
    assert node_2.depth == 1
    assert node_2.move_cost == 1
    assert node_2.total_cost == 1

    node_3 = Node(Puzzle(2, setup_3), node_2, 'move_wrapping', 2)
    assert node_3.puzzle.current_setup == setup_3
    assert node_3.parent == node_2
    assert node_3.depth == 2
    assert node_3.move_cost == 2
    assert node_3.total_cost == 3


def test_node_expand():
    setup_1 = [0, 2, 3, 1, 4, 6, 7, 5]

    puzzle = Puzzle(2, setup_1)
    node = Node(puzzle, None, None, None)


    successor_puzzle_tuples = puzzle.get_successors()
    actual_child_nodes = []

    for successor_puzzle_tuple in successor_puzzle_tuples:
        puzzle = successor_puzzle_tuple[0]
        move = successor_puzzle_tuple[1]
        cost = successor_puzzle_tuple[2]
        actual_child_nodes.append(Node(puzzle, node, move, cost))


    print('start_expanding')
    child_nodes = node.expand()

    for child_node in child_nodes:
        assert child_node in actual_child_nodes






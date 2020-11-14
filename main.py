from puzzle import Puzzle
from pprint import pprint

setup_1 = [[0,2,3,1],[4,6,2,5]]
setup_2 = [[1,2,3,0],[4,6,2,5]]
setup_3 = [[1,2,3,4],[0,6,2,5]]
setup_4 = [[1,2,3,4],[5,6,2,0]]

puzzle = Puzzle(setup_1)
print(puzzle)

puzzle.move_diagonal_long()
print(puzzle)

puzzle = Puzzle(setup_2)
print(puzzle)

puzzle.move_diagonal_long()
print(puzzle)

puzzle = Puzzle(setup_3)
print(puzzle)

puzzle.move_diagonal_long()
print(puzzle)

puzzle = Puzzle(setup_4)
print(puzzle)

puzzle.move_diagonal_long()
print(puzzle)

# puzzle.move_right()
# print(puzzle)

# puzzle.move_vertically()
# print(puzzle)


# puzzle.move_vertically()
# print(puzzle)

# puzzle.move_left()
# print(puzzle)


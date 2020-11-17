from puzzle import Puzzle
from pprint import pprint

setup_1 = [0,2,3,1,4,6,2,5]
setup_2 = [1,2,3,0,4,6,2,5]
setup_3 = [1,2,3,4,0,6,2,5]
setup_4 = [1,2,3,4,5,6,2,0]
setup_5 = [1,2,3,4,5,6,7,0,9,10,11,8]


puzzle = Puzzle(2, setup_1)
print('\n')
print(puzzle)
print(puzzle.possible_moves())


puzzle = Puzzle(2,setup_2)
print('\n')
print(puzzle)
print(puzzle.possible_moves())


puzzle = Puzzle(2,setup_3)
print('\n')
print(puzzle)
print(puzzle.possible_moves())



puzzle = Puzzle(2,setup_4)
print('\n')
print(puzzle)
print(puzzle.possible_moves())



puzzle = Puzzle(2,setup_5)
print('\n')
print(puzzle)
print(puzzle.possible_moves())


puzzle = Puzzle(3,setup_5)
print('\n')
print(puzzle)
print(puzzle.possible_moves())



puzzle = Puzzle(4,setup_5)
print('\n')
print(puzzle)
print(puzzle.possible_moves())

setup_6 = [1, 2, 3, 4, 5, 6, 7, 0, 9, 10, 11, 8]
puzzle = Puzzle(3,setup_6)
print('\n')
print(puzzle)
print(puzzle.possible_moves())

puzzle = Puzzle(4, [1, 2, 7, 4, 6, 3, 11, 5, 0, 8, 10, 9])
print(puzzle)
print(puzzle.possible_moves())
print(puzzle.is_empty_tile_corner())
print(puzzle.move_diagonal_short())

# puzzle = Puzzle(6,setup_5)
# print('\n')
# print(puzzle)
#
# puzzle = Puzzle(1,setup_5)
# print('\n')
# print(puzzle)
#
# puzzle = Puzzle(12,setup_5)
# print('\n')
# print(puzzle)


# puzzle.move_right()
# print(puzzle)

# puzzle.move_vertically()
# print(puzzle)


# puzzle.move_vertically()
# print(puzzle)

# puzzle.move_left()
# print(puzzle)

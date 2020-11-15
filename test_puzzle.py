from puzzle import Puzzle

def test_possible_moves_2x4():
    setup_1 = [0, 2, 3, 1, 4, 6, 7, 5]
    setup_2 = [1, 2, 3, 0, 4, 6, 7, 5]
    setup_3 = [1, 2, 3, 4, 0, 6, 7, 5]
    setup_4 = [1, 2, 3, 4, 5, 6, 7, 0]
    setup_5 = [1, 2, 3, 4, 5, 0, 7, 6]


    puzzle_1 = Puzzle(2, setup_1)
    possible_moves_p1 = ['move_wrapping', 'move_diagonal_short', 'move_diagonal_long', 'move_right', 'move_down']
    assert puzzle_1.possible_moves() == possible_moves_p1

    puzzle_2 = Puzzle(2, setup_2)
    possible_moves_p2 = ['move_wrapping', 'move_diagonal_short', 'move_diagonal_long', 'move_left', 'move_down']
    assert puzzle_2.possible_moves() == possible_moves_p2


    puzzle_3 = Puzzle(2, setup_3)
    possible_moves_p3 = ['move_wrapping', 'move_diagonal_short', 'move_diagonal_long', 'move_right', 'move_up']
    assert puzzle_3.possible_moves() == possible_moves_p3


    puzzle_4 = Puzzle(2, setup_4)
    possible_moves_p4 = ['move_wrapping', 'move_diagonal_short', 'move_diagonal_long', 'move_left', 'move_up']
    assert puzzle_4.possible_moves() == possible_moves_p4


    puzzle_5 = Puzzle(2, setup_5)
    possible_moves_p5 = ['move_right', 'move_left', 'move_up']
    assert puzzle_5.possible_moves() == possible_moves_p5


    return

def test_possible_moves_other_sizes():
    setup_6 = [1, 2, 3, 4, 5, 6, 7, 0, 9, 10, 11, 8]
    setup_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]

    puzzle_6 = Puzzle(2, setup_6)
    possible_moves_p6 = ['move_right', 'move_left', 'move_up']
    assert puzzle_6.possible_moves() == possible_moves_p6

    puzzle_7 = Puzzle(3, setup_6)
    possible_moves_p7 = ['move_left', 'move_down', 'move_up']
    assert puzzle_7.possible_moves() == possible_moves_p7

    puzzle_8 = Puzzle(4, setup_6)
    possible_moves_p8 = ['move_right', 'move_left', 'move_down', 'move_up']
    assert puzzle_8.possible_moves() == possible_moves_p8

    puzzle_9 = Puzzle(4, setup_7)
    possible_moves_p9 = ['move_wrapping', 'move_diagonal_short', 'move_diagonal_long', 'move_left', 'move_up']
    assert puzzle_9.possible_moves() == possible_moves_p9

    return


def test_move_up():

    puzzle = Puzzle(2, [1, 2, 3, 4, 0, 6, 7, 5])
    assert puzzle.move_up()[0].current_setup == [0, 2, 3, 4, 1, 6, 7, 5]

    puzzle = Puzzle(2, [1, 2, 3, 4, 6, 0, 7, 5])
    assert puzzle.move_up()[0].current_setup == [1, 0, 3, 4, 6, 2, 7, 5]

    puzzle = Puzzle(3, [1, 2, 3, 4, 6, 0, 7, 5 , 8])
    assert puzzle.move_up()[0].current_setup == [1, 2, 0, 4, 6, 3, 7, 5 , 8]

    puzzle = Puzzle(3, [1, 2, 3, 4, 6, 8, 7, 0, 5])
    assert puzzle.move_up()[0].current_setup == [1, 2, 3, 4, 0, 8, 7, 6, 5]

    return


def test_move_down():
    puzzle = Puzzle(2, [1, 2, 3, 0, 4, 6, 7, 5])
    assert puzzle.move_down()[0].current_setup == [1, 2, 3, 5, 4, 6, 7, 0]

    puzzle = Puzzle(2, [1, 0, 3, 4, 6, 2, 7, 5])
    assert puzzle.move_down()[0].current_setup == [1, 2, 3, 4, 6, 0, 7, 5]

    puzzle = Puzzle(3, [1, 2, 0, 4, 6, 3, 7, 5, 8])
    assert puzzle.move_down()[0].current_setup == [1, 2, 3, 4, 6, 0, 7, 5, 8]

    puzzle = Puzzle(3, [1, 2, 3, 4, 0, 8, 7, 6, 5])
    assert puzzle.move_down()[0].current_setup == [1, 2, 3, 4, 6, 8, 7, 0, 5]

    return


def test_move_right():

    puzzle = Puzzle(2, [1, 2, 3, 4, 0, 6, 7, 5])
    assert puzzle.move_right()[0].current_setup == [1, 2, 3, 4, 6, 0, 7, 5]
    assert puzzle.move_right()[0].rows == 2
    assert puzzle.move_right()[1] == 'move_right'
    assert puzzle.move_right()[2] == 1

    puzzle = Puzzle(2, [1, 0, 3, 4, 6, 2, 7, 5])
    assert puzzle.move_right()[0].current_setup == [1, 3, 0, 4, 6, 2, 7, 5]
    assert puzzle.move_right()[0].rows == 2
    assert puzzle.move_right()[1] == 'move_right'
    assert puzzle.move_right()[2] == 1

    puzzle = Puzzle(2, [0, 1, 3, 4, 6, 2, 7, 5])
    assert puzzle.move_right()[0].current_setup == [1, 0, 3, 4, 6, 2, 7, 5]
    assert puzzle.move_right()[0].rows == 2
    assert puzzle.move_right()[1] == 'move_right'
    assert puzzle.move_right()[2] == 1

    puzzle = Puzzle(2, [5, 1, 3, 4, 6, 2, 0, 7])
    assert puzzle.move_right()[0].current_setup == [5, 1, 3, 4, 6, 2, 7, 0]
    assert puzzle.move_right()[0].rows == 2
    assert puzzle.move_right()[1] == 'move_right'
    assert puzzle.move_right()[2] == 1

    puzzle = Puzzle(3, [1, 0, 2, 4, 6, 3, 7, 5, 8])
    assert puzzle.move_right()[0].current_setup == [1, 2, 0, 4, 6, 3, 7, 5, 8]
    assert puzzle.move_right()[0].rows == 3
    assert puzzle.move_right()[1] == 'move_right'
    assert puzzle.move_right()[2] == 1

    puzzle = Puzzle(3, [1, 2, 3, 4, 0, 8, 7, 6, 5])
    assert puzzle.move_right()[0].current_setup == [1, 2, 3, 4, 8, 0, 7, 6, 5]
    assert puzzle.move_right()[0].rows == 3
    assert puzzle.move_right()[1] == 'move_right'
    assert puzzle.move_right()[2] == 1

    return


def test_move_left():

    puzzle = Puzzle(2, [1, 2, 3, 4, 6, 0, 7, 5])
    assert puzzle.move_left()[0].current_setup == [1, 2, 3, 4, 0, 6, 7, 5]
    assert puzzle.move_left()[0].rows == 2
    assert puzzle.move_left()[1] == 'move_left'
    assert puzzle.move_left()[2] == 1

    puzzle = Puzzle(2, [1, 3, 0, 4, 6, 2, 7, 5])
    assert puzzle.move_left()[0].current_setup == [1, 0, 3, 4, 6, 2, 7, 5]
    assert puzzle.move_left()[0].rows == 2
    assert puzzle.move_left()[1] == 'move_left'
    assert puzzle.move_left()[2] == 1

    puzzle = Puzzle(2, [1, 0, 3, 4, 6, 2, 7, 5])
    assert puzzle.move_left()[0].current_setup == [0, 1, 3, 4, 6, 2, 7, 5]
    assert puzzle.move_left()[0].rows == 2
    assert puzzle.move_left()[1] == 'move_left'
    assert puzzle.move_left()[2] == 1

    puzzle = Puzzle(2, [5, 1, 3, 4, 6, 2, 7, 0])
    assert puzzle.move_left()[0].current_setup == [5, 1, 3, 4, 6, 2, 0, 7]
    assert puzzle.move_left()[0].rows == 2
    assert puzzle.move_left()[1] == 'move_left'
    assert puzzle.move_left()[2] == 1

    puzzle = Puzzle(3, [1, 2, 0, 4, 6, 3, 7, 5, 8])
    assert puzzle.move_left()[0].current_setup == [1, 0, 2, 4, 6, 3, 7, 5, 8]
    assert puzzle.move_left()[0].rows == 3
    assert puzzle.move_left()[1] == 'move_left'
    assert puzzle.move_left()[2] == 1

    puzzle = Puzzle(3, [1, 2, 3, 4, 8, 0, 7, 6, 5])
    assert puzzle.move_left()[0].current_setup == [1, 2, 3, 4, 0, 8, 7, 6, 5]
    assert puzzle.move_left()[0].rows == 3
    assert puzzle.move_left()[1] == 'move_left'
    assert puzzle.move_left()[2] == 1

    return


def test_move_wrapping():
    puzzle = Puzzle(2, [1, 2, 3, 4, 6, 5, 7, 0])
    assert puzzle.move_wrapping()[0].current_setup == [1, 2, 3, 4, 0, 5, 7, 6]
    assert puzzle.move_wrapping()[0].rows == 2
    assert puzzle.move_wrapping()[1] == 'move_wrapping'
    assert puzzle.move_wrapping()[2] == 2

    puzzle = Puzzle(2, [1, 2, 3, 4, 0, 5, 7, 6])
    assert puzzle.move_wrapping()[0].current_setup == [1, 2, 3, 4, 6, 5, 7, 0]
    assert puzzle.move_wrapping()[0].rows == 2
    assert puzzle.move_wrapping()[1] == 'move_wrapping'
    assert puzzle.move_wrapping()[2] == 2

    puzzle = Puzzle(2, [1, 2, 3, 0, 6, 5, 7, 4])
    assert puzzle.move_wrapping()[0].current_setup == [0, 2, 3, 1, 6, 5, 7, 4]
    assert puzzle.move_wrapping()[0].rows == 2
    assert puzzle.move_wrapping()[1] == 'move_wrapping'
    assert puzzle.move_wrapping()[2] == 2

    puzzle = Puzzle(2, [0, 2, 3, 1, 6, 5, 7, 4])
    assert puzzle.move_wrapping()[0].current_setup == [1, 2, 3, 0, 6, 5, 7, 4]
    assert puzzle.move_wrapping()[0].rows == 2
    assert puzzle.move_wrapping()[1] == 'move_wrapping'
    assert puzzle.move_wrapping()[2] == 2

    puzzle = Puzzle(3, [1, 2, 0, 4, 6, 3, 7, 5, 8])
    assert puzzle.move_wrapping()[0].current_setup == [0, 2, 1, 4, 6, 3, 7, 5, 8]
    assert puzzle.move_wrapping()[0].rows == 3
    assert puzzle.move_wrapping()[1] == 'move_wrapping'
    assert puzzle.move_wrapping()[2] == 2

    puzzle = Puzzle(3, [1, 2, 7, 4, 6, 3, 0, 5, 8])
    assert puzzle.move_wrapping()[0].current_setup == [1, 2, 7, 4, 6, 3, 8, 5, 0]
    assert puzzle.move_wrapping()[0].rows == 3
    assert puzzle.move_wrapping()[1] == 'move_wrapping'
    assert puzzle.move_wrapping()[2] == 2

    puzzle = Puzzle(3, [1, 2, 3, 4, 8, 5, 7, 6, 0])
    assert puzzle.move_wrapping()[0].current_setup == [1, 2, 3, 4, 8, 5, 0, 6, 7]
    assert puzzle.move_wrapping()[0].rows == 3
    assert puzzle.move_wrapping()[1] == 'move_wrapping'
    assert puzzle.move_wrapping()[2] == 2

    return

def test_move_diagonal_short():

    puzzle = Puzzle(2, [1, 2, 3, 4, 6, 5, 7, 0])
    assert puzzle.move_diagonal_short()[0].current_setup == [1, 2, 0, 4, 6, 5, 7, 3]
    assert puzzle.move_diagonal_short()[0].rows == 2
    assert puzzle.move_diagonal_short()[1] == 'move_diagonal_short'
    assert puzzle.move_diagonal_short()[2] == 3

    puzzle = Puzzle(2, [1, 2, 3, 4, 0, 5, 7, 6])
    assert puzzle.move_diagonal_short()[0].current_setup == [1, 0, 3, 4, 2, 5, 7, 6]
    assert puzzle.move_diagonal_short()[0].rows == 2
    assert puzzle.move_diagonal_short()[1] == 'move_diagonal_short'
    assert puzzle.move_diagonal_short()[2] == 3

    puzzle = Puzzle(2, [1, 2, 3, 0, 6, 5, 7, 4])
    assert puzzle.move_diagonal_short()[0].current_setup == [1, 2, 3, 7, 6, 5, 0, 4]
    assert puzzle.move_diagonal_short()[0].rows == 2
    assert puzzle.move_diagonal_short()[1] == 'move_diagonal_short'
    assert puzzle.move_diagonal_short()[2] == 3

    puzzle = Puzzle(2, [0, 2, 3, 1, 6, 5, 7, 4])
    assert puzzle.move_diagonal_short()[0].current_setup == [5, 2, 3, 1, 6, 0, 7, 4]
    assert puzzle.move_diagonal_short()[0].rows == 2
    assert puzzle.move_diagonal_short()[1] == 'move_diagonal_short'
    assert puzzle.move_diagonal_short()[2] == 3

    puzzle = Puzzle(3, [1, 2, 0, 4, 6, 3, 7, 5, 8])
    assert puzzle.move_diagonal_short()[0].current_setup == [1, 2, 6, 4, 0, 3, 7, 5, 8]
    assert puzzle.move_diagonal_short()[0].rows == 3
    assert puzzle.move_diagonal_short()[1] == 'move_diagonal_short'
    assert puzzle.move_diagonal_short()[2] == 3

    puzzle = Puzzle(3, [1, 2, 7, 4, 6, 3, 11, 5, 8, 9, 10, 0])
    assert puzzle.move_diagonal_short()[0].current_setup == [1, 2, 7, 4, 6, 3, 0, 5, 8, 9, 10, 11]
    assert puzzle.move_diagonal_short()[0].rows == 3
    assert puzzle.move_diagonal_short()[1] == 'move_diagonal_short'
    assert puzzle.move_diagonal_short()[2] == 3

    puzzle = Puzzle(4, [1, 2, 7, 4, 6, 3, 11, 5, 8, 9, 10, 0])
    assert puzzle.move_diagonal_short()[0].current_setup == [1, 2, 7, 4, 6, 3, 11, 0, 8, 9, 10, 5]
    assert puzzle.move_diagonal_short()[0].rows == 4
    assert puzzle.move_diagonal_short()[1] == 'move_diagonal_short'
    assert puzzle.move_diagonal_short()[2] == 3

    puzzle = Puzzle(4, [1, 2, 7, 4, 6, 3, 11, 5, 8, 0, 10, 9])
    assert puzzle.move_diagonal_short()[0].current_setup == [1, 2, 7, 4, 6, 3, 11, 0, 8, 5, 10, 9]
    assert puzzle.move_diagonal_short()[0].rows == 4
    assert puzzle.move_diagonal_short()[1] == 'move_diagonal_short'
    assert puzzle.move_diagonal_short()[2] == 3

    puzzle = Puzzle(4, [1, 2, 0, 4, 6, 3, 11, 5, 8, 7, 10, 9])
    assert puzzle.move_diagonal_short()[0].current_setup == [1, 2, 6, 4, 0, 3, 11, 5, 8, 7, 10, 9]
    assert puzzle.move_diagonal_short()[0].rows == 4
    assert puzzle.move_diagonal_short()[1] == 'move_diagonal_short'
    assert puzzle.move_diagonal_short()[2] == 3

    return

def test_move_diagonal_long():

    puzzle = Puzzle(2, [1, 2, 3, 4, 6, 5, 7, 0])
    assert puzzle.move_diagonal_long()[0].current_setup == [0, 2, 3, 4, 6, 5, 7, 1]
    assert puzzle.move_diagonal_long()[0].rows == 2
    assert puzzle.move_diagonal_long()[1] == 'move_diagonal_long'
    assert puzzle.move_diagonal_long()[2] == 3

    puzzle = Puzzle(2, [1, 2, 3, 4, 0, 5, 7, 6])
    assert puzzle.move_diagonal_long()[0].current_setup == [1, 2, 3, 0, 4, 5, 7, 6]
    assert puzzle.move_diagonal_long()[0].rows == 2
    assert puzzle.move_diagonal_long()[1] == 'move_diagonal_long'
    assert puzzle.move_diagonal_long()[2] == 3

    puzzle = Puzzle(2, [1, 2, 3, 0, 6, 5, 7, 4])
    assert puzzle.move_diagonal_long()[0].current_setup == [1, 2, 3, 6, 0, 5, 7, 4]
    assert puzzle.move_diagonal_long()[0].rows == 2
    assert puzzle.move_diagonal_long()[1] == 'move_diagonal_long'
    assert puzzle.move_diagonal_long()[2] == 3

    puzzle = Puzzle(2, [0, 2, 3, 1, 6, 5, 7, 4])
    assert puzzle.move_diagonal_long()[0].current_setup == [4, 2, 3, 1, 6, 5, 7, 0]
    assert puzzle.move_diagonal_long()[0].rows == 2
    assert puzzle.move_diagonal_long()[1] == 'move_diagonal_long'
    assert puzzle.move_diagonal_long()[2] == 3

    puzzle = Puzzle(3, [1, 2, 0, 4, 6, 3, 7, 5, 8])
    assert puzzle.move_diagonal_long()[0].current_setup == [1, 2, 7, 4, 6, 3, 0, 5, 8]
    assert puzzle.move_diagonal_long()[0].rows == 3
    assert puzzle.move_diagonal_long()[1] == 'move_diagonal_long'
    assert puzzle.move_diagonal_long()[2] == 3

    puzzle = Puzzle(3, [1, 2, 7, 4, 6, 3, 11, 5, 8, 9, 10, 0])
    assert puzzle.move_diagonal_long()[0].current_setup == [0, 2, 7, 4, 6, 3, 11, 5, 8, 9, 10, 1]
    assert puzzle.move_diagonal_long()[0].rows == 3
    assert puzzle.move_diagonal_long()[1] == 'move_diagonal_long'
    assert puzzle.move_diagonal_long()[2] == 3

    puzzle = Puzzle(4, [1, 2, 7, 4, 6, 3, 11, 5, 8, 9, 10, 0])
    assert puzzle.move_diagonal_long()[0].current_setup == [0, 2, 7, 4, 6, 3, 11, 5, 8, 9, 10, 1]
    assert puzzle.move_diagonal_long()[0].rows == 4
    assert puzzle.move_diagonal_long()[1] == 'move_diagonal_long'
    assert puzzle.move_diagonal_long()[2] == 3

    puzzle = Puzzle(4, [1, 2, 0, 4, 6, 3, 11, 5, 7, 8, 10, 9])
    assert puzzle.move_diagonal_long()[0].current_setup == [1, 2, 8, 4, 6, 3, 11, 5, 7, 0, 10, 9]
    assert puzzle.move_diagonal_long()[0].rows == 4
    assert puzzle.move_diagonal_long()[1] == 'move_diagonal_long'
    assert puzzle.move_diagonal_long()[2] == 3

    puzzle = Puzzle(4, [1, 2, 7, 4, 6, 3, 11, 5, 8, 0, 10, 9])
    assert puzzle.move_diagonal_long()[0].current_setup == [1, 2, 0, 4, 6, 3, 11, 5, 8, 7, 10, 9]
    assert puzzle.move_diagonal_long()[0].rows == 4
    assert puzzle.move_diagonal_long()[1] == 'move_diagonal_long'
    assert puzzle.move_diagonal_long()[2] == 3

    return
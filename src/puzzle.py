class Puzzle:

    # the cost of each move
    move_cost = {
        'move_wrapping': 2,
        'move_diagonal_short': 3,
        'move_diagonal_long': 3,
        'move_right': 1,
        'move_left': 1,
        'move_down': 1,
        'move_up': 1
    }

    def __init__(self, rows, setup, goal_setups=None, puzzle_number=None):

        self.initial_setup: [] = setup
        self.current_setup: [] = self.initial_setup
        self.puzzle_number = puzzle_number

        if rows < 2:
            raise Exception('there has to be at least two rows')
        self.rows: int = rows

        self.columns: int = int(len(self.current_setup) / self.rows)
        if self.columns < 2:
            raise Exception('there has to be at least two columns')

        self.total_cost = 0

        # add support for dynamic goal states
        if goal_setups is None:
            goal_setups = [[1, 2, 3, 4, 5, 6, 7, 0], [1, 3, 5, 7, 2, 4, 6, 0]]
        self.goal_setups = goal_setups

    def __str__(self):

        # # divide the long list into rows and columns depending on the puzzle size
        # sublists = []
        # for row in range(0, len(self.current_setup), self.columns):
        #     sublists.append(self.current_setup[row:row + self.columns])
        #
        # tiles = '\n'.join(' '.join(map(str, row)) for row in sublists)
        string_representaion = ' '.join(str(tile) for tile in self.current_setup)

        return string_representaion

    def possible_moves(self):
        possible_moves = []

        if self.is_empty_tile_corner():
            possible_moves.append('move_wrapping')
            possible_moves.append('move_diagonal_short')
            possible_moves.append('move_diagonal_long')

        if not self.is_empty_tile_on_right():
            possible_moves.append('move_right')

        if not self.is_empty_tile_on_left():
            possible_moves.append('move_left')

        if not self.is_empty_tile_on_bottom():
            possible_moves.append('move_down')

        if not self.is_empty_tile_on_top():
            possible_moves.append('move_up')

        return possible_moves

    # Check if the current state is the goal state
    def is_goal(self):

        return True if self.current_setup in self.goal_setups else False

    def is_empty_tile_corner(self):

        empty_tile_location = self.current_setup.index(0)
        corners = []

        if self.rows < 2:
            corners = [0, len(self.current_setup) - 1]
        else:
            corners = [0, self.columns - 1, len(self.current_setup) - self.columns, len(self.current_setup) - 1]

        # corners = [index for index in range(0, len(self.current_setup))
        #            if index % self.columns == 0 or index % self.columns == self.columns - 1]

        return True if empty_tile_location in corners else False

    def is_empty_tile_on_right(self):

        empty_tile_location = self.current_setup.index(0)

        right_corners = [index for index in range(0, len(self.current_setup)) if
                         index % self.columns == self.columns - 1]

        return True if empty_tile_location in right_corners else False

    def is_empty_tile_on_left(self):

        empty_tile_location = self.current_setup.index(0)

        left_corners = [index for index in range(0, len(self.current_setup)) if index % self.columns == 0]

        return True if empty_tile_location in left_corners else False

    def is_empty_tile_on_bottom(self):

        empty_tile_location = self.current_setup.index(0)

        # find the indices of the last row and check if the empty tile is between these indices
        bottom_row_start_index = len(self.current_setup) - self.columns
        bottom_row_end_index = len(self.current_setup) - 1

        return True if bottom_row_start_index <= empty_tile_location <= bottom_row_end_index else False

    def is_empty_tile_on_top(self):

        empty_tile_location = self.current_setup.index(0)

        # find the indices of the last row and check if the empty tile is between these indices
        top_row_start_index = 0
        top_row_end_index = self.columns - 1

        return True if top_row_start_index <= empty_tile_location <= top_row_end_index else False

    def move_up(self):
        # this method will create a new state when the empty tile is moved up

        if self.is_empty_tile_on_top():
            raise Exception('tried to move up when empty tile is already on top row')

        empty_tile_location = self.current_setup.index(0)

        replacement_tile_position = empty_tile_location - self.columns

        # create a new setup and replace the empty tile with the tile above
        new_setup = self.current_setup.copy()
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        # print("move_up applied")
        new_puzzle = Puzzle(setup=new_setup, rows=self.rows)
        move_name = "move_up"
        move_cost = self.move_cost[move_name]

        replacement_tile = self.current_setup[replacement_tile_position]

        return (new_puzzle, move_name, move_cost, replacement_tile)

    def move_down(self):
        # this method will create a new state when the empty tile is moved down

        if self.is_empty_tile_on_bottom():
            raise Exception('tried to move down when empty tile is already on bottom row')

        empty_tile_location = self.current_setup.index(0)
        replacement_tile_position = empty_tile_location + self.columns

        # create a new setup and replace the empty tile with the tile above
        new_setup = self.current_setup.copy()
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        new_puzzle = Puzzle(setup=new_setup, rows=self.rows)
        move_name = "move_down"
        move_cost = self.move_cost[move_name]

        replacement_tile = self.current_setup[replacement_tile_position]

        return (new_puzzle, move_name, move_cost, replacement_tile)

    def move_right(self):
        # this method will create a new state when the empty tile is moved right

        if self.is_empty_tile_on_right():
            raise Exception('tried to move right when empty tile is already on right corner')

        empty_tile_location = self.current_setup.index(0)
        replacement_tile_position = empty_tile_location + 1

        # create a new setup and replace the empty tile with the tile above
        new_setup = self.current_setup.copy()
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        #print("move_right applied")
        new_puzzle = Puzzle(setup=new_setup, rows=self.rows)
        move_name = "move_right"
        move_cost = self.move_cost[move_name]

        replacement_tile = self.current_setup[replacement_tile_position]

        return (new_puzzle, move_name, move_cost, replacement_tile)

    def move_left(self):
        # this method will create a new state when the empty tile is moved left

        if self.is_empty_tile_on_left():
            raise Exception('tried to move left when empty tile is already on left corner')

        empty_tile_location = self.current_setup.index(0)
        replacement_tile_position = empty_tile_location - 1

        # create a new setup and replace the empty tile with the tile above
        new_setup = self.current_setup.copy()
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        new_puzzle = Puzzle(setup=new_setup, rows=self.rows)
        move_name = "move_left"
        move_cost = self.move_cost[move_name]

        replacement_tile = self.current_setup[replacement_tile_position]

        return (new_puzzle, move_name, move_cost, replacement_tile)

    def move_wrapping(self):
        # this method will create a new state when the empty tile is moved to the other corner in the row

        if not self.is_empty_tile_corner():
            raise Exception('tried to move wrapping when empty tile is not on a corner')

        empty_tile_location = self.current_setup.index(0)
        replacement_tile_position: int = 0

        if empty_tile_location == 0:
            replacement_tile_position = self.columns - 1
        elif empty_tile_location == self.columns - 1:
            replacement_tile_position = 0
        elif empty_tile_location == len(self.current_setup) - self.columns:
            replacement_tile_position = len(self.current_setup) - 1
        else:
            replacement_tile_position = len(self.current_setup) - self.columns

        # create a new setup and replace the empty tile with the replacement tile
        new_setup = self.current_setup.copy()
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        new_puzzle = Puzzle(setup=new_setup, rows=self.rows)
        move_name = "move_wrapping"
        move_cost = self.move_cost[move_name]
        replacement_tile = self.current_setup[replacement_tile_position]

        return (new_puzzle, move_name, move_cost, replacement_tile)

    def move_diagonal_short(self):
        # this method will create a new state when the empty tile is moved diagonally

        if not self.is_empty_tile_corner():
            raise Exception('tried to move_diagonal_short when empty tile is not on a corner')

        empty_tile_location = self.current_setup.index(0)
        replacement_tile_position = 0

        if empty_tile_location == 0:  # top left corner
            replacement_tile_position = self.columns + 1
        elif empty_tile_location == self.columns - 1:  # top right corner
            replacement_tile_position = 2 * self.columns - 2
        elif empty_tile_location == len(self.current_setup) - self.columns: # bottom left corner
            replacement_tile_position = len(self.current_setup) - 2*self.columns + 1
        else:  # bottom right corner
            replacement_tile_position = len(self.current_setup) - self.columns - 2

        # create a new setup and replace the empty tile with the replacement tile
        new_setup = self.current_setup.copy()
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        #print("move_diagonal_short applied")
        new_puzzle = Puzzle(setup=new_setup, rows=self.rows)
        move_name = "move_diagonal_short"
        move_cost = self.move_cost[move_name]

        replacement_tile = self.current_setup[replacement_tile_position]

        return (new_puzzle, move_name, move_cost, replacement_tile)

    def move_diagonal_long(self):
        # this method will create a new state when the empty tile is moved to the oppisite corner

        if not self.is_empty_tile_corner():
            raise Exception('tried to move_diagonal_long when empty tile is not on a corner')

        empty_tile_location = self.current_setup.index(0)
        replacement_tile_position = 0

        if empty_tile_location == 0:  # top left corner
            replacement_tile_position = len(self.current_setup) - 1
        elif empty_tile_location == self.columns - 1:  # top right corner
            replacement_tile_position = len(self.current_setup) - self.columns
        elif empty_tile_location == len(self.current_setup) - self.columns: # bottom left corner
            replacement_tile_position = self.columns - 1
        else:  # bottom right corner
            replacement_tile_position = 0

        # create a new setup and replace the empty tile with the replacement tile
        new_setup = self.current_setup.copy()
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        #print("move_diagonal_long applied")
        new_puzzle = Puzzle(setup=new_setup, rows=self.rows)
        move_name = "move_diagonal_long"
        move_cost = self.move_cost[move_name]

        replacement_tile = self.current_setup[replacement_tile_position]

        return (new_puzzle, move_name, move_cost, replacement_tile)


    def get_successors(self):
        # this method will return all the successors of the current setup by applying all the possible actions

        successor_puzzles = []

        for action in self.possible_moves():
            if action == 'move_wrapping':
                successor_puzzles.append(self.move_wrapping())
                continue

            if action == 'move_diagonal_short':
                successor_puzzles.append(self.move_diagonal_short())
                continue

            if action == 'move_diagonal_long':
                successor_puzzles.append(self.move_diagonal_long())
                continue

            if action == 'move_right':
                successor_puzzles.append(self.move_right())
                continue

            if action == 'move_left':
                successor_puzzles.append(self.move_left())
                continue

            if action == 'move_down':
                successor_puzzles.append(self.move_down())
                continue

            if action == 'move_up':
                successor_puzzles.append(self.move_up())
                continue

        return successor_puzzles


    def get_heuristic(self, h=None):
        # this method will return the value of the heuristic

        if h == 'h1':
            return self.get_h1()
        elif h == 'h2':
            return self.get_h2()
        elif h == 'h0':
            return self.get_h0()

        return 0

    def get_h0(self):
        # this is the naive heuristic, h0 that will be used for the demo

        if self.current_setup.index(0) == len(self.current_setup) - 1:
            return 0

        return 1

    def get_h1(self):
        # Hamming distance: calculate how many tiles are out of place compared to the goal states

        misplaced_tiles_count_list = []

        # calculate how many misplaced tiles are in the current setup compared to all goal setups
        for goal_setup in self.goal_setups:
            misplaced_tiles_count = 0

            for i in range(0, len(self.current_setup)):
                if self.current_setup[i] != goal_setup[i]:
                    misplaced_tiles_count += 1

            misplaced_tiles_count_list.append(misplaced_tiles_count)

        # return the minimum count of misplaced tiles
        return min(misplaced_tiles_count_list)

    def get_h2(self):
        # this heuristic calculates the sum of permutation inversions

        per_goal_setup_calculation_list = []

        # calculate how many misplaced tiles are in the current setup compared to all goal setups
        for goal_setup in self.goal_setups:
            per_goal_setup_calculation_list.append(self.sum_of_permutation_inversions(goal_setup))

        # return the minimum of the sums
        return min(per_goal_setup_calculation_list)

    def get_num_of_rows(self):
        return self.rows

    def get_puzzle_num(self):
        return self.puzzle_number

    def get_initial_setup(self):
        return self.initial_setup               

    def sum_of_permutation_inversions(self, goal_setup):
        # print(goal_setup)
        sum_of_permutation = 1
        # for each tile, calculate how many tiles on the right should be on its left in the goal setup
        for i in range(0, len(self.current_setup)):
            current_tile = self.current_setup[i]

            if current_tile == 0:
                continue

            tiles_on_the_right = self.current_setup[i+1:]
            tile_index_in_goal_setup = goal_setup.index(current_tile)
            tiles_on_the_left = goal_setup[:tile_index_in_goal_setup]
            common_tiles = [tile for tile in tiles_on_the_right if tile in tiles_on_the_left]
            sum_of_permutation += len(common_tiles)

            # print(f'\n\ncurrent_tile {current_tile}')
            # print(f'tiles_on_the_right {tiles_on_the_right}')
            # print(f'tile_index_in_goal_setup {tile_index_in_goal_setup}')
            # print(f'tiles_on_the_left {tiles_on_the_left}')
            # print(f'common_tiles {common_tiles}')
            # print(f'sum_of_permutation {sum_of_permutation}')

        return sum_of_permutation



class Puzzle:

    def __init__(self, rows, setup):
        self.search_path = []
        self.solution_path = []
        self.current_setup = setup
        if rows < 2:
            raise Exception('there has to be at least two rows')
        self.rows: int = rows
        self.columns: int = int(len(self.current_setup) / self.rows)
        if self.columns < 2:
            raise Exception('there has to be at least two columns')

        self.total_cost = 0
        self.goal_setups = [[1, 2, 3, 4, 5, 6, 7, 0], [1, 3, 5, 7, 2, 4, 6, 0]]

    def __str__(self):

        # divide the long list into rows and columns depending on the puzzle size
        sublists = []
        for row in range(0, len(self.current_setup), self.columns):
            sublists.append(self.current_setup[row:row + self.columns])

        tiles = '\n'.join(' '.join(map(str, row)) for row in sublists)

        return tiles

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
        new_setup = self.current_setup
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        print("move_up applied")
        return new_setup

    def move_down(self):
        # this method will create a new state when the empty tile is moved down

        if self.is_empty_tile_on_bottom():
            raise Exception('tried to move down when empty tile is already on bottom row')

        empty_tile_location = self.current_setup.index(0)
        replacement_tile_position = empty_tile_location + self.columns

        # create a new setup and replace the empty tile with the tile above
        new_setup = self.current_setup
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        print("move_down applied")
        return new_setup

    def move_right(self):
        # this method will create a new state when the empty tile is moved right

        if self.is_empty_tile_on_right():
            raise Exception('tried to move right when empty tile is already on right corner')

        empty_tile_location = self.current_setup.index(0)
        replacement_tile_position = empty_tile_location + 1

        # create a new setup and replace the empty tile with the tile above
        new_setup = self.current_setup
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        print("move_right applied")
        return new_setup

    def move_left(self):
        # this method will create a new state when the empty tile is moved left

        if self.is_empty_tile_on_left():
            raise Exception('tried to move left when empty tile is already on left corner')

        empty_tile_location = self.current_setup.index(0)
        replacement_tile_position = empty_tile_location - 1

        # create a new setup and replace the empty tile with the tile above
        new_setup = self.current_setup
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        print("move_left applied")
        return new_setup

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
        new_setup = self.current_setup
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        print("move_wrapping applied")
        return new_setup

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
        new_setup = self.current_setup
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        print("move_diagonal_short applied")
        return new_setup

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
        new_setup = self.current_setup
        new_setup[empty_tile_location] = new_setup[replacement_tile_position]
        new_setup[replacement_tile_position] = 0

        print("move_diagonal_long applied")
        return new_setup

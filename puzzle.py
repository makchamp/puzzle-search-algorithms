class Puzzle:

    def __init__(self, setup):
        self.search_path = []
        self.solution_path = []
        self.current_setup = setup
        self.total_cost = 0

    def __str__(self):

        tiles = '\n'.join(' '.join(map(str, row)) for row in self.current_setup)
        # for tile in self.current_setup:
        #     print(*tile)

        return tiles

    def is_empty_tile_corner(self):

        if self.current_setup[0][0] == 0 or self.current_setup[1][0] == 0 \
                or self.current_setup[0][3] == 0 or self.current_setup[1][3] == 0:
            return True

        return False

    def move_vertically(self):

        if 0 in self.current_setup[0]:
            # find the index of the empty tile and the value of the replacement tile
            empty_tile_position = self.current_setup[0].index(0)
            replacement_tile = self.current_setup[1][empty_tile_position]

            # replace the two tiles
            self.current_setup[0][empty_tile_position] = replacement_tile
            self.current_setup[1][empty_tile_position] = 0

        else:

            # find the index of the empty tile and the value of the replacement tile
            empty_tile_position = self.current_setup[1].index(0)
            replacement_tile = self.current_setup[0][empty_tile_position]

            # replace the two tiles
            self.current_setup[1][empty_tile_position] = replacement_tile
            self.current_setup[0][empty_tile_position] = 0

        self.total_cost += 1
        print("move_vertically applied")
        return

    def move_right(self):

        # if 0 is already on the right, then throw an error
        if self.current_setup[0][3] == 0 or self.current_setup[1][3] == 0:

            raise Exception("Tried move_right but the empty tile is already on the right")

        else:

            # first find the if the empty tile is on the top or bottom row
            row = 0 if 0 in self.current_setup[0] else 1

            # find the index of the empty tile and the value of the replacement tile
            empty_tile_position = self.current_setup[row].index(0)
            replacement_tile = self.current_setup[row][empty_tile_position + 1]

            # replace the two tiles
            self.current_setup[row][empty_tile_position] = replacement_tile
            self.current_setup[row][empty_tile_position + 1] = 0

        self.total_cost += 1
        print("move_right applied")
        return

    def move_left(self):

        # if 0 is already on the left, then throw an error
        if self.current_setup[0][0] == 0 or self.current_setup[1][0] == 0:

            raise Exception("Tried move_left but the empty tile is already on the left")

        else:

            # first find the if the empty tile is on the top or bottom row
            row = 0 if 0 in self.current_setup[0] else 1

            # find the index of the empty tile and the value of the replacement tile
            empty_tile_position = self.current_setup[row].index(0)
            replacement_tile = self.current_setup[row][empty_tile_position - 1]

            # replace the two tiles
            self.current_setup[row][empty_tile_position] = replacement_tile
            self.current_setup[row][empty_tile_position - 1] = 0

        self.total_cost += 1
        print("move_left applied")
        return

    def move_wrapping(self):

        # if 0 is already not on a corner, then throw an error
        if not self.is_empty_tile_corner():

            raise Exception("Tried move_wrapper but the empty tile is not on the corner")

        else:

            # first find the if the empty tile is on the top or bottom row
            row = 0 if 0 in self.current_setup[0] else 1

            # find the indices of the empty and replacement tiles
            empty_tile_position = self.current_setup[row].index(0)
            replacement_tile_position = 3 if empty_tile_position == 0 else 0
            replacement_tile = self.current_setup[row][replacement_tile_position]

            # replace the two tiles
            self.current_setup[row][empty_tile_position] = replacement_tile
            self.current_setup[row][replacement_tile_position] = 0

        self.total_cost += 2
        print("move_wrapping applied")
        return

    def move_diagonal_short(self):

        # if 0 is already not on a corner, then throw an error
        if not self.is_empty_tile_corner():

            raise Exception("Tried move_diagonal_short but the empty tile is not on the corner")

        else:

            # first find the if the empty tile is on the top or bottom row
            row = 0 if 0 in self.current_setup[0] else 1

            # find the indices of the empty and replacement tiles
            empty_tile_position = self.current_setup[row].index(0)
            replacement_tile_position = 1 if empty_tile_position == 0 else 2
            replacement_tile = self.current_setup[row - 1][replacement_tile_position]

            # replace the two tiles
            self.current_setup[row][empty_tile_position] = replacement_tile
            self.current_setup[row - 1][replacement_tile_position] = 0

        self.total_cost += 3
        print("move_diagonal_short applied")
        return

    def move_diagonal_long(self):

        # if 0 is already not on a corner, then throw an error
        if not self.is_empty_tile_corner():

            raise Exception("Tried move_diagonal_long but the empty tile is not on the corner")

        else:

            # first find the if the empty tile is on the top or bottom row
            row = 0 if 0 in self.current_setup[0] else 1

            # find the indices of the empty and replacement tiles
            empty_tile_position = self.current_setup[row].index(0)
            replacement_tile_position = 3 if empty_tile_position == 0 else 0
            replacement_tile = self.current_setup[row - 1][replacement_tile_position]

            # replace the two tiles
            self.current_setup[row][empty_tile_position] = replacement_tile
            self.current_setup[row - 1][replacement_tile_position] = 0

        self.total_cost += 3
        print("move_diagonal_long applied")
        return

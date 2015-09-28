"""
Clone of 2048 game.
"""

import poc_2048_gui
import random;

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
    result = [];
    for dummy_num in range(len(line)):
        result.append(0);
    current_pos = 0;
    target_pos = 0;
    current_num = 0;
    for current_pos in range(len(line)):
        if (line[current_pos] != 0):
            if (current_num == 0):
                current_num = line[current_pos];
            elif (current_num != line[current_pos]):
                result[target_pos] = current_num;
                target_pos += 1;
                current_num = line[current_pos];
            else:
                result[target_pos] = current_num * 2;
                target_pos += 1;
                current_num = 0;
    if (current_num != 0):
        result[target_pos] = current_num;
    return result;

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Takes the height and width of the grid
        and creates the initial 2048 board
        """
        self._grid_height = grid_height;
        self._grid_width = grid_width;
        self.reset();
        self._starts = {UP:[(0, col) for col in range(self._grid_width)],
                       DOWN:[(self._grid_height - 1, col) for col in range(self._grid_width)],
                       LEFT:[(row, 0) for row in range(self._grid_height)],
                       RIGHT:[(row, self._grid_width - 1) for row in range(self._grid_height)]};

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._data = [[0 for dummy_col in range(self._grid_width)]
                     for dummy_row in range(self._grid_height)];
        for dummy_num in range(2):
            self.new_tile();

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        result = "";
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                result += str(self._data[row][col]) + " ";
            result += "\n";
        return result;

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height;

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width;

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if (UP == direction or DOWN == direction):
            steps = self._grid_height;
        else:
            steps = self._grid_width;
        start = self._starts[direction];
        offset = OFFSETS[direction];
        moved = False;
        for point in start:
            points_to_move = [];
            for order in range(steps):
                points_to_move.append(self._data[point[0] + offset[0] * order]
                                                [point[1] + offset[1] * order]);
            points_after_move = merge(points_to_move);
            for order in range(steps):
                if (self._data[point[0] + offset[0] * order]
                              [point[1] + offset[1] * order] != points_after_move[order]):
                    moved = True;
                self._data[point[0] + offset[0] * order][point[1] + offset[1] * order] = points_after_move[order];
        if (moved):
            self.new_tile();

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        col = random.randrange(0, self._grid_width);
        row = random.randrange(0, self._grid_height);
        while (self._data[row][col] != 0):
            col = random.randrange(0, self._grid_width);
            row = random.randrange(0, self._grid_height);
        if (random.randrange(0, 10) == 0):
            self._data[row][col] = 4;
        else:
            self._data[row][col] = 2;

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._data[row][col] = value;

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._data[row][col];


#poc_2048_gui.run_gui(TwentyFortyEight(5, 4))

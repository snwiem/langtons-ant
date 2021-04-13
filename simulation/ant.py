from enum import Enum
from simulation.grid import Color


class Direction(Enum):
    """
    The four directions the ant is allowed to move
    """
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Turn(Enum):
    """
    The direction to change to on certain conditions
    """
    RIGHT = 0
    LEFT = 1

class Ant:

    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.direction = Direction.NORTH

    def forward(self):
        """
        Simply moves the ant towards the current direction by one step
        :return: None
        """
        if self.direction == Direction.NORTH:
            self.y_pos -= 1
        elif self.direction == Direction.EAST:
            self.x_pos += 1
        elif self.direction == Direction.SOUTH:
            self.y_pos += 1
        elif self.direction == Direction.WEST:
            self.x_pos -= 1

    def turn(self, direction):
        """
        Changes the direction the ant is heading to
        :param direction: either Turn.LEFT or Turn.RIGHT
        :return: None
        """
        if direction == Turn.RIGHT:
            new_direction_value = self.direction.value + 1
            if new_direction_value >= len(Direction):
                new_direction_value = 0
        elif direction == Turn.LEFT:
            new_direction_value = self.direction.value - 1
            if new_direction_value < 0:
                new_direction_value = len(Direction)-1
        self.direction = Direction(new_direction_value)


    def move(self, grid):
        """
        This implements the basic ruleset for Langton's ant.
        If the color of the cell the ant is currently sitting on is Color.WHITE the ant turns Turn.RIGHT.
        If the color of the cell is Color.BLACK. The ant turns Turn.LEFT. After changing the direction the
        ant makes a step toward this new direction. Finally the cell the ant was placed on flips color.
        :param grid: The grid containing the cell information
        :return: None
        """
        if Color.WHITE == grid.cell_color(self.x_pos, self.y_pos):
            self.turn(Turn.RIGHT)
        else:
            self.turn(Turn.LEFT)
        grid.flip_color(self.x_pos, self.y_pos)
        self.forward()
        grid.adjust_dimensions(self.x_pos, self.y_pos)
        # log.debug('(%d, %d) -> %s' % (self.x_pos, self.y_pos, self.direction.name))





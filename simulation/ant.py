from enum import Enum
import logging as log
from simulation.grid import Color


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Turn(Enum):
    RIGHT = 0
    LEFT = 1

class Ant:

    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.direction = Direction.NORTH

    def forward(self):
        if self.direction == Direction.NORTH:
            self.y_pos -= 1
        elif self.direction == Direction.EAST:
            self.x_pos += 1
        elif self.direction == Direction.SOUTH:
            self.y_pos += 1
        elif self.direction == Direction.WEST:
            self.x_pos -= 1

    def turn(self, direction):
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
        if Color.WHITE == grid.cell_color(self.x_pos, self.y_pos):
            self.turn(Turn.RIGHT)
        else:
            self.turn(Turn.LEFT)
        grid.flip_color(self.x_pos, self.y_pos)
        self.forward()
        log.debug('(%d, %d) -> %s' % (self.x_pos, self.y_pos, self.direction.name))





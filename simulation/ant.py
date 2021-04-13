from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Ant:

    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.direction = Direction.NORTH
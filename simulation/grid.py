from enum import Enum


class Color(Enum):
    """
    Simple enum for color interpretation of the grid.
    """
    BLACK = 0
    WHITE = 1


class Grid:
    """
    The grid contains information about the cell states the ant requires to make decisions.

    This implementation just stores information about the Color.BLACK cells. This removes boundries
    from grid. Only limitations are the machine the simulation is running on.
    """

    def __init__(self):
        self.cells = {}
        self._min_x = self._min_y = self._max_x = self._max_y = 0

    def adjust_dimensions(self, x, y):
        self._min_x = min(self._min_x, x)
        self._max_x = max(self._max_x, x)
        self._min_y = min(self._min_y, y)
        self._max_y = max(self._max_y, y)

    def add_cell(self, x, y):
        """
        Adds a cell to the grid at the given coordinates. The added cell is interpreted to have the color Color.BLACK
        (see cell_color())
        :param x: The x-coordinate
        :param y: The y-coordinate
        :return: None
        """
        if x in self.cells:
            self.cells[x].add(y)
        else:
            self.cells[x] = {y}

    def remove_cell(self, x, y):
        """
        Removes a Color.BLACK cell from the grid. If the cell does not exist, nothing happens.

        :param x: The x-coordinate
        :param y: The y-coordinate
        :return: None
        """
        try:
            self.cells[x].remove(y)
            if 0 == len(self.cells[x]):
                del self.cells[x]
        except KeyError:
            pass

    def cell_color(self, x, y):
        """
        Returns the color of the cell for the given coordinates. If the coordinates are known to the grid those
        are interpreted to indicate a Color.BLACK cell. If no such coordinates are known to the grid, the cell is
        iterpreted to be Color.WHITE
        :param x: The x-coordinate
        :param y: The y-coordinate
        :return: None
        """
        try:
            if y in self.cells[x]:
                return Color.BLACK
        except KeyError:
            pass
        return Color.WHITE

    def flip_color(self, x, y):
        """
        Simply flips the color of the cell at the given coordinates. As the color is only interpreted by cell_color(x, y)
        internally the method removes a known cell from the grid or adds the coordinates if not already known.
        :param x:
        :param y:
        :return:
        """
        try:
            self.cells[x].remove(y)
        except KeyError:
            self.add_cell(x, y)

    @property
    def width(self):
        return abs(self._min_x - self._max_x) + 1

    @property
    def height(self):
        return abs(self._min_y - self._max_y) + 1

    @property
    def min_x(self):
        return self._min_x

    @property
    def min_y(self):
        return self._min_y

    @property
    def max_x(self):
        return self._max_x

    @property
    def max_y(self):
        return self._max_y

from enum import Enum

class Color(Enum):
    BLACK = 0
    WHITE = 1

class Grid:

    def __init__(self):
        self.cells = {}
        self._min_x = self._min_y = self._max_x = self._max_y = 0

    def _adjust_dimensions(self, x, y):
        self._min_x = min(self._min_x, x)
        self._max_x = max(self._max_x, x)
        self._min_y = min(self._min_y, y)
        self._max_y = max(self._max_y, y)

    def add_cell(self, x, y):
        self._adjust_dimensions(x, y)
        if x in self.cells:
            self.cells[x].add(y)
        else:
            self.cells[x] = {y}

    def remove_cell(self, x, y):
        try:
            self.cells[x].remove(y)
            if 0 == len(self.cells[x]):
                del self.cells[x]
        except KeyError:
            pass

    def cell_color(self, x, y):
        try:
            if y in self.cells[x]:
                return Color.BLACK
        except KeyError:
            pass
        return Color.WHITE

    def flip_color(self, x, y):
        try:
            self.cells[x].remove(y)
        except KeyError:
            self.add_cell(x, y)

    @property
    def width(self):
        return abs(self._min_x - self._max_x)

    @property
    def height(self):
        return abs(self._min_y - self._max_y)

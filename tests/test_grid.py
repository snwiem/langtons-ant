import pytest as pt
from simulation.grid import Grid, Color


def test_add_cell():
    grid = Grid()
    assert 0 == len(grid.cells)
    grid.add_cell(-3, 5)
    assert 1 == len(grid.cells)
    assert 1 == len(grid.cells[-3])


def test_remove_cell():
    grid = Grid()
    grid.cells = {-3: {5}}
    assert 1 == len(grid.cells)
    assert 1 == len(grid.cells[-3])
    # should to nothing
    grid.remove_cell(0, 0)
    assert 1 == len(grid.cells)
    assert 1 == len(grid.cells[-3])
    # should also do nothing
    grid.remove_cell(0, 5)
    assert 1 == len(grid.cells)
    assert 1 == len(grid.cells[-3])
    # should also do nothing
    grid.remove_cell(-3, 0)
    assert 1 == len(grid.cells)
    assert 1 == len(grid.cells[-3])
    # should empty grid cells
    grid.remove_cell(-3, 5)
    assert 0 == len(grid.cells)


def test_adjust_dimensions():
    grid = Grid()
    grid.adjust_dimensions(3, 5)
    assert grid._min_x == 0 and grid._max_x == 3
    assert grid._min_y == 0 and grid._max_y == 5
    grid.adjust_dimensions(-2, 7)
    assert grid._min_x == -2 and grid._max_x == 3
    assert grid._min_y == 0 and grid._max_y == 7
    grid.adjust_dimensions(-1, -4)
    assert grid._min_x == -2 and grid._max_x == 3
    assert grid._min_y == -4 and grid._max_y == 7


def test_width_and_height():
    grid = Grid()
    grid.adjust_dimensions(3, 5)
    assert grid.width == 4
    assert grid.height == 6
    grid.adjust_dimensions(-2, 7)
    assert grid.width == 6
    assert grid.height == 8
    grid.adjust_dimensions(-1, -4)
    assert grid.width == 6
    assert grid.height == 12


def test_cell_color():
    grid = Grid()
    grid.cells = {-3: {5}, 2: {-1}}
    assert Color.WHITE == grid.cell_color(0, 0)
    assert Color.WHITE == grid.cell_color(-23, 101)
    assert Color.BLACK == grid.cell_color(-3, 5)
    assert Color.WHITE == grid.cell_color(-3, 4)
    assert Color.BLACK == grid.cell_color(2, -1)
    assert Color.WHITE == grid.cell_color(2, 2)

def test_flip_color():
    grid = Grid()
    grid.cells = {-3: {5}, 2: {-1}}
    assert Color.WHITE == grid.cell_color(0, 0)
    assert Color.BLACK == grid.cell_color(-3, 5)
    grid.flip_color(0, 0)
    assert Color.BLACK == grid.cell_color(0, 0)
    grid.flip_color(-3, 5)
    assert Color.WHITE == grid.cell_color(-3, 5)
    assert Color.BLACK == grid.cell_color(2, -1)
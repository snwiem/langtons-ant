import pytest as pt
from pytest_mock import mocker

from simulation.grid import Grid, Color

from simulation.ant import Ant, Direction, Turn


@pt.mark.parametrize(('direction', 'position'),
                     [(Direction.NORTH, (0, -1)),
                      (Direction.SOUTH, (0, 1)),
                      (Direction.EAST, (1, 0)),
                      (Direction.WEST, (-1, 0))])
def test_forward(direction, position):
    ant = Ant()
    assert 0 == ant.x_pos
    assert 0 == ant.y_pos
    ant.direction = direction
    ant.forward()
    assert ant.x_pos == position[0]
    assert ant.y_pos == position[1]


@pt.mark.parametrize(('initial_direction', 'direction', 'result_direction'),
                     [(Direction.NORTH, Turn.LEFT, Direction.WEST),
                      (Direction.NORTH, Turn.RIGHT, Direction.EAST),
                      (Direction.EAST, Turn.LEFT, Direction.NORTH),
                      (Direction.EAST, Turn.RIGHT, Direction.SOUTH),
                      (Direction.SOUTH, Turn.LEFT, Direction.EAST),
                      (Direction.SOUTH, Turn.RIGHT, Direction.WEST),
                      (Direction.WEST, Turn.LEFT, Direction.SOUTH),
                      (Direction.WEST, Turn.RIGHT, Direction.NORTH)])
def test_turn(initial_direction, direction, result_direction):
    ant = Ant()
    ant.direction = initial_direction
    ant.turn(direction)
    assert ant.direction == result_direction


@pt.mark.parametrize('initial_direction, cell_color, expected_position, expected_direction',
                     [(Direction.NORTH, Color.WHITE, (1, 0), Direction.EAST),
                      (Direction.EAST, Color.WHITE, (0, 1), Direction.SOUTH),
                      (Direction.SOUTH, Color.WHITE, (-1, 0), Direction.WEST),
                      (Direction.WEST, Color.WHITE, (0, -1), Direction.NORTH),
                      (Direction.NORTH, Color.BLACK, (-1, 0), Direction.WEST),
                      (Direction.WEST, Color.BLACK, (0, 1), Direction.SOUTH),
                      (Direction.SOUTH, Color.BLACK, (1, 0), Direction.EAST),
                      (Direction.EAST, Color.BLACK, (0, -1), Direction.NORTH)])
def test_move(mocker, initial_direction, cell_color, expected_position, expected_direction):
    grid = mocker.patch.object(Grid, 'cell_color')
    grid.cell_color.return_value = cell_color
    ant = Ant()
    ant.x_pos = 0
    ant.y_pos = 0
    ant.direction = initial_direction
    ant.move(grid)
    grid.cell_color.assert_called_with(0, 0)
    grid.flip_color.assert_called_with(0, 0)
    assert ant.x_pos == expected_position[0]
    assert ant.y_pos == expected_position[1]
    assert ant.direction == expected_direction

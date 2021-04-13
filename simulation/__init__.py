import logging
import time

from simulation.ant import Ant
from simulation.grid import Grid


def main():
    """
    Simple entry point to the Langton's ant simulation.
    The simulation will run at 5 frames per second
    :return: None
    """
    logging.basicConfig(level=logging.DEBUG)
    grid = Grid()
    ant = Ant()
    moves = 0
    while True:
        ant.move(grid)
        moves += 1
        time.sleep(0.2)

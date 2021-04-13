import logging
import time

from simulation.ant import Ant
from simulation.grid import Grid


def main():
    logging.basicConfig(level=logging.DEBUG)
    grid = Grid()
    ant = Ant()
    moves = 0
    while True:
        ant.move(grid)
        moves += 1
        time.sleep(0.2)

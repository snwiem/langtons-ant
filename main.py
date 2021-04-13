import time

from simulation import main
from visuals.game import Game
import logging

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    game = Game()
    game.run()

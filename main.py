from visuals.game import Game
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    game = Game()
    game.run()

import pygame as pg
import logging as log

from simulation import Ant


class AntSprite(pg.sprite.Sprite):

    def __init__(self, cell_size):
        pg.sprite.Sprite.__init__(self)
        self.ant = Ant()
        self.image = pg.surface.Surface((cell_size, cell_size))
        self.image.fill(pg.Color('red'))
        self.rect = self.image.get_rect()

    def update(self, grid, td):
        log.debug("update called (td=%f)" % td)
        self.ant.move(grid)



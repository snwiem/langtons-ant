import pygame as pg
import logging as log

from simulation import Ant, Grid


class Game:
    SCREEN_WIDTH = SCREEN_HEIGHT = 800
    FRAMES_PER_SECOND = 60
    FRAME_TIMES = [10, 25, 50, 100, 200, 500, 1000]

    def __init__(self):
        pg.init()
        self._running = False
        self._paused = False
        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.grid = Grid()
        self.ant = Ant()
        self.time_delta = 0
        self.frame_time = len(self.FRAME_TIMES) // 2
        self.frame = 0

    def handle_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self._running = False
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self._running = False
                    return
                if event.key == pg.K_SPACE:
                    self._paused = not self._paused
                if not self._paused:
                    if event.key == pg.K_MINUS or event.key == pg.K_KP_MINUS:
                        self.frame_time += 1
                        if self.frame_time >= len(self.FRAME_TIMES):
                            self.frame_time = len(self.FRAME_TIMES) - 1
                    if event.key == pg.K_PLUS or event.key == pg.K_KP_PLUS:
                        self.frame_time -= 1
                        if self.frame_time < 0:
                            self.frame_time = 0

    def draw_grid(self):
        self.screen.fill(pg.Color('white'))
        cell_width = self.SCREEN_WIDTH / self.grid.width
        cell_height = self.SCREEN_HEIGHT / self.grid.height

        for col in range(self.grid.width):
            pg.draw.line(self.screen, pg.Color('black'), (col * cell_width, 0), (col * cell_width, self.SCREEN_HEIGHT))
        for row in range(self.grid.height):
            pg.draw.line(self.screen, pg.Color('black'), (0, row * cell_height), (self.SCREEN_WIDTH, row * cell_height))

        min_x = self.grid.min_x
        min_y = self.grid.min_y
        for cell in self.grid.cells.items():
            cell_x = cell[0]
            for cell_y in cell[1]:
                relative_x = cell_x + abs(min(0, min_x))
                relative_y = cell_y + abs(min(0, min_y))
                pg.draw.rect(self.screen, pg.Color('blue'), (relative_x * cell_width, relative_y * cell_height, cell_width, cell_height))

    def draw_ant(self):
        cell_width = self.SCREEN_WIDTH / self.grid.width
        cell_height = self.SCREEN_HEIGHT / self.grid.height
        min_x = self.grid.min_x
        min_y = self.grid.min_y
        relative_x = self.ant.x_pos + abs(min(0, min_x))
        relative_y = self.ant.y_pos + abs(min(0, min_y))
        pg.draw.rect(self.screen, pg.Color('red'), (relative_x * cell_width, relative_y * cell_height, cell_width, cell_height))

    def update_screen(self):
        self.draw_grid()
        self.draw_ant()
        pg.display.flip()

    def run(self):
        self._running = True
        while self._running:
            self.handle_events()

            if not self._paused:
                if self.time_delta > self.FRAME_TIMES[self.frame_time]:
                    self.time_delta = 0
                    self.ant.move(self.grid)
                    self.frame += 1
                    self.update_screen()
                self.time_delta += self.clock.tick(self.FRAMES_PER_SECOND)

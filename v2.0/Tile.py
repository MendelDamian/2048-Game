import pygame
from global_const import *


class Tile:
    _ids = 0

    # Formula to get size of one tile
    tile_size = HEIGHT * 0.82 / BOARD_SIZE
    # Formula to get size of space between tiles
    space = HEIGHT * 0.03 / BOARD_SIZE

    def __init__(self):
        self.id = Tile._ids
        Tile._ids += 1

        # Window of action should be a square
        self.x1 = FIRST_X + (self.space + self.tile_size) * (self.id % BOARD_SIZE)
        self.y1 = FIRST_Y + (self.space + self.tile_size) * (self.id // BOARD_SIZE)

        self.cords = (self.x1, self.y1, self.tile_size, self.tile_size)

        self.value = 0
        self.color = (0, 0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.cords)

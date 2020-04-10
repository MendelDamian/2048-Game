import pygame
from global_const import WIDTH, HEIGHT, BOARD_SIZE


class Tile:
    # Id of each tile
    _ids = 0

    def __init__(self):
        # Indexing tiles
        self.id = Tile._ids
        Tile._ids += 1

        # Set X's and Y's
        self.set_pos()

        # Value of tile
        self.value = 0
        # RGB color of tile
        self.color = (0, 0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.cords)

    def set_pos(self):
        # Formula to get size of one tile
        Tile._tile_size = HEIGHT * 0.82 / BOARD_SIZE
        # Formula to get size of space between tiles
        Tile._space = HEIGHT * 0.03 / BOARD_SIZE
        # Formula to get cordinates of first tile
        Tile._start_x = int(WIDTH / 2 - (BOARD_SIZE / 2 * Tile._tile_size))
        Tile._start_y = int(HEIGHT / 2 - (BOARD_SIZE / 2 * Tile._tile_size))
        # Update X's and Y's
        self.x1 = Tile._start_x + (Tile._space + Tile._tile_size) * (self.id % BOARD_SIZE)
        self.y1 = Tile._start_y + (Tile._space + Tile._tile_size) * (self.id // BOARD_SIZE)
        # Cordinates of beggining and end
        self.cords = (self.x1, self.y1, Tile._tile_size, Tile._tile_size)

import pygame
from global_const import RESOLUTION, MONITOR_RESOLUTION, BOARD_SIZE


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
        """Draw tiles on the passed screen surface.
        
        Args:
            screen (pygame.Surface): Surface to draw
        """
        pygame.draw.rect(screen, self.color, self.cords)

    def set_pos(self, fullscreen=False, width=0, height=0):
        """Setup and update tiles position
        
        Args:
            fullscreen (bool, optional, default=False): Is fullscreen
            width (int, optional, default=0): Surface width
            height (int, optional, default=0): Surface height
        """
        window_size = (width, height) if width and height else MONITOR_RESOLUTION if fullscreen else RESOLUTION
        # Formula to get size of one tile
        Tile._tile_size = window_size[1] * 0.82 / BOARD_SIZE
        # Formula to get size of space between tiles
        Tile._space = window_size[1] * 0.03 / BOARD_SIZE
        # Formula to get cordinates of first tile
        Tile._start_x = int(window_size[0] / 2 - (BOARD_SIZE / 2 * Tile._tile_size))
        Tile._start_y = int(window_size[1] / 2 - (BOARD_SIZE / 2 * Tile._tile_size))
        # Update X's and Y's
        self.x1 = Tile._start_x + (Tile._space + Tile._tile_size) * (self.id % BOARD_SIZE)
        self.y1 = Tile._start_y + (Tile._space + Tile._tile_size) * (self.id // BOARD_SIZE)
        # Cordinates of beggining and end
        self.cords = (self.x1, self.y1, Tile._tile_size, Tile._tile_size)

import pygame
from render_text import render_text
from global_const import *


class Tile:
    # Id of each tile
    _ids = 0
    
    def __init__(self):
        # Indexing tiles
        self.id = Tile._ids
        Tile._ids += 1
        # Needed for tiles's background
        Tile._ids = Tile._ids % (BOARD_SIZE * BOARD_SIZE)
        # Set X's and Y's
        self.set_pos()
        # Value of tile
        self.value = 0

    def draw(self, screen):
        """Draw tiles on the passed screen surface.
        
        Args:
            screen (pygame.Surface): Surface to draw
        """
        pygame.draw.rect(screen, COLORS[self.value], self.cords)

        font_cords = (
            self.cords[0] + Tile._tile_size//2, 
            self.cords[1] + Tile._tile_size//2
        )
        font_text = str(self.value)

        render_text(screen, font_text, font_cords)

    def set_pos(self, fullscreen=False, width=0, height=0):
        """Setup and update tiles position
        
        Args:
            fullscreen (bool, optional, default=False): Is fullscreen
            width (int, optional, default=0): Surface width
            height (int, optional, default=0): Surface height
        """
        window_size = (width, height) if width and height else \
            MONITOR_RESOLUTION if fullscreen else RESOLUTION
        # Formula to get size of one tile
        shorter_edge = window_size[0] if window_size[0] <= window_size[1] \
            else window_size[1]
        Tile._tile_size = shorter_edge * 0.82 / BOARD_SIZE
        # Formula to get size of space between tiles
        tile_space = shorter_edge * 0.03 / BOARD_SIZE
        # Formula to get cordinates of first tile
        start_x = int(window_size[0] / 2 - (BOARD_SIZE / 2 * Tile._tile_size))
        start_y = int(window_size[1] / 2 - (BOARD_SIZE / 2 * Tile._tile_size))
        # Update X's and Y's
        self.x1 = start_x + (tile_space + Tile._tile_size) * \
            (self.id % BOARD_SIZE)
        self.y1 = start_y + (tile_space + Tile._tile_size) * \
            (self.id // BOARD_SIZE)
        # Cordinates of beggining and end
        self.cords = (self.x1, self.y1, Tile._tile_size, Tile._tile_size)

    def __repr__(self):
        '''Print value of the tile
        
        Returns:
            string: value of the tile
        '''
        return str(self.value)

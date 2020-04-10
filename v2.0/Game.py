import pygame
import time
from Tile import Tile
from global_const import WIDTH, HEIGHT, BOARD_SIZE, ORIGINAL_WIDTH, ORIGINAL_HEIGHT, MONITOR_WIDTH, MONITOR_HEIGHT

FPS = 60
COLORS = {
    'BACKGROUND': (199, 183, 171),
}
RESIZABLE_FLAGS = pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF
FULLSCREEN_FLAGS = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF


class Game:
    def __init__(self):
        self.play = True
        self.fullscreen = False
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT], RESIZABLE_FLAGS)

        self.board = [[Tile() for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def run(self):
        """Main game loop"""
        while self.play:
            self.catch_events()
            self.draw()
            self.update()

    def catch_events(self):
        """Catch key events"""
        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                self.play = False

            # Video resize
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.dict['size']
                # Update all tiles position
                self.update_tiles_position()

            elif event.type == pygame.KEYDOWN:
                # Recognize keys
                pressed = pygame.key.get_pressed()
                alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]

                # When F pressed
                if event.key == pygame.K_f:
                    self.fullscreen = not self.fullscreen
                    # Set fullscreen
                    if self.fullscreen:
                        WIDTH, HEIGHT = MONITOR_WIDTH, MONITOR_HEIGHT
                        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN_FLAGS)
                    # Set Windowed
                    else:
                        WIDTH, HEIGHT = ORIGINAL_WIDTH, ORIGINAL_HEIGHT
                        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE_FLAGS)
                    # Update all tiles position
                    self.update_tiles_position()

                # Quit
                if event.key == pygame.K_F4 and alt_held:
                    self.play = False

    def draw(self):
        """Draws surface"""
        pygame.draw.rect(self.screen, COLORS['BACKGROUND'], (0, 0, WIDTH, HEIGHT))
        # Draw tiles
        [[col.draw(self.screen) for col in row] for row in self.board]

    def update_tiles_position(self):
        """Update all tils position"""
        [[col.set_pos() for col in row] for row in self.board]

    def clear_board(self):
        """Clear board"""
        self.board *= 0

    def update(self):
        pygame.display.update()
        self.clock.tick(FPS)

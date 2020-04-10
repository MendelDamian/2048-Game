import pygame
from Tile import Tile
from global_const import RESOLUTION, MONITOR_RESOLUTION, BOARD_SIZE

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
        self.screen = pygame.display.set_mode(RESOLUTION, RESIZABLE_FLAGS)

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
            if event.type == pygame.VIDEORESIZE:
                if not self.fullscreen:
                    self.screen = pygame.display.set_mode((event.w, event.h), RESIZABLE_FLAGS)
                    self.update_tiles_position(width=event.w, height=event.h)

            if event.type == pygame.KEYDOWN:
                # Check if alt is pressed
                pressed = pygame.key.get_pressed()
                alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
                # Quit on alt + F4
                if event.key == pygame.K_F4 and alt_held:
                    self.play = False

                # Fullscreen toggle
                if event.key == pygame.K_f:
                    self.fullscreen = not self.fullscreen
                    if self.fullscreen:
                        self.screen = pygame.display.set_mode(MONITOR_RESOLUTION, FULLSCREEN_FLAGS)
                    else:
                        self.screen = pygame.display.set_mode(RESOLUTION, RESIZABLE_FLAGS)
                    self.update_tiles_position()

    def draw(self):
        """Draws surface"""
        self.screen.fill(COLORS['BACKGROUND'])
        # Draw tiles
        [[col.draw(self.screen) for col in row] for row in self.board]

    def update_tiles_position(self, width=0, height=0):
        """Update tiles position
        
        Args:
            width (int, optional, default=0): Surface width
            height (int, optional, default=0): Surface height
        """
        [[col.set_pos(self.fullscreen, width, height) for col in row] for row in self.board]

    def clear_board(self):
        """Clear board"""
        self.board *= 0

    def update(self, *args, **kwargs):
        """Code which update screen"""
        pygame.display.update(*args, **kwargs)
        self.clock.tick(FPS)

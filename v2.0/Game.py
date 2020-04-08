import pygame
import time
from Tile import Tile
from global_const import *


class Game:
    def __init__(self):
        self.play = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()

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
            if event.type == pygame.QUIT:
                self.play = False

    def draw(self):
        """Draws surface"""
        self.screen.fill(COLORS['BACKGROUND'])
        # Draw tiles
        [[col.draw(self.screen) for col in row] for row in self.board]

    def clear_board(self):
        """Clear board"""
        self.board *= 0

    def update(self):
        pygame.display.update()
        self.clock.tick(FPS)

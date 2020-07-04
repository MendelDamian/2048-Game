import pygame
import numpy as np
import random
from Tile import Tile
from global_const import *

RESIZABLE_FLAGS = pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF
FULLSCREEN_FLAGS = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF


class Game:
    def __init__(self):
        self.play = True
        self.fullscreen = False
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(RESOLUTION, RESIZABLE_FLAGS)

        self.tiles_background = [[Tile() for _ in range(BOARD_SIZE)] 
                                 for _ in range(BOARD_SIZE)]
        self.board = np.array([[Tile() for _ in range(BOARD_SIZE)] 
                               for _ in range(BOARD_SIZE)])
        self.board_random(2)

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
                    new_width = event.w if event.w >= MIN_WIDTH else \
                        MIN_WIDTH
                    new_height = event.h if event.h >= MIN_HEIGHT else \
                        MIN_HEIGHT
                    self.screen = pygame.display.set_mode(
                        (new_width, new_height), 
                        RESIZABLE_FLAGS)
                    self.update_tiles_position(
                        width=new_width, 
                        height=new_height)

            # KeyDown events
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
                        self.screen = pygame.display.set_mode(
                            MONITOR_RESOLUTION, 
                            FULLSCREEN_FLAGS)
                    else:
                        self.screen = pygame.display.set_mode(
                            RESOLUTION, 
                            RESIZABLE_FLAGS)
                    self.update_tiles_position()

                # Move event
                if event.key in [pygame.K_UP, pygame.K_DOWN, 
                                 pygame.K_LEFT, pygame.K_RIGHT]:
                    self.move(event.key)
                    self.board_random()

    def move(self, direction):
        '''Movement
        
        Args:
            direction (pygame.KEY): Pressed key (K_UP, K_DOWN, K_LEFT, K_RIGHT)
        '''
        if direction in (pygame.K_UP, pygame.K_DOWN):
            self.board = self.board.T
        if direction in (pygame.K_RIGHT, pygame.K_DOWN):
            self.board = self.board[:,::-1]

        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE - 1):
                for k in range(j + 1, BOARD_SIZE):
                    if self.board[i][k].value == 0:
                        continue
                    if self.board[i][j].value == 0 or \
                       self.board[i][j].value == self.board[i][k].value:
                        self.board[i][j].value += self.board[i][k].value
                        self.board[i][k].value = 0

        if direction in (pygame.K_RIGHT, pygame.K_DOWN):
            self.board = self.board[:,::-1]
        if direction in (pygame.K_UP, pygame.K_DOWN):
            self.board = self.board.T

    def draw(self):
        """Draws surface"""
        self.screen.fill(COLORS['BACKGROUND'])
        # Draw tiles
        [[col.draw(self.screen) for col in row] 
         for row in self.board]

    def update_tiles_position(self, width=0, height=0):
        """Update tiles position
        
        Args:
            width (int, optional, default=0): Surface width
            height (int, optional, default=0): Surface height
        """
        [[col.set_pos(self.fullscreen, width, height) for col in row] 
         for row in self.board]

    def board_random(self, amount=1):
        '''Put value '2' in random place in self.board
        
        Args:
            amount (int, optional): amount of values to place
        
        Returns:
            bool: return true if success else false
        '''
        for _ in range(amount):
            if self.check_if_lose():
                self.play = False
                return False
            while True:
                row = random.randint(0, BOARD_SIZE - 1)
                col = random.randint(0, BOARD_SIZE - 1)
                if self.board[row][col].value != 0:
                    continue
                self.board[row][col].value = 2
                break
            return True

    def check_if_lose(self):
        """Checks if a board is full
        
        Returns:
            BOOL: Return True if board is full else False
        """
        for row in self.board:
            for col in row:
                if not col.value:
                    return False
        return True

    def update(self):
        """Code which update screen"""
        pygame.display.flip()
        self.clock.tick(FPS)

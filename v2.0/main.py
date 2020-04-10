import pygame
import os
import sys
from Game import Game
from global_const import WIDTH, HEIGHT, MONITOR_WIDTH, MONITOR_HEIGHT

CAPTION = '2048 Game'


def main():
    os.environ["SDL_VIDEO_CENTERED"] = "True"

    pygame.init()
    # Get user's monitor resolution
    MONITOR_WIDTH = pygame.display.Info().current_w
    MONITOR_HEIGHT = pygame.display.Info().current_h
    # Setup window
    pygame.display.set_caption(CAPTION)

    game = Game()
    game.run()


if __name__ == '__main__':
    main()
    
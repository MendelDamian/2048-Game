import pygame
import os
import sys
from Game import Game
from global_const import RESOLUTION, MONITOR_RESOLUTION

CAPTION = '2048 Game'


def main():
    # Center window when show up
    # os.environ["SDL_VIDEO_CENTERED"] = "True"
    pygame.init()
    # Get user's monitor resolution
    MONITOR_RESOLUTION = (pygame.display.Info().current_w, pygame.display.Info().current_h)

    # Setup window
    pygame.display.set_caption(CAPTION)

    game = Game()
    game.run()


if __name__ == '__main__':
    main()
    
import pygame
import os
import sys
from Game import Game
from global_const import *
# TODO: Always have the 4:3 ratio
# TODO: Score

def main():
    # Center window when show up
    # os.environ["SDL_VIDEO_CENTERED"] = "True"
    pygame.init()
    pygame.font.init()
    # Get user's monitor resolution
    MONITOR_RESOLUTION = (
        pygame.display.Info().current_w, 
        pygame.display.Info().current_h
    )
    # Setup window
    pygame.display.set_caption(CAPTION)

    # Game loop
    Game().run()

    # Exit
    pygame.quit()
    pygame.font.quit()
    sys.exit()


if __name__ == '__main__':
    main()
    
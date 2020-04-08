import pygame
import os
import sys
from Game import Game
from global_const import *


def main():
    os.environ["SDL_VIDEO_CENTERED"] = "True"

    pygame.init()
    pygame.display.set_caption(CAPTION)
    pygame.display.set_mode([WIDTH, HEIGHT])

    game = Game()
    game.run()


if __name__ == '__main__':
    main()
    
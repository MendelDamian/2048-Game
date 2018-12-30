import pygame


class Screen:

    def __init__(self):

        pygame.init()
        self.screen_width = 800
        self.screen_height = self.screen_width
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("2048 Game!")
        self.clock = pygame.time.Clock()

    def quit(self):
        pygame.quit()
        quit()

    def event_catcher(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            print(pygame.mouse.get_pos())

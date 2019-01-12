import pygame


class Screen:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = self.screen_width
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("2048 Game!")
        self.screen.fill((189, 173, 161))
        self.clock = pygame.time.Clock()

    def quit(self):
        pygame.quit()
        quit()

    def event_catcher(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return "up"

            # print(pygame.mouse.get_pos())

    def message_display(self, text, x, y, font_size, color):
        font = pygame.font.SysFont('arial', font_size)
        text_surf, text_rect = self.text_objects(text, font, color)
        text_rect.center = (x, y)
        self.screen.blit(text_surf, text_rect)

    def text_objects(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

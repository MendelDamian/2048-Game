import pygame


class Screen:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = self.screen_width
        self.background_color = (189, 173, 161)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("2048 Game!")
        self.screen.fill(self.background_color)
        self.clock = pygame.time.Clock()

    def quit(self):
        pygame.quit()
        quit()

    def event_catcher(self):
        self.screen.fill(self.background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return "up"
                elif event.key == pygame.K_LEFT:
                    return "left"
                elif event.key == pygame.K_RIGHT:
                    return "right"
                elif event.key == pygame.K_DOWN:
                    return "down"

            # print(pygame.mouse.get_pos())

    def message_display(self, text, x, y, font_size, color):
        font = pygame.font.SysFont('arial', font_size)
        text_surf, text_rect = self.text_objects(text, font, color)
        text_rect.center = (x, y)
        self.screen.blit(text_surf, text_rect)

    def text_objects(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

import pygame
from Button import Button


class Screen:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = self.screen_width
        self.fps = 60
        pygame.display.set_caption("2048 Game!")
        self.background_color = (189, 173, 161)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.game = False

        self.main_menu()

        self.up_key = pygame.K_UP
        self.left_key = pygame.K_LEFT
        self.right_key = pygame.K_RIGHT
        self.down_key = pygame.K_DOWN

    def quit(self):
        pygame.quit()
        quit()

    def event_catcher(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if self.game:
                    if event.key == self.up_key:
                        return "up"
                    elif event.key == self.left_key:
                        return "left"
                    elif event.key == self.right_key:
                        return "right"
                    elif event.key == self.down_key:
                        return "down"

    def message_display(self, text, x, y, font_size, color, font="verdana"):
        font = pygame.font.SysFont(font, font_size)
        text_surf, text_rect = self.text_objects(text, font, color)
        text_rect.center = (x, y)
        self.screen.blit(text_surf, text_rect)

    def text_objects(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def main_menu(self):
        play = Button(x=0.5*self.screen_width, y=0.5 * self.screen_height,
                      width=0.35*self.screen_width, height=0.1*self.screen_height,
                      color=(20, 163, 39))

        settings = Button(x=0.5*self.screen_width, y=0.5 * self.screen_height+play.height+10,
                          width=0.35*self.screen_width, height=0.1*self.screen_height,
                          color=(90, 186, 199))

        exitb = Button(x=0.5*self.screen_width, y=0.5 * self.screen_height+play.height+settings.height+20,
                       width=0.35*self.screen_width, height=0.1*self.screen_height,
                       color=(204, 13, 0))

        while not self.game:
            self.screen.fill(self.background_color)
            self.event_catcher()

            self.message_display("2048", 0.5 * self.screen_width, 0.20 * self.screen_height,
                                 160, (242, 82, 31), "verdana")

            # PLAY BUTTON
            pygame.draw.rect(self.screen, play.color, [play.x, play.y, play.width, play.height])
            self.message_display("PLAY", play.x+0.5*play.width, play.y+0.475*play.height,
                                 50, (0, 0, 0), "DejaVu Sans Mono")
            if play.check(pygame.mouse.get_pos()):
                self.game = True

            # SETTINGS BUTTON
            pygame.draw.rect(self.screen, settings.color, [settings.x, settings.y, settings.width, settings.height])
            self.message_display("SETTINGS", settings.x+0.5*play.width, settings.y+0.475*settings.height,
                                 50, (0, 0, 0), "DejaVu Sans Mono")
            settings.check(pygame.mouse.get_pos())

            # EXIT BUTTON
            pygame.draw.rect(self.screen, exitb.color, [exitb.x, exitb.y, exitb.width, exitb.height])
            self.message_display("EXIT", exitb.x+0.5*settings.width, exitb.y+0.475*exitb.height,
                                 50, (0, 0, 0), "DejaVu Sans Mono")
            if exitb.check(pygame.mouse.get_pos()):
                self.quit()

            self.clock.tick(self.fps)
            pygame.display.update()

import pygame
import os
from Button import Button
from xml.etree import ElementTree
from Square import Square
from random import randint


class Screen:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = self.screen_width
        self.size = 4
        self.width = (self.screen_width-40-10*(2*self.size-1))/self.size
        self.tiles = []
        self.theme = "Default"
        Square.add_theme(self.theme)
        for i in range(self.size):
            for j in range(self.size):
                x1 = j*20+20
                y1 = i*20+20
                self.tiles.append(Square(x1=x1+j*self.width, y1=y1+i*self.width,
                                         x2=self.width, y2=self.width))
        self.fps = 60
        self.lang = "pl-PL"
        pygame.display.set_caption("2048 Game!")
        self.background_color = (189, 173, 161)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.game = False
        self.settings_menu = False
        self.up_key = pygame.K_UP
        self.left_key = pygame.K_LEFT
        self.right_key = pygame.K_RIGHT
        self.down_key = pygame.K_DOWN
        self.main_menu()
        self.play()

    def event_catcher(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.game:
                        self.game = False
                    elif self.settings_menu:
                        self.settings_menu = False
                    elif not self.game:
                        Screen.quit()
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

    def check_lose(self):
        points = 0
        for k in range(self.size*self.size):
            if self.tiles[k].value == 0:
                points += 1
                break
        if not points:
            Screen.quit()

    def move(self, direction):
        if direction == "up":
            for k in range(self.size*self.size):
                for l in range(1, k // self.size+1):
                    if self.tiles[k-self.size*l].value == 0 or \
                       self.tiles[k-self.size*l].value == self.tiles[k-self.size*(l-1)].value:
                        self.tiles[k-self.size*l].value += self.tiles[k-self.size*(l-1)].value
                        self.tiles[k-self.size*(l-1)].value = 0

        elif direction == "left":
            for k in range(self.size*self.size):
                for l in range(1, k % self.size+1):
                    if self.tiles[k-l].value == 0 or \
                       self.tiles[k-l].value == self.tiles[k-(l-1)].value:
                        self.tiles[k-l].value += self.tiles[k-(l-1)].value
                        self.tiles[k-(l-1)].value = 0

        elif direction == "right":
            for k in range(self.size*self.size-1, -1, -1):
                for l in range(1, self.size - k % self.size):
                    if self.tiles[k+l-1].value == self.tiles[k+l].value or \
                       self.tiles[k+l].value == 0:
                        self.tiles[k+l].value += self.tiles[k+l-1].value
                        self.tiles[k+l-1].value = 0

        elif direction == "down":
            for k in range(self.size*self.size-1, -1, -1):
                for l in range(1, self.size-k//self.size):
                    if self.tiles[k+(l-1)*self.size].value == self.tiles[k+l*self.size].value or \
                       self.tiles[k+l*self.size].value == 0:
                        self.tiles[k+l*self.size].value += self.tiles[k+(l-1)*self.size].value
                        self.tiles[k+(l-1)*self.size].value = 0

        self.random_field()

    def random_field(self):
        self.check_lose()
        field = randint(0, self.size*self.size-1)
        while True:
            if not self.tiles[field].value:
                self.tiles[field].value = 2
                break
            else:
                field = randint(0, self.size*self.size-1)

    def req_word(self, requested_word):
        path = os.path.abspath(os.path.join("lang", "{}.xml".format(self.lang)))
        for word in ElementTree.parse(path).findall(self.lang):
            return word.find(requested_word).text

    def main_menu(self):
        play = Button(x=0.5*self.screen_width, y=0.5 * self.screen_height,
                      width=0.5*self.screen_width, height=0.1*self.screen_height,
                      color=(20, 163, 39), text="play")

        settings = Button(x=0.5*self.screen_width, y=0.5 * self.screen_height+play.height+10,
                          width=0.5*self.screen_width, height=0.1*self.screen_height,
                          color=(90, 186, 199), text="settings")

        exitb = Button(x=0.5*self.screen_width, y=0.5 * self.screen_height+play.height+settings.height+20,
                       width=0.5*self.screen_width, height=0.1*self.screen_height,
                       color=(204, 13, 0), text="exit")

        while not self.game:
            self.screen.fill(self.background_color)
            self.event_catcher()

            # LOGO
            self.message_display("2048", 0.5 * self.screen_width, 0.2 * self.screen_height,
                                 200, (242, 82, 31), "Clear Sans Bold")

            # PLAY BUTTON
            pygame.draw.rect(self.screen, play.color, [play.x, play.y, play.width, play.height])
            self.message_display(self.req_word(play.text), play.x+0.5*play.width,
                                 play.y+0.475*play.height, 50, (0, 0, 0), "DejaVu Sans Mono")
            if play.check(pygame.mouse.get_pos()):
                self.game = True

            # SETTINGS BUTTON
            pygame.draw.rect(self.screen, settings.color, [settings.x, settings.y, settings.width, settings.height])
            self.message_display(self.req_word(settings.text), settings.x+0.5*play.width,
                                 settings.y+0.475*settings.height, 50, (0, 0, 0), "DejaVu Sans Mono")
            if settings.check(pygame.mouse.get_pos()):
                self.settings_menu = True
                self.settings()

            # EXIT BUTTON
            pygame.draw.rect(self.screen, exitb.color, [exitb.x, exitb.y, exitb.width, exitb.height])
            self.message_display(self.req_word(exitb.text), exitb.x+0.5*settings.width,
                                 exitb.y+0.475*exitb.height, 50, (0, 0, 0), "DejaVu Sans Mono")
            if exitb.check(pygame.mouse.get_pos()):
                Screen.quit()

            self.clock.tick(self.fps)
            pygame.display.update()

    def settings(self):
        while self.settings_menu:
            self.screen.fill(self.background_color)
            self.event_catcher()

            self.message_display(self.req_word("settings"), 0.5 * self.screen_width, 0.07 * self.screen_height,
                                 100, (242, 82, 31), "Clear Sans Bold")

            self.clock.tick(self.fps)
            pygame.display.update()

    def play(self):
        self.reset()
        self.random_field()
        while self.game:
            direction = self.event_catcher()
            self.screen.fill(self.background_color)
            if direction:
                self.move(direction)

            for i in range(self.size*self.size):
                self.tiles[i].update_color()
                pygame.draw.rect(self.screen, self.tiles[i].color, [self.tiles[i].x1, self.tiles[i].y1,
                                                                    self.tiles[i].x2, self.tiles[i].y2])
                if self.tiles[i].value:
                    self.message_display(text=str(self.tiles[i].value), x=(2*self.tiles[i].x1+self.tiles[i].x2)/2,
                                         y=(2*self.tiles[i].y1+self.tiles[i].y2)/2, font_size=100,
                                         color=self.tiles[i].font_color, font="Clear Sans Bold")

            self.clock.tick(self.fps)
            pygame.display.update()

        self.main_menu()

    def reset(self):
        for i in range(self.size*self.size):
            self.tiles[i].value = 0

    @classmethod
    def quit(cls):
        pygame.quit()
        quit()

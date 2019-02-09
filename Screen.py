import pygame
from os import listdir, path, system, name
from Button import Button
from Square import Square
from Stack import Stack
from random import randint
from xml.etree import ElementTree
from time import sleep
from os.path import isfile


class Screen:

    def __init__(self):

        self.size_default = 4
        self.theme_default = "Default"
        self.lang_default = "en-GB"

        self.size = 4
        self.theme = "Default"
        self.lang = "en-GB"

        self.langs = []
        self.nof = 0
        for num, img in enumerate(listdir("images\\flags")):
            self.langs.append(img[:5])
            self.nof = num

        Square.add_theme(self.theme)

        self.settings()

        pygame.init()
        self.screen_width = 800
        self.screen_height = round(self.screen_width * 1.065)
        self.icon = pygame.image.load("images\\icon.png")
        pygame.display.set_icon(self.icon)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.fps = 60
        self.flags_img = []
        for num, img in enumerate(listdir("images\\flags")):
            self.flags_img.append(pygame.image.load("images\\flags\\" + img).convert())
            self.flags_img[num] = pygame.transform.scale(self.flags_img[num], (16, 10))

        pygame.display.set_caption("2048 Game!")
        self.background_color = (189, 173, 161)
        self.clock = pygame.time.Clock()
        self.game = False
        self.langb = []
        for i in range(len(self.langs)+1):
            self.langb.append(Button(x=self.screen_width-55, y=11+16*i, width=100, height=17,
                                     color=self.background_color, text="", change=0))

        self.main_menu()

        self.up_key = pygame.K_UP
        self.left_key = pygame.K_LEFT
        self.right_key = pygame.K_RIGHT
        self.down_key = pygame.K_DOWN
        self.backspace_key = pygame.K_BACKSPACE
        self.width = (self.screen_width-40-10*(2*self.size-1))/self.size
        self.tiles = []
        self.score = 0
        self.best = 0
        self.pause_menu = False

        for i in range(self.size):
            for j in range(self.size):
                x1 = j*20+20
                y1 = i*20+20
                self.tiles.append(Square(x1=x1+j*self.width, y1=y1+i*self.width+self.screen_height-self.screen_width,
                                         x2=self.width, y2=self.width))
        self.size_of_stack = 3
        self.stack = Stack(self.size_of_stack * self.size * self.size)
        self.score_stack = Stack(self.size_of_stack)
        self.best_score_stack = Stack(self.size_of_stack)

        self.play()

    def event_catcher(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not self.game:
                        Screen.quit()
                    elif self.pause_menu:
                        self.pause_menu = False
                    elif self.game:
                        self.pause_menu = True
                        self.pause()

                elif self.game:
                    if event.key == self.up_key:
                        return "up"
                    elif event.key == self.left_key:
                        return "left"
                    elif event.key == self.right_key:
                        return "right"
                    elif event.key == self.down_key:
                        return "down"
                    elif event.key == self.backspace_key:
                        return "back"

    def message_display(self, text, x, y, font_size, color=(0, 0, 0), font="verdana", pos="center"):
        font = pygame.font.SysFont(font, font_size)
        text_surf, text_rect = Screen.text_objects(text, font, color)
        text_rect.center = (x, y)
        if pos == "left":
            text_rect.left = x
        elif pos == "right":
            text_rect.right = x
        self.screen.blit(text_surf, text_rect)

    def check_lose(self):
        points = 0
        for k in range(self.size*self.size):
            if self.tiles[k].value == 0:
                points += 1
                break
        if not points:
            Screen.quit()

    def move(self, direction):
        if direction != "back":
            for tile in self.tiles:
                self.stack.push(tile.value)
            self.score_stack.push(self.score)
            self.best_score_stack.push(self.best)

        if direction == "up":
            for k in range(self.size*self.size):
                for l in range(1, k // self.size+1):
                    if self.tiles[k-self.size*l].value == 0 or \
                       self.tiles[k-self.size*l].value == self.tiles[k-self.size*(l-1)].value:
                        if self.tiles[k-self.size*l].value != 0 and self.tiles[k-self.size*(l-1)].value != 0:
                            self.score += self.tiles[k-self.size*l].value + self.tiles[k-self.size*(l-1)].value
                        self.tiles[k-self.size*l].value += self.tiles[k-self.size*(l-1)].value
                        self.tiles[k-self.size*(l-1)].value = 0

        elif direction == "left":
            for k in range(self.size*self.size):
                for l in range(1, k % self.size+1):
                    if self.tiles[k-l].value == 0 or \
                       self.tiles[k-l].value == self.tiles[k-(l-1)].value:
                        if self.tiles[k-l].value != 0 and self.tiles[k-l].value != 0:
                            self.score += self.tiles[k-l].value + self.tiles[k-(l-1)].value
                        self.tiles[k-l].value += self.tiles[k-(l-1)].value
                        self.tiles[k-(l-1)].value = 0

        elif direction == "right":
            for k in range(self.size*self.size-1, -1, -1):
                for l in range(1, self.size - k % self.size):
                    if self.tiles[k+l-1].value == self.tiles[k+l].value or \
                       self.tiles[k+l].value == 0:
                        if self.tiles[k+l-1].value != 0 and self.tiles[k+l].value != 0:
                            self.score += self.tiles[k+l].value + self.tiles[k+l-1].value
                        self.tiles[k+l].value += self.tiles[k+l-1].value
                        self.tiles[k+l-1].value = 0

        elif direction == "down":
            for k in range(self.size*self.size-1, -1, -1):
                for l in range(1, self.size-k//self.size):
                    if self.tiles[k+(l-1)*self.size].value == self.tiles[k+l*self.size].value or \
                       self.tiles[k+l*self.size].value == 0:
                        if self.tiles[k+(l-1)*self.size].value != 0 and self.tiles[k+l*self.size].value != 0:
                            self.score += self.tiles[k+l*self.size].value + self.tiles[k+(l-1)*self.size].value
                        self.tiles[k+l*self.size].value += self.tiles[k+(l-1)*self.size].value
                        self.tiles[k+(l-1)*self.size].value = 0

        elif direction == "back" and not self.stack.empty():
            for i in range(self.size * self.size, 0, -1):
                self.tiles[i-1].value = self.stack.top()
                self.stack.pop()
            self.score = self.score_stack.top()
            self.score_stack.pop()
            self.best = self.best_score_stack.top()
            self.best_score_stack.pop()

    def random_field(self):
        self.check_lose()
        field = randint(0, self.size*self.size-1)
        while True:
            if not self.tiles[field].value:
                x = randint(0, 10)
                if not x:
                    self.tiles[field].value = 4
                else:
                    self.tiles[field].value = 2
                break
            else:
                field = randint(0, self.size*self.size-1)

    def main_menu(self):
        # PLAY BUTTON
        play = Button(x=0.5*self.screen_width, y=0.5 * self.screen_height,
                      width=0.5*self.screen_width, height=0.1*self.screen_height,
                      color=(20, 163, 39), text="play")

        # EXIT BUTTON
        exitb = Button(x=0.5*self.screen_width, y=0.5 * self.screen_height+play.height+10,
                       width=0.5*self.screen_width, height=0.1*self.screen_height,
                       color=(204, 13, 0), text="exit")

        # LANGUAGE BUTTONS
        langb = []
        for i in range(len(self.langs)+1):
            langb.append(Button(x=self.screen_width-55, y=11+16*i, width=100, height=17,
                                color=self.background_color, text="", change=0))

        while not self.game:
            self.screen.fill(self.background_color)
            self.event_catcher()

            # LOGO
            self.message_display("2048", 0.5 * self.screen_width, 0.2 * self.screen_height,
                                 200, (242, 82, 31), "Clear Sans Bold")

            # PLAY BUTTON
            pygame.draw.rect(self.screen, play.color, [play.x, play.y, play.width, play.height])
            self.message_display(Screen.req_word(play.text, self.lang), play.x+0.5*play.width,
                                 play.y+0.475*play.height, 50, (0, 0, 0), "DejaVu Sans Mono")
            if play.check(pygame.mouse.get_pos()):
                self.game = True

            # EXIT BUTTON
            pygame.draw.rect(self.screen, exitb.color, [exitb.x, exitb.y, exitb.width, exitb.height])
            self.message_display(Screen.req_word(exitb.text, self.lang), exitb.x+0.5*play.width,
                                 exitb.y+0.475*exitb.height, 50, (0, 0, 0), "DejaVu Sans Mono")
            if exitb.check(pygame.mouse.get_pos()):
                Screen.quit()

            self.show_languages()

            self.clock.tick(self.fps)
            pygame.display.update()

    def play(self):
        self.reset()
        self.random_field()

        while self.game:
            self.screen.fill(self.background_color)
            direction = self.event_catcher()
            if direction:
                self.move(direction)
                if direction != "back":
                    self.random_field()
                    if self.score > self.best:
                        self.best = self.score

            for i in range(self.size*self.size):
                self.tiles[i].update_color()
                pygame.draw.rect(self.screen, self.tiles[i].color, [self.tiles[i].x1, self.tiles[i].y1,
                                                                    self.tiles[i].x2, self.tiles[i].y2])
                if self.tiles[i].value:
                    self.message_display(text=str(self.tiles[i].value), x=(2*self.tiles[i].x1+self.tiles[i].x2)/2,
                                         y=(2*self.tiles[i].y1+self.tiles[i].y2)/2, font_size=100,
                                         color=self.tiles[i].font_color, font="Clear Sans Bold")

            # UNDO
            self.message_display(text=Screen.req_word("undo", self.lang)+": {}".format(self.stack.size()//len(self.tiles)),
                                 x=20, y=(self.screen_height-self.screen_width+10)/2, font_size=30,
                                 color=(69, 69, 69), pos="left")

            # SCORE
            self.message_display(text=Screen.req_word("score", self.lang)+": {}".format(self.score),
                                 x=self.screen_width*0.5, y=(self.screen_height-self.screen_width+10)/2, font_size=30,
                                 color=(69, 69, 69))

            # BEST SCORE
            self.message_display(text=Screen.req_word("best", self.lang)+": {}".format(self.best),
                                 x=self.screen_width-20, y=(self.screen_height-self.screen_width+10)/2, font_size=30,
                                 color=(69, 69, 69), pos="right")

            self.clock.tick(self.fps)
            pygame.display.update()

        self.main_menu()

    def pause(self):
        # Resume button
        resumeb = Button(x=0.5*self.screen_width, y=0.5 * self.screen_height,
                         width=0.5*self.screen_width, height=0.1*self.screen_height,
                         color=(20, 163, 39), text="resume")

        # Back to menu button
        endb = Button(x=0.5*self.screen_width, y=0.5 * self.screen_height+resumeb.height+10,
                      width=0.5*self.screen_width, height=0.1*self.screen_height,
                      color=(204, 13, 0), text="end")

        while self.pause_menu:
            self.screen.fill(self.background_color)
            self.event_catcher()

            # Pause logo
            self.message_display(Screen.req_word("pause", self.lang), 0.5 * self.screen_width,
                                 0.07 * self.screen_height, 100, (242, 82, 31), "Clear Sans Bold")

            # Resume Button
            pygame.draw.rect(self.screen, resumeb.color, [resumeb.x, resumeb.y, resumeb.width, resumeb.height])
            self.message_display(Screen.req_word(resumeb.text, self.lang), resumeb.x+0.5*resumeb.width,
                                 resumeb.y+0.475*resumeb.height, 50, (0, 0, 0), "DejaVu Sans Mono")
            if resumeb.check(pygame.mouse.get_pos()):
                self.pause_menu = False

            # Back to menu Button
            pygame.draw.rect(self.screen, endb.color, [endb.x, endb.y, endb.width, endb.height])
            self.message_display(Screen.req_word(endb.text, self.lang), endb.x+0.5*endb.width,
                                 endb.y+0.475*endb.height, 50, (0, 0, 0), "DejaVu Sans Mono")
            if endb.check(pygame.mouse.get_pos()):
                self.pause_menu = False
                self.game = False
                sleep(0.1)

            self.show_languages()

            self.clock.tick(self.fps)
            pygame.display.update()

    def settings(self):
        while True:
            Screen.cls()
            print("\nCurrent settings:\n")
            print(f"1) Size: {self.size}")
            print(f"2) Theme: {self.theme}")
            print(f"3) Language: {self.lang}")

            print("\nIf you want to change someting type digit of the option, if not - press Enter")
            print("Input:  ",end='')
            choice = input()

            if choice == "":
                break
            elif choice == "1":
                self.set_size()
            elif choice == "2":
                self.select_theme()
            elif choice == "3":
                self.set_lang()
            else:
                print("Wrong option")

    def set_size(self):
        Screen.cls()
        print("What size of game do you want? ")
        try:
            print("\nInput:  ", end='')
            self.size = int(input())
        except ValueError:
            print("It must be a value between 4 and 16")
            self.set_size()
        if self.size > 16 or self.size < 4:
            print("It must be a value between 4 and 16")
            self.set_size()

    def select_theme(self):
        Screen.cls()
        print("Which theme do you want to use?")
        for theme in listdir("Themes\\"):
            if theme[:-4] != "Example":
                print(theme[:-4])
        
        print("\nInput:  ", end='')
        self.theme = input()
        if not isfile("Themes\\{}.txt".format(self.theme)):
            print("Incorrect option!")
            self.select_theme()
        if self.theme == "Example":
            print("Incorrect option!")
            self.select_theme()

        Square.add_theme(self.theme)

    def set_lang(self):
        Screen.cls()
        print("Which language do you want to use? ")
        for index, item in enumerate(self.langs):
            print(f"{index}.", item)

        for i in range(10):
            try:
                print("\nInput:  ", end='')
                self.lang = int(input())
            except ValueError:
                print("Choice the number between 0-{}".format(self.nof))
                continue

            if self.lang > self.nof or self.lang < 0:
                print("Choice the number between 0-{}".format(self.nof))
                continue
            break

        else:
            print("Critical ERROR")
            Screen.quit()

        self.lang = self.langs[self.lang]

    def show_languages(self):
        # LANG BUTTON
        for i in range(len(self.langs)+1):
            pygame.draw.rect(self.screen, self.langb[i].color, [self.langb[i].x, self.langb[i].y, self.langb[i].width, self.langb[i].height])
            if self.langb[i].check(pygame.mouse.get_pos()) and i and self.langs[i-1] != self.lang:
                self.lang = Screen.req_word("short_name", self.langs[i-1])

        # Names of languages
        s = 0
        self.message_display(text=Screen.req_word("selected", self.lang) + ": " +
                             Screen.req_word("full_name", self.lang),
                             font_size=15, x=self.screen_width-25, y=10, pos="right")
        self.screen.blit(self.flags_img[self.find()], (self.screen_width-20, 5))
        for item in self.langs:
            self.message_display(text=Screen.req_word("full_name", item),
                                 font_size=15, x=self.screen_width-25, y=26+(16*s), pos="right")
            self.screen.blit(self.flags_img[s], (self.screen_width-20, 21+(16*s)))
            s += 1

    def reset(self):
        for i in range(self.size*self.size):
            self.tiles[i].value = 0
        self.score = 0
        while not self.stack.empty():
            self.stack.pop()

    def find(self):
        i = 0
        for element in self.langs:
            if element == self.lang:
                return i
            else:
                i += 1

    @classmethod
    def text_objects(cls, text, font, color):
        text_surface = 0
        try:
            text_surface = font.render(text, True, color)
        except AttributeError:
            print("ERROR at def text_surface")
            font = pygame.font.SysFont("Arial", 50)
            text_surface = font.render(text, True, color)
        finally:
            return text_surface, text_surface.get_rect()

    @classmethod
    def req_word(cls, requested_word, language):
        full_path = path.abspath(path.join("lang", "{}.xml".format(language)))
        for word in ElementTree.parse(full_path).findall(language):
            return word.find(requested_word).text

    @classmethod
    def quit(cls):
        pygame.quit()
        quit()

    @classmethod
    def cls(cls):
        system('cls' if name=='nt' else 'clear')

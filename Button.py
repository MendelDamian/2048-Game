import pygame


class Button:
    def __init__(self, x, y, width, height, color, text):
        self.x = x - 0.5*width
        self.y = y - 0.5*height
        self.width = width
        self.height = height
        self.text = text
        self.default_color = color
        self.color = color
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]

    def check(self, mouse_pos):
        m_x = mouse_pos[0]
        m_y = mouse_pos[1]

        if self.x+self.width > m_x > self.x and self.y+self.height > m_y > self.y:
            self.color = ((self.r+10) % 256, (self.g+10) % 256, (self.b+10) % 256)
            if pygame.mouse.get_pressed()[0]:
                return True
        else:
            self.color = self.default_color

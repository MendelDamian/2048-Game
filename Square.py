COLORS = {0: (206, 192, 181), 2: (255, 214, 182), 4: (246, 186, 198), 8: (165, 211, 182), 16: (243, 234, 129),
          32: (255, 175, 124), 64: (153, 181, 221), 128: (241, 136, 167), 256: (196, 132, 167), 512: (251, 117, 114),
          1024: (141, 91, 118)}


class Square:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2 + 10
        self.y2 = y2 + 10
        self.value = 0
        self.update_color()

    def update_color(self):
        self.color = COLORS[self.value]

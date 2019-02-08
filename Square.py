COLORS = []
light_color = (253, 250, 245)
dark_color = (134, 121, 115)


class Square:

    num_lines = 0
    max_value = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2 + 10
        self.y2 = y2 + 10
        self.value = 0
        self.r = 0
        self.g = 0
        self.b = 0
        self.color = 0
        self.font_color = 0
        self.update_color()

    def update_color(self):
        if self.value <= pow(2, Square.num_lines-1):
            self.r = int(COLORS[int(Square.sqrt(self.value))][str(self.value)][0])
            self.g = int(COLORS[int(Square.sqrt(self.value))][str(self.value)][1])
            self.b = int(COLORS[int(Square.sqrt(self.value))][str(self.value)][2])
        else:
            self.r = int(COLORS[Square.num_lines][str(Square.max_value)][0])
            self.g = int(COLORS[Square.num_lines][str(Square.max_value)][1])
            self.b = int(COLORS[Square.num_lines][str(Square.max_value)][2])

        self.color = int(self.r), int(self.g), int(self.b)

        if self.r + self.g + self.b > 600:
            self.font_color = dark_color
        else:
            self.font_color = light_color

    @classmethod
    def add_theme(cls, theme):
        with open("Themes\\{}.txt".format(theme), 'r') as file:
            cls.num_lines = sum(1 for x in file)-1
            cls.max_value = pow(2, cls.num_lines)
            file.seek(0)
            for line in file:
                elements = line.rstrip().split(" ")
                COLORS.append(dict(zip(elements[:1], list(zip(elements[1::], elements[2::], elements[3::])))))

        file.close()

    @classmethod
    def sqrt(cls, x):
        if not x:
            return 0
        i = 0    
        while x:
            i += 1
            x = x/2
            if x == 1:
                x = 0
        return i

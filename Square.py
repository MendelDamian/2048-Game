COLORS = []


def add_theme(theme):
    with open("Themes\\"+theme+".txt", 'r') as file:
        for line in file:
            elements = line.rstrip().split(" ")
            COLORS.append(dict(zip(elements[:1], list(zip(elements[1::], elements[2::], elements[3::])))))

    file.close()


def some(x):
    i = 0
    if not x:
        return 0
    while x:
        i += 1
        x = x/2
        if x == 1:
            x = 0
    return i


class Square:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2 + 10
        self.y2 = y2 + 10
        self.value = 0
        self.r = COLORS[int(some(self.value))][str(self.value)][0]
        self.g = COLORS[int(some(self.value))][str(self.value)][1]
        self.b = COLORS[int(some(self.value))][str(self.value)][2]
        self.color = int(self.r), int(self.g), int(self.b)
        self.font_color = (134, 121, 115)

    def update_color(self):
        self.r = COLORS[int(some(self.value))][str(self.value)][0]
        self.g = COLORS[int(some(self.value))][str(self.value)][1]
        self.b = COLORS[int(some(self.value))][str(self.value)][2]
        self.color = int(self.r), int(self.g), int(self.b)
        if self.value > 4:
            self.font_color = (253, 250, 245)
        else:
            self.font_color = (134, 121, 115)

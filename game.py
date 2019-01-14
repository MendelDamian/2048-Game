from Screen import Screen
from Square import Square
from Square import add_theme
from random import randint
import pygame

screen = Screen()
size = 4
add_theme(screen.theme)
width = (screen.screen_width-40-10*(2*size-1))/size
squares = []

for i in range(size):
    for j in range(size):
        x1 = j*20+20
        y1 = i*20+20
        squares.append(Square(x1=x1+j*width, y1=y1+i*width,
                              x2=width, y2=width))


def check_lose():
    points = 0
    for k in range(size*size):
        if squares[k].value == 0:
            points += 1
            break
    if not points:
        screen.quit()


def move(direction):
    if direction == "up":
        for k in range(size*size):
            for l in range(1, k // size+1):
                if squares[k-size*l].value == 0 or \
                   squares[k-size*l].value == squares[k-size*(l-1)].value:
                    squares[k-size*l].value += squares[k-size*(l-1)].value
                    squares[k-size*(l-1)].value = 0

    elif direction == "left":
        for k in range(size*size):
            for l in range(1, k % size+1):
                if squares[k-l].value == 0 or \
                   squares[k-l].value == squares[k-(l-1)].value:
                    squares[k-l].value += squares[k-(l-1)].value
                    squares[k-(l-1)].value = 0

    elif direction == "right":
        for k in range(size*size-1, -1, -1):
            for l in range(1, size - k % size):
                if squares[k+l-1].value == squares[k+l].value or \
                   squares[k+l].value == 0:
                    squares[k+l].value += squares[k+l-1].value
                    squares[k+l-1].value = 0

    elif direction == "down":
        for k in range(size*size-1, -1, -1):
            for l in range(1, size-k//size):
                if squares[k+(l-1)*size].value == squares[k+l*size].value or \
                   squares[k+l*size].value == 0:
                    squares[k+l*size].value += squares[k+(l-1)*size].value
                    squares[k+(l-1)*size].value = 0

    random_field()


def random_field():
    check_lose()
    field = randint(0, size*size-1)
    while True:
        if not squares[field].value:
            squares[field].value = 2
            break
        else:
            field = randint(0, size*size-1)


def game():
    random_field()
    while screen.game:
        direction = screen.event_catcher()
        screen.screen.fill(screen.background_color)
        if direction:
            move(direction)

        for i in range(size*size):
            squares[i].update_color()
            pygame.draw.rect(screen.screen, squares[i].color, [squares[i].x1, squares[i].y1,
                                                               squares[i].x2, squares[i].y2])
            if squares[i].value:
                screen.message_display(text=str(squares[i].value), x=(2*squares[i].x1+squares[i].x2)/2,
                                       y=(2*squares[i].y1+squares[i].y2)/2, font_size=100,
                                       color=squares[i].font_color, font="Clear Sans Bold")

        screen.clock.tick(screen.fps)
        pygame.display.update()

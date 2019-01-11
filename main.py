from Screen import Screen
from Square import Square
from random import randint
import pygame

screen = Screen()
size = 4
width = (screen.screen_width-40-10*(2*size-1))/size
squares = []
game = [size*size]

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


def random_field():
    field = randint(0, 15)
    while True:
        if not squares[field].value:
            squares[field].value = 2
            break
        else:
            field = randint(0, 15)


random_field()
while True:
    check_lose()
    if screen.event_catcher():
        random_field()

    for i in range(size*size):
        pygame.draw.rect(screen.screen, squares[i].blank_color, [squares[i].x1, squares[i].y1,
                                                                 squares[i].x2, squares[i].y2])
        if squares[i].value != 0:
            screen.message_display(text=str(squares[i].value), x=(2*squares[i].x1+squares[i].x2)/2,
                                   y=(2*squares[i].y1+squares[i].y2)/2, font_size=50, color=(0, 0, 0))

    pygame.display.update()
    screen.clock.tick(60)

import Screen
import Square
import pygame

screen = Screen.Screen()
size = 4
width = (screen.screen_width-40-10*(2*size-1))/size
squares = []

for i in range(size):
    for j in range(size):
        x1 = j*20+20
        y1 = i*20+20
        squares.append(Square.Square(x1=x1+j*width, y1=y1+i*width,
                                     x2=width, y2=width))

while True:
    screen.event_catcher()
    for i in range(size*size):
        pygame.draw.rect(screen.screen, (200, 200, 100), [squares[i].x1, squares[i].y1,
                                                          squares[i].x2, squares[i].y2])

    pygame.display.update()
    screen.clock.tick(60)

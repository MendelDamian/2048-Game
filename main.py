import Screen
import Square
import pygame

screen = Screen.Screen()
size = 4
squares = []
for i in range(size):
    for j in range(size):
        x1 = j * 200
        y1 = i * 200
        squares.append(Square.Square(x1=x1, y1=y1, x2=x1 + 200, y2=y1 + 200))

while True:
    screen.event_catcher()
    for i in range(size*size):
        pygame.draw.rect(screen.screen, (i, i+50, i+100), [squares[i].x1, squares[i].y1,
                                                           squares[i].x2, squares[i].y2])
    pygame.display.update()
    screen.clock.tick(60)

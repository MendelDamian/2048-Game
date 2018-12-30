import Screen
import Square
import pygame

screen = Screen.Screen()
size = 2
squares =  []
w1 = screen.screen_width/2
squares.append(Square.Square(x1=20, y1=20, x2=365, y2=365)) #11
squares.append(Square.Square(x1=405, y1=20, x2=365, y2=365)) #12
squares.append(Square.Square(x1=20, y1=405, x2=365, y2=365)) #21
squares.append(Square.Square(x1=405, y1=405, x2=365, y2=365)) #22

while True:
    screen.event_catcher()
    for i in range(size*size):
        pygame.draw.rect(screen.screen, (i+75, i+50, i+100), [squares[i].x1, squares[i].y1,
                                                              squares[i].x2, squares[i].y2])

    pygame.display.update()
    screen.clock.tick(60)

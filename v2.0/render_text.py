import pygame


def render_text(screen, text, pos, color=(0, 0, 0), font_name='Comic Sans MS', font_size=30):
    '''Function to draw on a surface
    
    Args:
        screen (pygame.Surface): Surface to draw
        text (string): Text to draw
        pos (tuple): Position to draw (X, Y)
        color (tuple, optional): RGB value of font color
        font (str, optional): font name
        font_size (int, optional): font size
    '''
    font = pygame.font.SysFont(font_name, font_size)
    font = font.render(text, False, color)
    text_rect = font.get_rect(center=pos)
    screen.blit(font, text_rect)

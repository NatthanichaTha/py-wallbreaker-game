import pygame

def draw_rect_outline(screen, fill_color, x, y, width, height, outline_size=1, outline_color = (0,0,0)):
    pygame.draw.rect(screen, outline_color, pygame.Rect(x, y, width, height))
    pygame.draw.rect(screen, fill_color, pygame.Rect(x + outline_size, y + outline_size, width - (outline_size*2), height - (outline_size*2)))
import pygame


def draw_grid(screen, colour, number_of_divisions=3, gridlines_width=1):
    cell_height = screen.get_height // number_of_divisions
    cell_width = screen.get_width // number_of_divisions

    for vertical_position in range(0, screen.get_height, cell_height):
        for horizontal_position in range(0, screen.get_width, cell_width):
            rect = pygame.Rect(horizontal_position, vertical_position, cell_height,
                               cell_width)
            pygame.draw.rect(screen, colour, rect, gridlines_width)

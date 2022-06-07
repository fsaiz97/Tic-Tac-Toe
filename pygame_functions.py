import pygame


def draw_grid(screen, screen_height, screen_width, colour, number_of_divisions = 3):
    gridlines_width = 1

    for vertical_position in range(0, screen_height, screen_height // number_of_divisions):
        for horizontal_position in range(0, screen_width, screen_width // number_of_divisions):
            rect = pygame.Rect(horizontal_position, vertical_position, screen_height // number_of_divisions,
                               screen_width // number_of_divisions)
            pygame.draw.rect(screen, colour, rect, gridlines_width)

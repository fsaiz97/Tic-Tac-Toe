import pygame


def get_game_window_size():
    display_width = 600
    display_height = 600

    return display_width, display_height


def draw_grid(surface, colour, number_of_divisions=3, gridlines_width=1):
    cell_height = surface.get_height() // number_of_divisions
    cell_width = surface.get_width() // number_of_divisions

    for vertical_position in range(0, surface.get_height(), cell_height):
        for horizontal_position in range(0, surface.get_width(), cell_width):
            rect = pygame.Rect(horizontal_position, vertical_position, cell_height, cell_width)
            pygame.draw.rect(surface, colour, rect, gridlines_width)


def get_grid_pos(cell_width, cell_height, mouse_pos):

    return mouse_pos[0] // cell_width, mouse_pos[1] // cell_height

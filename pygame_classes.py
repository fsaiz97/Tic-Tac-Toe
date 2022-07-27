from typing import Tuple

import pygame

from pygame_functions import draw_grid

MouseClickStates = Tuple[bool, bool, bool]  # type for the tuple returned by pygame.mouse.get_pressed()


class GameWindow:
    """Window for displaying the game in, along with control mechanisms relating to the game."""

    def __init__(self, window_width, window_height, cell_width, cell_height):
        self.cell_width = cell_width
        self.cell_height = cell_height

        self.display_surface = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Tic-Tac-Toe")
        self.display_surface.fill(pygame.Color("White"))
        draw_grid(self.display_surface, pygame.Color("Black"))

    def get_width(self):
        return self.display_surface.get_width()

    def get_height(self):
        return self.display_surface.get_height()


class Button(pygame.sprite.Sprite):
    """Basic button class that activates when clicked"""

    def __init__(self, pixel_width, pixel_height, colour=pygame.Color("White")):
        super(Button, self).__init__()
        self.surface = pygame.Surface((pixel_width, pixel_height))
        self.surface.fill(colour)
        self.rect = self.surface.get_rect()

    def update(self, mouse_presses: MouseClickStates):
        pass

    def draw(self, screen, position):
        screen.blit(self.surface, position)


class Grid(pygame.sprite.Sprite):
    """Collects Button instances into a grid game-board"""

    def __init__(self, number_of_columns, number_of_rows, pixel_width, pixel_height):
        super(Grid, self).__init__()
        self.pixel_width = pixel_width
        self.pixel_height = pixel_height
        button_pixel_width = self.pixel_width // number_of_columns
        button_pixel_height = self.pixel_height // number_of_rows
        self.button_array = [[Button(button_pixel_width, button_pixel_height, pygame.Color("Red"))
                              for j in range(0, number_of_columns)] for i in range(0, number_of_rows)]
        self.surface = pygame.Surface((self.pixel_width, pixel_height))
        self.surface.fill(pygame.Color("White"))

        for row_index, vertical_position in enumerate(range(0, self.pixel_height, button_pixel_height)):
            for column_index, horizontal_position in enumerate(range(0, self.pixel_width, button_pixel_width)):
                self.button_array[row_index][column_index].draw(self.surface, (horizontal_position, vertical_position))
        self.rect = self.surface.get_rect()

    def draw_to_screen(self, screen, position):
        screen.blit(self.surface, position)


class TileSet:
    def __init__(self, file, tile_size, margin):
        self.margin = margin
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.size = tile_size
        self.tiles = []
        self.load_tiles()

    def load_tiles(self):
        for x in range(0, self.rect.width, self.size):
            tile = pygame.Surface((self.size, self.size))
            tile.blit(self.image, (0, 0), (x, 0, self.size, self.size))
            self.tiles.append(tile)

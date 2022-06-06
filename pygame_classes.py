from typing import Tuple

import pygame

MouseClickStates = Tuple[bool, bool, bool]  # type for the tuple returned by pygame.mouse.get_pressed()


class Button(pygame.sprite.Sprite):
    """Basic button class that activates when clicked"""

    def __init__(self, pixel_width, pixel_height, colour=pygame.Color("White")):
        super(Button, self).__init__()
        self.image = pygame.Surface((pixel_width, pixel_height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()

    def update(self, mouse_presses: MouseClickStates):
        pass

    def draw(self, screen, pos):
        screen.blit(self.image, pos)


class Grid(pygame.sprite.Sprite):
    """Collects Button instances into a grid game-board"""

    def __init__(self, number_of_rows, number_of_columns, pixel_height, pixel_width):
        super(Grid, self).__init__()
        self.pixel_width = pixel_width
        self.pixel_height = pixel_height
        button_pixel_width = self.pixel_width // number_of_columns
        button_pixel_height = self.pixel_height // number_of_rows
        self.button_array = [[Button(button_pixel_width, button_pixel_height, pygame.Color("Red"))
                              for j in range(0, number_of_columns)] for i in range(0, number_of_rows)]
        self.image = pygame.Surface((self.pixel_width, pixel_height))
        self.image.fill(pygame.Color("White"))

        for i, x in enumerate(range(0, self.pixel_height, button_pixel_height)):
            for j, y in enumerate(range(0, self.pixel_width, button_pixel_width)):
                self.button_array[i][j].draw(self.image, (x, y))
        self.rect = self.image.get_rect()

    def draw(self, screen, pos):
        screen.blit(self.image, pos)

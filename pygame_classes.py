from typing import Tuple

import pygame

MouseClickStates = Tuple[bool, bool, bool]  # type for the tuple returned by pygame.mouse.get_pressed()


class Button(pygame.sprite.Sprite):
    """Basic button class that activates when clicked"""

    def __init__(self, width, height, colour=pygame.Color("White")):
        super(Button, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()

    def update(self, mouse_presses: MouseClickStates):
        pass

    def draw(self, screen, pos):
        screen.blit(self.image, pos)


class Grid(pygame.sprite.Sprite):
    """Collects Button instances into a grid game-board"""

    def __init__(self, n_rows, n_columns, width, height):
        super(Grid, self).__init__()
        self.width = width
        self.height = height
        self.array = [[Button(width/n_columns, height/n_rows, pygame.Color("Black"))] for row in range(0, n_rows)]
        self.image = pygame.Surface((width, height))
        self.image.fill(pygame.Color("White"))
        for i, x in enumerate(range(0, self.height, self.height // n_rows)):
            for j, y in enumerate(range(0, self.width, self.width // n_columns)):
                self.array[i][j].draw(self.image, (x, y))
        self.rect = self.image.get_rect()

    def draw(self, screen, pos):
        screen.blit(self.image, pos)
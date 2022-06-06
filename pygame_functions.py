import pygame


def draw_grid(screen, screen_height, screen_width, colour):
    for x in range(0, screen_height, screen_height // 3):
        for y in range(0, screen_width, screen_width // 3):
            rect = pygame.Rect(x, y, screen_height // 3, screen_width // 3)
            pygame.draw.rect(screen, colour, rect, 1)

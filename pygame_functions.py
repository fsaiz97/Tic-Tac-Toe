import pygame


def draw_grid(screen, SCREEN_HEIGHT, SCREEN_WIDTH, colour):
    for x in range(0, SCREEN_HEIGHT, SCREEN_HEIGHT // 3):
        for y in range(0, SCREEN_WIDTH, SCREEN_WIDTH // 3):
            rect = pygame.Rect(x, y, SCREEN_HEIGHT // 3, SCREEN_WIDTH // 3)
            pygame.draw.rect(screen, colour, rect, 1)


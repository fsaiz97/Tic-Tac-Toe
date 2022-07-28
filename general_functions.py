import os

from pygame_classes import TileSet


def load_tiles():
    tileset_file_name = "tileset.png"
    tileset_file_path = os.path.join(os.path.dirname(__file__), tileset_file_name)
    tile_size = 34
    margin = 1
    return TileSet(tileset_file_path, tile_size, margin)


def get_graphics_choice():
    while True:
        graphics_choice = input("Do you want graphics? (Y/y, N/n)\n").lower()
        if graphics_choice not in ['y', 'n']:
            print("Invalid choice, Please try again.\n")
        elif graphics_choice == 'y':
            graphics_on = True
            break
        else:
            graphics_on = False
            break
    return graphics_on

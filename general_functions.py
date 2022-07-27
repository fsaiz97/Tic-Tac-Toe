import sys
import os

from pygame_classes import TileSet


def get_current_root_directory():
    if hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS
    else:
        return "."


def load_tiles():
    # number_of_divisions = 3
    # cell_width = display_width // number_of_divisions
    # cell_height = display_height // number_of_divisions
    # cell_dims = cell_width, cell_height
    tileset_file_name = "tileset.png"
    tileset_file_path = os.path.join(get_current_root_directory(), tileset_file_name)
    tile_size = 34
    margin = 1
    return TileSet(tileset_file_path, tile_size, margin)

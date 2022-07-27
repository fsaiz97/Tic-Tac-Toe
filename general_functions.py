import sys


def get_current_root_directory():
    if hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS
    else:
        return "."

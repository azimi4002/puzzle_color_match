from typing import List

from colors import Color
from tile import Tile

# List all wooden tiles to pass to board
MAIN_TILES: List[Tile] = [
    Tile(Color.YELLOW, Color.RED, Color.BLUE, Color.GREEN),
    Tile(Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE),
    Tile(Color.BLUE, Color.YELLOW, Color.GREEN, Color.RED),
    Tile(Color.GREEN, Color.BLUE, Color.RED, Color.YELLOW),
    Tile(Color.YELLOW, Color.BLUE, Color.RED, Color.GREEN),
    Tile(Color.RED, Color.YELLOW, Color.GREEN, Color.BLUE),
    Tile(Color.BLUE, Color.RED, Color.YELLOW, Color.GREEN),
    Tile(Color.GREEN, Color.YELLOW, Color.BLUE, Color.RED),
]


SINGLE_COLOR_TILES: List[Tile] = [
    Tile(Color.RED, Color.RED, Color.RED, Color.RED),
    Tile(Color.RED, Color.RED, Color.RED, Color.RED),
    Tile(Color.RED, Color.RED, Color.RED, Color.RED),
    Tile(Color.RED, Color.RED, Color.RED, Color.RED),
    Tile(Color.RED, Color.RED, Color.RED, Color.RED),
    Tile(Color.RED, Color.RED, Color.RED, Color.RED),
    Tile(Color.RED, Color.RED, Color.RED, Color.RED),
    Tile(Color.RED, Color.RED, Color.RED, Color.RED),
]

TWO_TILES: List[Tile] = [
    Tile(Color.RED, Color.BLUE, Color.RED, Color.BLUE),
    Tile(Color.BLUE, Color.RED, Color.BLUE, Color.RED),
]
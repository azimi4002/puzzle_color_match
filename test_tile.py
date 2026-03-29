import unittest
from typing import Dict, Tuple, List

from board import MAIN_POSITIONS
from colors import Color
from sample_tiles import MAIN_TILES, SINGLE_COLOR_TILES, TWO_TILES
from solver import solve, is_compatible
from tile import Tile

class TestTile(unittest.TestCase):
    def test_two_color_cross_rotations(self):
        tile = Tile(Color.RED, Color.GREEN, Color.RED, Color.GREEN)
        rotations = tile.rotations()
        assert len(rotations) == 2

    def test_two_color_rotations(self):
        tile = Tile(Color.RED, Color.GREEN, Color.GREEN, Color.GREEN)
        rotations = tile.rotations()
        assert len(rotations) == 4


if __name__ == "__main__":
    unittest.main()
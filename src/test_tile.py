import unittest

from colors import Color
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

import unittest
from typing import Dict, Tuple, List

from board import MAIN_POSITIONS
from sample_tiles import MAIN_TILES, SINGLE_COLOR_TILES, TWO_TILES
from solver import solve, is_compatible
from tile import Tile

# For test
TWO_TILES_BOARD_POSITIONS: List[Tuple[int, int]] = [
    (1, 0), (1, 1)
]

def validate_main_solution(solution: Dict[Tuple[int, int], Tile]) -> bool:
    """For validation of a solution checks all known adjacencies."""
    adjacencies = [
        ((0, 0), (1, 0)),
        ((1, 0), (2, 0)),
        ((1, 0), (1, 1)),
        ((1, 0), (1, -1)),
        ((1, -1), (2, -1)),
        ((2, 0), (2, -1)),
        ((2, -1), (2, -2)),
        ((2, -1), (3, -1)),
    ]

    for p1, p2 in adjacencies:
        if not is_compatible(p1, solution[p1], p2, solution[p2]):
            return False
    return True

class TestSolver(unittest.TestCase):
    def test_main_sample_valid(self):
        solutions = solve(MAIN_POSITIONS, MAIN_TILES, log=False)
        valid_count = 0
        for i, sol in enumerate(solutions):
            if validate_main_solution(sol):
                valid_count += 1
            else:
                print(f"Error: Solution {i + 1} not color matched")

        print(f"{valid_count}/{len(solutions)} solutions matched color.")

    def test_single_color_tiles(self):
        solutions = solve(MAIN_POSITIONS, SINGLE_COLOR_TILES, log=False)
        assert len(solutions) == 1

    def test_two_color_tiles_two_positions(self):
        solutions = solve(TWO_TILES_BOARD_POSITIONS, TWO_TILES, log=False)
        assert len(solutions) == 2

if __name__ == "__main__":
    unittest.main()
from typing import Dict, Tuple, List

from tile import Tile


def print_solution(
        solutions: List[Dict[Tuple[int, int], Tile]],
        positions: List[Tuple[int, int]],
        log: bool
) -> None:
    if not log:
        return

    print(f"Found {len(solutions)} solutions.")

    for idx, sol in enumerate(solutions, start=1):
        print(f"Solution {idx}:")
        parts = [f"({x}, {y}): {sol[(x, y)]}" for x, y in positions]
        print(", ".join(parts))

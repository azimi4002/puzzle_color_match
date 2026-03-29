from collections import Counter
from typing import Tuple, List, Dict

from printer import print_solution
from tile import Tile


def is_compatible(
        pos1: Tuple[int, int], sq1: Tile,
        pos2: Tuple[int, int], sq2: Tile
) -> bool:
    """Check if two adjacent squares' colours are match"""
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]

    if dx == 1 and dy == 0:  # sq1 left of sq2
        return sq1.tr == sq2.tl and sq1.br == sq2.bl
    if dx == -1 and dy == 0:  # sq1 right of sq2
        return sq2.tr == sq1.tl and sq2.br == sq1.bl
    if dx == 0 and dy == 1:  # sq1 above sq2
        return sq1.bl == sq2.tl and sq1.br == sq2.tr
    if dx == 0 and dy == -1:  # sq1 below sq2
        return sq2.bl == sq1.tl and sq2.br == sq1.tr

    return True  # If not adjacent, so there is no constraint and is compatible


def solve(
        positions: List[Tuple[int, int]],
        tiles: List[Tile],
        log: bool = True
    ):
    solutions: List[Dict[Tuple[int, int], Tile]] = []
    assignment: Dict[Tuple[int, int], Tile] = {}
    tiles_counter: Counter[Tile] = Counter(tiles)

    backtrack(0, positions, tiles_counter, assignment, solutions)

    print_solution(solutions, positions, log)

    return solutions


def backtrack(
        index: int,
        positions: List[Tuple[int, int]],
        tile_counts: Counter[Tile],
        assignment: Dict[Tuple[int, int], Tile],
        solutions: List[Dict[Tuple[int, int], Tile]]
) -> None:
    """
    tile_counts: list of all possible wooden tiles remaining to choose from.
    """
    if index == len(positions):
        solutions.append(assignment.copy())
        return

    current_pos = positions[index]

    for tile, count in list(tile_counts.items()):
        if count == 0:
            continue

        for tile_rotation in tile.rotations():

            # Check compatibility with all existing neighbours
            can_place = True
            for prev_pos, prev_square in assignment.items():
                if not is_compatible(prev_pos, prev_square, current_pos, tile_rotation):
                    can_place = False
                    break

            if can_place:
                assignment[current_pos] = tile_rotation
                tile_counts[tile] -= 1
                # Recurse with remaining squares
                backtrack(index + 1, positions, tile_counts, assignment, solutions)
                del assignment[current_pos]  # For backtracking
                tile_counts[tile] += 1  # For backtracking

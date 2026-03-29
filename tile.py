from dataclasses import dataclass
from typing import List

from colors import Color


@dataclass(frozen=True)
class Tile:
    """Wooden tile with its four corner colors."""
    tl: Color
    tr: Color
    br: Color
    bl: Color

    def rotate(self, k: int) -> "Tile":
        """Rotate tile 90 deg clockwise k times"""
        k = k % 4
        tl, tr, br, bl = self.tl, self.tr, self.br, self.bl

        for _ in range(k):
            tl, tr, br, bl = bl, tl, tr, br

        return Tile(tl, tr, br, bl)

    def rotations(self) -> List["Tile"]:
        """Return unique rotations"""
        seen = set[str]()
        result = []
        for k in range(4):
            t = self.rotate(k)
            if str(t) not in seen:
                seen.add(str(t))
                result.append(t)
        return result

    def __str__(self) -> str:
        return f"{self.tl.value}{self.tr.value}{self.br.value}{self.bl.value}"

    def canonical_str(self) -> str:
        """str representation which is independent of rotation"""
        from_tl = f"{self.tl}{self.tr}{self.br}{self.bl}"
        from_tr = f"{self.tr}{self.br}{self.bl}{self.tl}"
        from_br = f"{self.br}{self.bl}{self.tl}{self.tr}"
        from_bl = f"{self.bl}{self.tl}{self.tr}{self.br}"
        return min(from_tl, from_tr, from_br, from_bl)

    def __eq__(self, other):
        """Tiles with different rotations are the same."""
        return other is not None and self.canonical_str() == other.canonical_str()

    def __hash__(self):
        """Tiles with different rotations are the same."""
        return hash(self.canonical_str())

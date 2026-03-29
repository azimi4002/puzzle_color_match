# Tile Placement

I place tiles on predefined coordinates such that adjacent edges match in color. Each tile has four corners `(tl, tr, br, bl)` and can be rotated.

---

## Key Ideas

### 1. Tile Representation
- Each tile is an immutable object.
- Colors are defined using an `Enum`.
- Tiles can be rotated and generating up to 4 unique orientations.

---

### 2. Board & Constraints
- The board is represented as a grid of coordinates (x , y) after being rotated 45° counter‑clockwise. The topmost, leftmost cell is defined as (0, 0).
- The board is defined as a set of fixed coordinates.
- A placement is valid only if all adjacent tiles have matching edge colors.

---

### 3. Backtracking Search
- I use DFS with backtracking:
  - Place tiles one position at a time
  - Try all valid rotations
  - Prune early if constraints fail

---

### 4. Avoiding Duplicates
- Tiles are treated as a **multiset** using a `Counter`
- Prevents redundant permutations when identical tiles exist
- Fixed placement order ensures deterministic solutions

---

## Validation
- Each solution is verified by re-checking all adjacency constraints
- Tests ensure:
  - Correct rotations
  - Valid edge matching
  - No duplicate solutions

---

## Complexity
- Worst-case is exponential (`O(n!)`)
- Practical performance improved via:
  - Early pruning
  - Constraint checking
  - Rotation deduplication

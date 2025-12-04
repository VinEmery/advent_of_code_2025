#!/usr/bin/env python3
from pathlib import Path
from typing import List, Tuple

# Toggle this to False if you want less output
PRINT_GRIDS = True

# 8 neighboring directions (row, col)
NEIGHBORS: List[Tuple[int, int]] = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def count_adjacent_rolls(grid: List[List[str]], r: int, c: int) -> int:
    """Count how many '@' neighbors (8-directional) a cell has."""
    h = len(grid)
    w = len(grid[0])
    cnt = 0
    for dr, dc in NEIGHBORS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '@':
            cnt += 1
    return cnt


def print_grid(grid: List[List[str]]) -> None:
    """Print the current grid."""
    for row in grid:
        print("".join(row))
    print()  # blank line


def print_grid_with_marks(grid: List[List[str]],
                          to_remove: List[Tuple[int, int]]) -> None:
    """
    Print grid where:
      - 'x' marks cells that will be removed this round
      - '@' are other rolls
      - '.' are empty
    """
    h = len(grid)
    w = len(grid[0])
    marked = [row.copy() for row in grid]

    for r, c in to_remove:
        if marked[r][c] == '@':
            marked[r][c] = 'x'

    print_grid(marked)


def simulate_removals_with_visual(grid: List[str]) -> int:
    """
    Repeatedly remove all accessible rolls (cells with '@' having < 4 '@' neighbors)
    until no more can be removed. Return total number of removed rolls.
    Also print each step if PRINT_GRIDS is True.
    """
    if not grid:
        return 0

    g: List[List[str]] = [list(row) for row in grid]
    h = len(g)
    w = len(g[0])

    if PRINT_GRIDS:
        print("Initial state:")
        print_grid(g)

    total_removed = 0
    round_num = 1

    while True:
        to_remove: List[Tuple[int, int]] = []

        # Find all currently accessible rolls
        for r in range(h):
            for c in range(w):
                if g[r][c] != '@':
                    continue
                neighbors = count_adjacent_rolls(g, r, c)
                if neighbors < 4:
                    to_remove.append((r, c))

        if not to_remove:
            if PRINT_GRIDS:
                print("No more removable rolls.")
            break

        if PRINT_GRIDS:
            print(f"Round {round_num} (removing {len(to_remove)} rolls):")
            print_grid_with_marks(g, to_remove)

        # Remove them all at once
        for r, c in to_remove:
            g[r][c] = '.'

        total_removed += len(to_remove)
        round_num += 1

        if PRINT_GRIDS:
            print("After removal:")
            print_grid(g)

    return total_removed


def main() -> None:
    # Read input from "inputday4.txt" in same directory as this script
    script_path = Path(__file__).resolve()
    input_path = script_path.with_name("inputday4.txt")

    lines = [
        line.rstrip("\n")
        for line in input_path.read_text().splitlines()
        if line.strip()
    ]

    total = simulate_removals_with_visual(lines)
    print("Total rolls removed:", total)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from pathlib import Path


def count_accessible_rolls(grid: list[str]) -> int:
    """
    Count how many '@' cells have fewer than 4 adjacent '@' rolls
    in the 8 surrounding positions.
    """
    if not grid:
        return 0

    h = len(grid)
    w = len(grid[0])

    # Sanity: ensure all rows have same width
    for row in grid:
        if len(row) != w:
            raise ValueError("All rows in the input must have the same length")

    # Directions for 8 neighbors: (dy, dx)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    accessible = 0

    for y in range(h):
        for x in range(w):
            if grid[y][x] != "@":
                continue

            neighbor_ats = 0
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w:
                    if grid[ny][nx] == "@":
                        neighbor_ats += 1

            if neighbor_ats < 4:
                accessible += 1

    return accessible


def main() -> None:
    # Read input from file "inputday4.txt" in the same directory as this script
    script_path = Path(__file__).resolve()
    input_path = script_path.with_name("inputday4.txt")

    # Load non-empty lines as the grid
    lines = [
        line.rstrip("\n")
        for line in input_path.read_text().splitlines()
        if line.strip()  # ignore blank lines
    ]

    result = count_accessible_rolls(lines)
    print("Accessible rolls of paper:", result)


if __name__ == "__main__":
    main()

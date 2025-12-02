#!/usr/bin/env python3

# Advent of Code 2025 - Day 2
# Input: one line like
#  2200670-2267527,265-409,38866-50720,...
# Output:
#  Part 1: <sum>
#  Part 2: <sum>

import sys


def parse_ranges(line: str):
    ranges = []
    parts = [p for p in line.strip().split(",") if p]
    for p in parts:
        start, end = map(int, p.split("-"))
        ranges.append((start, end))
    return ranges


def is_invalid_part1(n: int) -> bool:
    """
    Part 1:
    Invalid if the ID consists of some sequence of digits
    repeated exactly twice, e.g. 55, 6464, 123123, 1010.
    """
    s = str(n)
    L = len(s)
    if L % 2 != 0:
        return False
    m = L // 2
    return s == s[:m] * 2


def is_invalid_part2(n: int) -> bool:
    """
    Part 2:
    Invalid if the ID consists of some sequence of digits
    repeated at least twice, e.g. 12341234, 123123123,
    1212121212, 1111111.
    """
    s = str(n)
    L = len(s)
    # Try all possible block sizes m, where we have at least 2 repeats
    for m in range(1, L // 2 + 1):
        if L % m != 0:
            continue
        repeats = L // m
        if repeats < 2:
            continue
        if s == s[:m] * repeats:
            return True
    return False


def solve(ranges):
    part1 = 0
    part2 = 0

    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_part1(n):
                part1 += n
            if is_invalid_part2(n):
                part2 += n

    return part1, part2


def main():
    data = sys.stdin.read().strip()
    if not data:
        print("No input provided.", file=sys.stderr)
        sys.exit(1)

    ranges = parse_ranges(data)
    part1, part2 = solve(ranges)
    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == "__main__":
    main()

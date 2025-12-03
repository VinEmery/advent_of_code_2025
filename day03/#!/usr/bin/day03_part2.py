#!/usr/bin/env python3
from pathlib import Path
from typing import List


def max_subseq(s: str, k: int) -> str:
    """
    Return the lexicographically largest subsequence of length k
    from digit string s, preserving order.
    Greedy stack algorithm, O(n).
    """
    stack: List[str] = []
    n = len(s)
    remove = n - k  # how many digits we can drop

    for ch in s:
        while stack and remove > 0 and stack[-1] < ch:
            stack.pop()
            remove -= 1
        stack.append(ch)

    # If we didn't remove enough, chop off the tail
    return "".join(stack[:k])


def solve(banks: List[str]) -> int:
    # For part 2 we need exactly 12 digits per bank
    return sum(int(max_subseq(bank, 12)) for bank in banks)


def _get_day_number_from_stem(stem: str) -> int:
    """
    Extract the day number from a script name like 'day03_part2' -> 3.
    Looks for 'day' and then reads following digits.
    """
    if "day" not in stem:
        raise ValueError(f"Cannot find 'day' in script name: {stem}")

    i = stem.index("day") + 3
    digits = []
    while i < len(stem) and stem[i].isdigit():
        digits.append(stem[i])
        i += 1

    if not digits:
        raise ValueError(f"No day digits found in script name: {stem}")

    return int("".join(digits))


def main() -> None:
    script_path = Path(__file__).resolve()
    day_num = _get_day_number_from_stem(script_path.stem)

    input_name = f"input_day{day_num}.txt"
    input_path = script_path.with_name(input_name)

    banks = [
        line.strip()
        for line in input_path.read_text().splitlines()
        if line.strip()
    ]

    total = solve(banks)
    print("Part 2:", total)


if __name__ == "__main__":
    main()

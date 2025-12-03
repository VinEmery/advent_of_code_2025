#!/usr/bin/env python3
from pathlib import Path
from typing import List


def max_two_digit(bank: str) -> int:
    """
    Given a string of digits (e.g. '987654321111111'),
    return the largest possible two-digit number that can be formed by
    selecting two positions i < j and concatenating those digits.
    """
    max_val = -1
    n = len(bank)

    for i in range(n):
        d1 = ord(bank[i]) - ord("0")
        for j in range(i + 1, n):
            d2 = ord(bank[j]) - ord("0")
            val = 10 * d1 + d2
            if val > max_val:
                max_val = val

    return max_val


def solve(banks: List[str]) -> int:
    return sum(max_two_digit(bank) for bank in banks)


def main() -> None:
    script_path = Path(__file__).resolve()

    # Extract day number from script name, e.g. "day03" -> 3
    day_digits = "".join(ch for ch in script_path.stem if ch.isdigit())
    day_num = int(day_digits)  # 3

    # Input file: input_day3.txt, input_day4.txt, ...
    input_name = f"input_day{day_num}.txt"
    input_path = script_path.with_name(input_name)

    # Read all non-empty lines as banks
    banks = [
        line.strip()
        for line in input_path.read_text().splitlines()
        if line.strip()
    ]

    total = solve(banks)
    print("Total output joltage:", total)


if __name__ == "__main__":
    main()

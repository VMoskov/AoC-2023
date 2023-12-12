import re
import math


def part1():
    total_sum = 0
    lines = open("day3_input.txt").read().splitlines()
    for index, line in enumerate(lines):
        symbols = [i for i in range(len(line)) if line[i] != "." and not line[i].isdigit()]

        if not symbols:
            continue

        for i in symbols:
            total_sum += sum(adjacent_numbers(lines, index, i))

    print(f"Part1: {total_sum}")


def part2():
    ratios = 0
    lines = open("day3_input.txt").read().splitlines()
    for index, line in enumerate(lines):
        symbols = [i for i in range(len(line)) if line[i] == "*"]

        if not symbols:
            continue

        for i in symbols:
            ratios += math.prod(adjacent_numbers(lines, index, i)) if len(adjacent_numbers(lines, index, i)) == 2 else 0

    print(f"Part2: {ratios}")


def adjacent_numbers(lines, line_index, symbol_index):
    numbers = [extract_number(lines, line_index, symbol_index, "up"),
               extract_number(lines, line_index, symbol_index, "down"),
               extract_number(lines, line_index, symbol_index, "up-right"),
               extract_number(lines, line_index, symbol_index, "right"),
               extract_number(lines, line_index, symbol_index, "down-right"),
               extract_number(lines, line_index, symbol_index, "up-left"),
               extract_number(lines, line_index, symbol_index, "left"),
               extract_number(lines, line_index, symbol_index, "down-left")]
    return set(number for number in numbers if number != 0)


def find_beggining_of_number(line, index):
    if not line[index].isdigit():
        return index+1
    return find_beggining_of_number(line, index - 1)


def extract_number(lines, line_index, symbol_index, direction):
    index_offsets = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
        "up-left": (-1, -1),
        "up-right": (-1, 1),
        "down-left": (1, -1),
        "down-right": (1, 1)
    }

    offset = index_offsets[direction]
    line = lines[line_index + offset[0]]

    if line[symbol_index + offset[1]].isdigit():
        first_digit = find_beggining_of_number(line, symbol_index + offset[1])
        return int(re.compile(r"(\d+)").search(line[first_digit:]).group(0))
    return 0


if __name__ == "__main__":
    part1()
    part2()

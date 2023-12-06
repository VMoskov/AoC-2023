import re


def part1():
    possible_games = []
    pool = {"red": 12, "green": 13, "blue": 14}
    regex = [re.compile(fr"(\d+)\s+{color}") for color in pool]

    for line in open("day2_input.txt"):
        sets = [[int(digit) for digit in pattern.findall(line)] for pattern in regex]  # red, green, blue
        if max(sets[0]) > pool["red"] or max(sets[1]) > pool["green"] or max(sets[2]) > pool["blue"]:
            continue
        else:
            possible_games.append(int(re.findall(r"(\d+)", line)[0]))

    print(f"Part1: {sum(possible_games)}")


def part2():
    powers = []
    regex = [re.compile(fr"(\d+)\s+{color}") for color in ["red", "green", "blue"]]

    for line in open("day2_input.txt"):
        sets = [[int(digit) for digit in pattern.findall(line)] for pattern in regex]
        powers.append(max(sets[0]) * max(sets[1]) * max(sets[2]))

    print(f"Part2: {sum(powers)}")


if __name__ == "__main__":
    part1()
    part2()

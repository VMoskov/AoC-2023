import re
import math


def part1():
    wins = []
    data = open("day6_input.txt", "r")
    times = [int(number) for number in re.findall(r"(\d+)", data.readline().strip())]
    distances = [int(number) for number in re.findall(r"(\d+)", data.readline().strip())]

    for time, distance in zip(times, distances):
        wins.append(sum(1 for speed in range(1, time + 1) if (time - speed) * speed > distance))

    print(f"Part1: {math.prod(wins)}")


def part2():
    data = open("day6_input.txt", "r")
    time = int("".join(re.findall(r"(\d+)", data.readline().strip())))
    distance = int("".join(re.findall(r"(\d+)", data.readline().strip())))
    wins = sum(1 for speed in range(1, time + 1) if (time - speed) * speed > distance)
    print(f"Part2: {wins}")


if __name__ == "__main__":
    part1()
    part2()

import re


def part1():
    calibration_values = []
    for line in open("day1_input.txt"):
        digits = [char for char in line if char.isdigit()]
        calibration_values.append(int("".join([digits[0], digits[-1]])))

    print(f"Part1: {sum(calibration_values)}")


def part2():
    calibration_values = []
    for line in open("./day1_input.txt"):
        line = (line.replace("one", "o1e").replace("two", "t2o").replace("three", "th3ee")
                .replace("four", "f4ur").replace("five", "f5ve").replace("six", "s6x")
                .replace("seven", "se7en").replace("eight", "ei8ht").replace("nine", "n9ne"))

        digits = re.findall(r"(\d)", line)
        calibration_values.append(int("".join([str(digits[0]), str(digits[-1])])))

    print(f"Part2: {sum(calibration_values)}")


if __name__ == "__main__":
    part1()
    part2()
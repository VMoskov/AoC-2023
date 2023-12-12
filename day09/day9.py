import re


def part1():
    extrapolated_values = []
    for line in open("day9_input.txt", 'r'):
        history, differences = get_history_differences(line.strip())
        extrapolated_values.append(get_extrapolated_value(history, differences, 1))

    print(f"Part1: {sum(extrapolated_values)}")


def part2():
    extrapolated_values = []
    for line in open("day9_input.txt", 'r'):
        history, differences = get_history_differences(line.strip())
        extrapolated_values.append(get_extrapolated_value(history, differences, 2))

    print(f"Part2: {sum(extrapolated_values)}")


def get_extrapolated_value(history, differences, part_number):
    i = -1 if part_number == 1 else 0
    for index, difference in enumerate(differences):
        if index < 2:
            continue
        differences[index].append(difference[i] + differences[index-1][-1] if i == -1 else difference[i] - differences[index-1][-1])

    return history[i] + differences[-1][-1] if i == -1 else history[i] - differences[-1][-1]


def get_history_differences(line):
    history = [int(number) for number in re.findall(r"(-*\d+)", line)]
    differences = []

    while True:
        difference = find_differences(differences[-1]) if differences else find_differences(history)
        differences.append(difference)
        if sum(difference) == 0:
            differences.reverse()
            break

    return history, differences


def find_differences(history):
    return [history[i+1] - history[i] for i in range(len(history)-1)]


if __name__ == "__main__":
    part1()
    part2()

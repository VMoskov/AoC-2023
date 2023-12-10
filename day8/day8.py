import re


def part1():
    steps = 0
    nodes, instructions = parse_nodes()
    state = "AAA"

    while True:
        for instruction in instructions:
            side = 0 if instruction == "L" else 1
            state = nodes[state][side]
            steps += 1
            if state == "ZZZ":
                print(f"Part1: {steps}")
                exit(0)


def part2():
    steps = 0
    nodes, instructions = parse_nodes()

    states = [state for state in nodes if state[-1] == "A"]

    while True:
        for instruction in instructions:
            side = 0 if instruction == "L" else 1
            states = [nodes[state][side] for state in states]
            steps += 1
            z = [state for state in states if state[-1] == "Z"]
            if len(z) == len(states):
                print(f"Part2: {steps}")
                exit(0)


def parse_nodes():
    nodes = {}

    for index, line in enumerate(open("day8_input.txt", 'r')):
        if index == 1:
            continue
        if index == 0:
            instructions = line.strip()
            continue

        node = re.findall(r"(\w+)\s+=\s+\((\w+),\s+(\w+)\)", line.strip())[0]
        nodes[node[0]] = (node[1], node[2])

    return nodes, instructions


if __name__ == "__main__":
    part1()
    part2()

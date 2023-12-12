import re
from math import gcd


def part1():
    nodes, instructions = parse_nodes()
    state = "AAA"
    print(f"Part1: {count_steps(nodes, state, instructions, part=1)}")


def part2():
    nodes, instructions = parse_nodes()
    states = [state for state in nodes if state.endswith("A")]
    states_steps = [count_steps(nodes, state, instructions, part=2) for state in states]

    lcm = states_steps[0]
    for i in states_steps[1:]:
        lcm = lcm * i // gcd(lcm, i)

    print(f"Part2: {lcm}")


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


def count_steps(nodes, state, instructions, part):
    steps = 0

    while True:
        for instruction in instructions:
            side = 0 if instruction == "L" else 1
            state = nodes[state][side]
            steps += 1
            if (part == 2 and state.endswith("Z")) or (part == 1 and state == "ZZZ"):
                return steps


if __name__ == "__main__":
    part1()
    part2()

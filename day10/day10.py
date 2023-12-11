def part1():
    landscape = []
    for index, line in enumerate(open("day10_input.txt", 'r')):
        landscape.append(line.strip())
        if line.__contains__("S"):
            S = (index, line.index("S"))

    previous_position = S
    current_position = S
    neighbours = find_neighbours(landscape, S)
    step = next_step(neighbours, current_position, previous_position, landscape[current_position[0]][current_position[1]])
    current_position = make_a_step(current_position, step)
    steps = 1

    while current_position != S:
        neighbours = find_neighbours(landscape, current_position)
        step = next_step(neighbours, current_position, previous_position, landscape[current_position[0]][current_position[1]])
        previous_position = current_position
        current_position = make_a_step(current_position, step)
        steps += 1

    print(f"Part1: {int(steps/2 if steps % 2 == 0 else steps/2 + 1)}")


def find_neighbours(landscape, current_position):
    i, j = current_position
    return [landscape[i + 1][j], landscape[i - 1][j], landscape[i][j + 1], landscape[i][j - 1]]


def next_step(neighbours, current_position, previous_position, symbol):
    """
    neighbours[0] = down
    neighbours[1] = up
    neighbours[2] = right
    neighbours[3] = left
    """

    def valid_move(direction):
        return previous_position != make_a_step(current_position, legend[direction])

    elements = ["|", "-", "7", "J", "L", "F"]
    legend = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}
    moves = {
        "|": ("down", "up"),
        "-": ("right", "left"),
        "7": ("left", "down"),
        "J": ("up", "left"),
        "L": ("up", "right"),
        "F": ("down", "right")
    }

    if symbol == "S":
        if neighbours[0] in ["|", "J", "L"]:
            if valid_move("down"):
                return legend["down"]
        if neighbours[1] in ["|", "7", "F"]:
            if valid_move("up"):
                return legend["up"]
        if neighbours[2] in ["-", "J", "7"]:
            if valid_move("right"):
                return legend["right"]
        if neighbours[3] in ["-", "L", "F"]:
            if valid_move("left"):
                return legend["left"]

    return legend[moves[symbol][0]] if valid_move(moves[symbol][0]) else legend[moves[symbol][1]]


def make_a_step(current_position, step):
    return current_position[0] + step[0], current_position[1] + step[1]


if __name__ == '__main__':
    part1()
    # part2()

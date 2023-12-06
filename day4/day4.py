import re


def part1():
    points = []
    for line in open("day4_input.txt"):
        numbers = re.findall(r'Card\s+(\d+):\s*((\d+\s*)+) \| (\s*(\d+\s*)+)', line.strip())
        numbers = [re.findall(r"(\d+)\s*", numbers[0][i]) for i in range(len(numbers[0])) if i in [1, 3]]
        points.append(len(set(numbers[0]) & set(numbers[1])))

    print(f"Part1: {sum(2**(power-1) for power in points if power != 0)}")


def part2():
    cards = {}
    for line in open("day4_input.txt"):
        numbers = re.findall(r'Card\s+(\d+):\s*((\d+\s*)+) \| (\s*(\d+\s*)+)', line.strip())
        numbers = [re.findall(r"(\d+)\s*", numbers[0][i]) for i in range(len(numbers[0])) if i in [0, 1, 3]]

        current_card = int(numbers[0][0])
        cards[current_card] = 1 if current_card not in cards else cards[current_card] + 1

        intersection = len(set(numbers[1]) & set(numbers[2]))

        for card_id in range(current_card+1, current_card+intersection+1):
            cards[card_id] = cards[current_card] if card_id not in cards else cards[card_id] + cards[current_card]

    print(f"Part2: {sum(cards.values())}")


if __name__ == "__main__":
    part1()
    part2()

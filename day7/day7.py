from collections import Counter


def part1():
    types = {"5": [], "4": [], "FH": [], "3": [], "2P": [], "1P": [], "HC": []}

    for line in open("day7_input.txt", 'r'):
        line = line.strip().split()
        cards = [char for char in line[0]]
        bid = int(line[1])

        types = categorize_hand_1(cards, bid, types)

    order = []
    for key in types:
        if types[key]:
            order += [pair[1] for pair in sorted(types[key], key=sort_cards_1)]

    order.reverse()
    print(f"Part1: {sum([(i+1)*order[i] for i in range(len(order))])}")


def part2():
    types = {"5": [], "4": [], "FH": [], "3": [], "2P": [], "1P": [], "HC": []}

    for line in open("day7_input.txt", 'r'):
        line = line.strip().split()
        cards = [char for char in line[0]]
        bid = int(line[1])

        types = categorize_hand_2(cards, bid, types)

    order = []
    for key in types:
        if types[key]:
            order += [pair[1] for pair in sorted(types[key], key=sort_cards_2)]

    order.reverse()
    print(f"Part2: {sum([(i + 1) * order[i] for i in range(len(order))])}")


def sort_cards_1(hand):
    cards = "AKQJT98765432"
    return [cards.index(card) for card in hand[0]]


def categorize_hand_1(cards, bid, types):
    types[type_of_hand(cards)].append(("".join(cards), bid))
    return types


def sort_cards_2(hand):
    cards = "AKQT98765432J"
    return [cards.index(card) for card in hand[0]]


def categorize_hand_2(cards, bid, types):
    if cards.__contains__("J"):
        cards_frequency = Counter(cards)
        max_frequency = max(cards_frequency.values())
        candidates = [card for card in cards_frequency if cards_frequency[card] == max_frequency and card != "J"]

        if not candidates:
            candidates = [card for card in cards_frequency if card != "J"]

        if not candidates:
            candidates = ["A"]

        best_hand = [card.replace("J", max(candidates, key=sort_cards_1)) for card in cards]
        types[type_of_hand(best_hand)].append(("".join(cards), bid))
        return types

    return categorize_hand_1(cards, bid, types)


def type_of_hand(cards):
    if len(set(cards)) == 1:
        return "5"

    elif len(set(cards)) == 2:
        if cards.count(cards[0]) == 4 or cards.count(cards[0]) == 1:
            return "4"
        else:
            return "FH"

    elif len(set(cards)) == 3:
        for i in range(5):
            if cards.count(cards[i]) == 3:
                return "3"
        else:
            return "2P"

    elif len(set(cards)) == 4:
        return "1P"

    else:
        return "HC"


if __name__ == "__main__":
    part1()
    part2()

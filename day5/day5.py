import re


def part1():
    seeds = []
    locations = []
    almanac = [line for line in open("day5_example.txt", "r").read().splitlines() if line]
    data = {}

    for index, line in enumerate(almanac):
        if index == 0:
            seeds = [int(number) for number in re.findall(r"(\d+)", line)]
            continue

        almanac_map = re.findall(r"(.+)\smap:", line)
        tmp = extract_data(almanac, almanac_map, index)
        if tmp:
            for key, value in tmp.items():
                if value:
                    data[key] = value

    for seed in seeds:
        soil = calculate_property(data, "seed-to-soil", seed)
        fertilizer = calculate_property(data, "soil-to-fertilizer", soil)
        water = calculate_property(data, "fertilizer-to-water", fertilizer)
        light = calculate_property(data, "water-to-light", water)
        temperature = calculate_property(data, "light-to-temperature", light)
        humidity = calculate_property(data, "temperature-to-humidity", temperature)
        locations.append(calculate_property(data, "humidity-to-location", humidity))

    print(f"Part1: {min(locations)}")


def part2():
    seeds = []
    locations = []
    almanac = [line for line in open("day5_input.txt", "r").read().splitlines() if line]
    data = {}

    for index, line in enumerate(almanac):
        if index == 0:
            seeds = [(int(pair[0]), int(pair[1])) for pair in re.findall(r"(\d+) (\d+)", line)]
            continue

        almanac_map = re.findall(r"(.+)\smap:", line)
        tmp = extract_data(almanac, almanac_map, index)
        if tmp:
            for key, value in tmp.items():
                if value:
                    data[key] = value

    for pair in seeds:
        for seed in range(pair[0], pair[0] + pair[1]):
            soil = calculate_property(data, "seed-to-soil", seed)
            fertilizer = calculate_property(data, "soil-to-fertilizer", soil)
            water = calculate_property(data, "fertilizer-to-water", fertilizer)
            light = calculate_property(data, "water-to-light", water)
            temperature = calculate_property(data, "light-to-temperature", light)
            humidity = calculate_property(data, "temperature-to-humidity", temperature)
            locations.append(calculate_property(data, "humidity-to-location", humidity))

    print(f"Part2: {min(locations)}")


def extract_data(almanac, almanac_map, index):
    def extract_info(map_key):
        result = []
        curr = index + 1
        while curr < len(almanac) and almanac_map[0] == map_key and almanac[curr][0].isdigit():
            result.append([int(number) for number in re.findall(r"(\d+)", almanac[curr])])
            curr += 1
        return result

    if not almanac_map:
        return None

    data = {
        "seed-to-soil": extract_info("seed-to-soil"),
        "soil-to-fertilizer": extract_info("soil-to-fertilizer"),
        "fertilizer-to-water": extract_info("fertilizer-to-water"),
        "water-to-light": extract_info("water-to-light"),
        "light-to-temperature": extract_info("light-to-temperature"),
        "temperature-to-humidity": extract_info("temperature-to-humidity"),
        "humidity-to-location": extract_info("humidity-to-location")
    }

    return data


def calculate_property(data, map_type, value):
    result = value
    for i in range(len(data[map_type])):
        if data[map_type][i][1] <= value < data[map_type][i][1] + data[map_type][i][2]:
            result = data[map_type][i][0] + value - data[map_type][i][1]
    return result


if __name__ == "__main__":
    part1()
    # part2()

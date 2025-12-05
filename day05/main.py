import json
from combine_ranges import combine_ranges
from part1 import part1
from part2 import part2


with open("day05/example_input.txt", "r") as f:
    example_list = [line.strip() for line in f.readlines()]
    gap = example_list.index("")
    id_ranges_str, ids = example_list[:gap], [int(id) for id in example_list[gap + 1 :]]
    example_input = (combine_ranges(id_ranges_str), ids)

with open("day05/example_output.json", "r") as f:
    example_output = json.load(f)

with open("day05/puzzle_input.txt", "r") as f:
    puzzle_list = [line.strip() for line in f.readlines()]
    gap = puzzle_list.index("")
    id_ranges_str, ids = puzzle_list[:gap], [int(id) for id in puzzle_list[gap + 1 :]]
    puzzle_input = (combine_ranges(id_ranges_str), ids)


def main():
    example_result_p1 = part1(example_input)
    assert (
        example_result_p1 == example_output["part1"]
    ), f"Expected {example_output["part1"]}, got {example_result_p1}"

    puzzle_result_p1 = part1(puzzle_input)
    print(f"Part 1: {puzzle_result_p1}")

    example_result_p2 = part2(example_input)
    assert (
        example_result_p2 == example_output["part2"]
    ), f"Expected {example_output["part2"]}, got {example_result_p2}"

    puzzle_result_p2 = part2(puzzle_input)
    print(f"Part 2: {puzzle_result_p2}")


if __name__ == "__main__":
    main()

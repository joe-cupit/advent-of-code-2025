import json
from part1 import part1
from part2 import part2


with open("day03/example_input.txt", "r") as f:
    example_input = [row.strip() for row in f.readlines()]

with open("day03/example_output.json", "r") as f:
    example_output = json.load(f)

with open("day03/puzzle_input.txt", "r") as f:
    puzzle_input = [row.strip() for row in f.readlines()]


def main():
    example_result_p1 = part1(example_input)
    assert (
        example_result_p1 == example_output["part1"]
    ), f"Expected {example_output["part1"]}, got {example_result_p1}"

    puzzle_result_p1 = part1(puzzle_input)
    print(f"Part 1 sum: {puzzle_result_p1}")

    example_result_p2 = part2(example_input)
    assert (
        example_result_p2 == example_output["part2"]
    ), f"Expected {example_output["part2"]}, got {example_result_p2}"

    puzzle_result_p2 = part2(puzzle_input)
    print(f"Part 2 sum: {puzzle_result_p2}")


if __name__ == "__main__":
    main()

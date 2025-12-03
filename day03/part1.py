from turn_on_batteries import turn_on_batteries


def part1(puzzle_input: list[str]):
    bank_sum = 0
    for bank in puzzle_input:
        bank_sum += turn_on_batteries(bank, 2)

    return bank_sum

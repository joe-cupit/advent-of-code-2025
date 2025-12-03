def biggest_and_index(bank: str):
    batteries = [(int(b), i) for i, b in enumerate(bank)]
    batteries.sort(key=lambda b: b[0], reverse=True)

    return batteries[0]


def part1(puzzle_input: list[str]):
    bank_sum = 0

    for bank in puzzle_input:
        n1, i1 = biggest_and_index(bank[:-1])
        n2, _ = biggest_and_index(bank[i1 + 1 :])

        bank_sum += int(f"{n1}{n2}")

    return bank_sum

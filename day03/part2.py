def biggest_and_index(bank: str):
    batteries = [(int(b), i) for i, b in enumerate(bank)]
    batteries.sort(key=lambda b: b[0], reverse=True)

    return batteries[0]


def part2(puzzle_input: list[str]):
    BATTERIES = 12

    bank_sum = 0
    for bank in puzzle_input:
        batteries_on = ""

        for i in range(BATTERIES):
            joltage, index = biggest_and_index(
                bank[: -(BATTERIES - 1 - i)] if i < (BATTERIES - 1) else bank
            )

            batteries_on += str(joltage)
            bank = bank[index + 1 :]

        bank_sum += int(batteries_on)

    return bank_sum

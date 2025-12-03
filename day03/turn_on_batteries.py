def biggest_and_index(bank: str):
    batteries = [(int(b), i) for i, b in enumerate(bank)]
    batteries.sort(key=lambda b: b[0], reverse=True)

    return batteries[0]


def turn_on_batteries(bank: str, turn_on: int):
    batteries_on = ""

    for i in range(turn_on):
        joltage, index = biggest_and_index(
            bank[: -(turn_on - 1 - i)] if i < (turn_on - 1) else bank
        )

        batteries_on += str(joltage)
        bank = bank[index + 1 :]

    return int(batteries_on)

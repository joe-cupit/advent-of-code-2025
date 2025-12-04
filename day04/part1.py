from count_adjacents import count_adjacents

PAPER_ROLLS = "@"


def part1(puzzle_input: list[str]):
    accessible_paper = 0

    for ri, row in enumerate(puzzle_input):
        for ci, col in enumerate(row):
            if col != PAPER_ROLLS:
                continue

            if count_adjacents(puzzle_input, PAPER_ROLLS, (ri, ci)) < 4:
                accessible_paper += 1

    return accessible_paper

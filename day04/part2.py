from count_adjacents import count_adjacents

PAPER_ROLLS = "@"


def part2(puzzle_input: list[str]):
    removed_paper = 0

    removed_some_paper = True

    while removed_some_paper:
        removed_some_paper = False

        for ri, row in enumerate(puzzle_input):
            for ci, col in enumerate(row):
                if col != PAPER_ROLLS:
                    continue

                if count_adjacents(puzzle_input, PAPER_ROLLS, (ri, ci)) < 4:
                    removed_paper += 1
                    puzzle_input[ri] = (
                        puzzle_input[ri][:ci] + "x" + puzzle_input[ri][ci + 1 :]
                    )
                    removed_some_paper = True

    return removed_paper

def combine_ranges(id_ranges_str):
    overlapping_id_ranges = sorted(
        [[int(id) for id in ids.split("-")] for ids in id_ranges_str]
    )

    id_ranges = [overlapping_id_ranges[0]]
    for id_range in overlapping_id_ranges[1:]:
        if id_range[0] <= id_ranges[-1][1] + 1:
            id_ranges[-1][1] = max(id_range[1], id_ranges[-1][1])
        else:
            id_ranges.append(id_range)

    return id_ranges

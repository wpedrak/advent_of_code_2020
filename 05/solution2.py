def get_lines():
    file = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in file]
    return lines


def get_id(seat: str):
    seat = seat.replace('F', '0')
    seat = seat.replace('B', '1')
    seat = seat.replace('L', '0')
    seat = seat.replace('R', '1')

    return int(seat, base=2)


all_free_ids = set(range(2 ** 10)) - set(map(get_id, get_lines()))

for free_id in all_free_ids:
    if free_id == 0 or free_id == 2 ** 10 - 1:
        continue

    if (free_id - 1) in all_free_ids or (free_id + 1) in all_free_ids:
        continue

    print(free_id)

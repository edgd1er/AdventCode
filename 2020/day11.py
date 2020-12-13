# AdventCode Day 11
from copy import deepcopy

import time

debug = False


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))
        return ret

    return wrap


# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
#    Otherwise, the seat's state does not change.

deltas = [(temp_row, temp_col)
          for temp_row in range(-1, 2) for temp_col in range(-1, 2)
          if not temp_row == temp_col == 0]


def get_neighbours(input_local, row, col, debug=False):
    print("get_neighbours row:", len(input_local), " ,col:", len(input_local[0])) if debug else ""
    nbours = []
    for drow, dcol in deltas:
        nrow = row + drow
        ncol = col + dcol
        if 0 <= nrow < len(input_local):
            if 0 <= ncol < len(input_local[nrow]):
                print("get_neighbours: nrow:", nrow, "ncol:", ncol, "seat: ", input_local[nrow][ncol], " ,input",
                      "".join(input_local[nrow])) if debug else ""
                nbours.append((nrow, ncol))
    return nbours


def get_neighbours2(input_local, row, col, debug=False):
    nbours = []
    print("get_neighbours2 start row:", row, " ,col:", col) if debug else ""
    for drow, dcol in deltas:
        nrow = row + drow
        ncol = col + dcol
        # while in range and no floor met, continue to inspect
        while 0 <= nrow < len(input_local) and 0 <= ncol < len(input_local[row]) and input_local[nrow][ncol] == ".":
            nrow += drow
            ncol += dcol
        # end of array or floor found
        if 0 <= nrow < len(input_local) and 0 <= ncol < len(input_local[nrow]):
            print("get_neighbours: nrow:", nrow, "ncol:", ncol, "seat: ", input_local[nrow][ncol], " ,input",
                  "".join(input_local[nrow])) if debug else ""
            nbours.append((nrow, ncol))
    print("get_neighbours2 end: nbours:", nbours) if debug else ""
    return nbours


def get_neighbours_seated(input_local, row, col, part, debug=False):
    nbours = get_neighbours(input_local, row, col, debug) if part == 4 else get_neighbours2(input_local, row, col,
                                                                                            debug)
    nb_seats = sum(input_local[row_][col_] == "#" for row_, col_ in nbours)
    print("get_neighbours_seated: ", nb_seats, "row:", row, "col:", col, debug) if debug else ""
    return nb_seats


@timing
def part1(input_local, max_neighbours, debug=False):
    loop = 0
    print("row:", len(input_local), " ,col:", len(input_local[0])) if debug else ""
    while True:
        changed = 0
        new_input = deepcopy(input_local)
        for row, col in seats_cords:
            seat = input_local[row][col]
            print("seat:", row, col, "val:", seat) if debug else ""
            nbours = get_neighbours_seated(input_local, row, col, max_neighbours, False)
            print("neighbours for ", col, row, ": ", nbours) if debug else ""
            if seat == "L" and nbours == 0:
                new_input[row][col] = "#"
                print("occupying seat", row, col) if debug else ""
                changed = 1
            elif seat == "#" and nbours >= max_neighbours:
                print("freeing seat", row, col) if debug else ""
                new_input[row][col] = "L"
                changed = 1
        # no more changes
        # if new_input == input_local:
        print("changed:", changed) if debug else ""
        if changed == 0:
            nb_seat = sum(seat == '#' for line in new_input for seat in line)
            return loop, nb_seat, input_local
        # all changed are performed
        input_local = new_input
        for rowidx, row in enumerate(input_local):
            print(rowidx, " ".join(row)) if debug else ""
        loop += 1


# Main
# part 1 sample
debug = True
input_list_sample = list(map(list, open("day11_sample.lst").read().splitlines()))
seats_cords = [(row_idx, col_idx)
               for row_idx, row in enumerate(input_list_sample)
               for col_idx, seat in enumerate(row)
               if seat != '.']

loop, nb, input = part1(input_list_sample, 4, False)
print("part 1 sample loops: ", loop, " ,seated: ", nb)  # 5 loops , 37 seats
for rowidx, row in enumerate(input):
    print(rowidx, " ".join(row))

input = list(map(list, open("day11.lst").read().splitlines()))
seats_cords = [(row_idx, col_idx)
               for row_idx, row in enumerate(input)
               for col_idx, seat in enumerate(row)
               if seat != '.']
print("\ninput row:", len(input), " ,col:", len(input[0]))
loop, nb, input = part1(input, 4, False)
print("part 1 loops: ", loop, ", seated: ", nb)  # 81 loops, 2368 seats

# part2
input_list_sample = list(map(list, open("day11_sample.lst").read().splitlines()))
seats_cords = [(row_idx, col_idx)
               for row_idx, row in enumerate(input_list_sample)
               for col_idx, seat in enumerate(row) if seat != '.']
loop, nb, input = part1(input_list_sample, 5, False)
print("part 2 sample loops: ", loop, " ,seated: ", nb)  # loops: 6 seats: 26
for rowidx, row in enumerate(input):
    print(rowidx, " ".join(row))

input = list(map(list, open("day11.lst").read().splitlines()))
seats_cords = [(row_idx, col_idx)
               for row_idx, row in enumerate(input)
               for col_idx, seat in enumerate(row)
               if seat != '.']
print("\ninput row:", len(input), " ,col:", len(input[0]))
loop, nb, input = part1(input, 5, False)
print("part 2 loops: ", loop, ", seated: ", nb)  # loops:  84 , seated:  2124

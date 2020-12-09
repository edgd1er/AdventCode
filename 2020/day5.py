# AdventCode Day 5
import collections
import time

lList = []
seats = {}
o_seats = {}

input_list = open("day5.lst").read().split("\n")

for line in input_list:
    lList.append(line.strip())


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))
        return ret

    return wrap


# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.def

def get_row(seat_row_min, seat_row_max, decode):
    current = decode[0]
    decode = decode[1:]
    if decode == "":
        if current == "B":
            return seat_row_max
        else:
            return seat_row_min
    if current == "B":
        seat_row_min = seat_row_min + round((seat_row_max - seat_row_min) / 2)
    if current == "F":
        seat_row_max = seat_row_max - round((seat_row_max - seat_row_min) / 2)
    # print("get_row: min: {}, max {}, current: {}, decode: {}".format(seat_row_min, seat_row_max, current, decode))
    return get_row(seat_row_min, seat_row_max, decode)


def get_seat(seat_min, seat_max, decode):
    current = decode[0]
    decode = decode[1:]
    if decode == "":
        if current == "R":
            return seat_max
        else:
            return seat_min
    if current == "R":
        seat_min = seat_min + round((seat_max - seat_min) / 2)
    if current == "L":
        seat_max = seat_max - round((seat_max - seat_min) / 2)
    # print("get_seat: min: {}, max {}, current: {}, decode: {}".format(seat_min, seat_max, current, decode))
    return get_seat(seat_min, seat_max, decode)


@timing
def part1(to_decode):
    start_time = time.time()
    r1, idx, max_id = 0, 0, 0
    for el in to_decode:
        # idx += 1
        # print("line: {}, r: {}, c: {}, idx: {}".format(el, el[:7], el[7:], idx))
        row = get_row(0, 127, el[0:7])
        seat = get_seat(0, 7, el[7:])
        seat_id = row * 8 + seat
        seats[seat_id] = str(row) + "," + str(seat)
        max_id = seat_id if seat_id > max_id else max_id
        # print("line: {}, row: {}, seat: {}, ID: {}".format(el, row, seat, seat_id))

    print("part1: max ID: {}, time {} seconds".format(max_id, time.time() - start_time))


@timing
def part2(pport):
    start_time = time.time()
    r2 = 0
    o_seats = collections.OrderedDict(sorted(seats.items()))
    for key in o_seats.keys():
        if r2 == 0:
            r2 = key
        if r2 != key:
            print("missing r2: {} next key: {}, o_seats: {}".format(r2, key, o_seats[key]))
            break
        r2 += 1

    # for key in range(600,610):
    #    print("key: {}, o_seats: {}".format(key, o_seats[key])) if key in o_seats else print
    c, l = o_seats[r2 - 1].split(",")
    myseat = str(c) + "," + str(int(l) + 1)
    print("part2: r2:", r2, " my seat: ", myseat, ", time:", time.time() - start_time, "seconds")


print("checks")
a = get_row(0, 127, "FBFBBFF")
b = get_seat(0, 7, "RLR")
print(a, b, a * 8 + b)

# BBFFBBFRLL: row 44, column 5, seat ID 357.
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# part1(['FBFBBFFRLR','BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL'])
# quit

print("list size: {0}".format(str(len(lList))))
print("list: [0]: {0}".format(str(lList[0])))
part1(lList)  # 987
print("\n")
part2(lList)  # 603

# AdventCode Day 12

from collections import deque

import time

debug = False
directions = {'E': (0, 1), 'S': (-1, 0), 'W': (0, -1), 'N': (1, 0)}


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))
        return ret

    return wrap


@timing
def part1(input):
    x, y = 0, 0
    for dir, value in input:
        if dir == 'F':
            y += current_dir[0][0] * value
            x += current_dir[0][1] * value
        elif dir in directions:
            y += directions[dir][0] * value
            x += directions[dir][1] * value
        elif dir in {'L', 'R'}:
            current_dir.rotate({'L': 1, 'R': -1}[dir] * (value // 90))
    print("part1: manhattan distance:", abs(y) + abs(x))


# Main
# part 1 sample
debug = True
input_list_sample = [(item[0], int(item[1:])) for item in list(open("day12_sample.lst").read().splitlines())]
print(input_list_sample)
current_dir = deque(directions.values())
part1(input_list_sample)  # 25

input_list = [(item[0], int(item[1:])) for item in list(open("day12.lst").read().splitlines())]
print("orders: ", len(input_list))
current_dir = deque(directions.values())
part1(input_list)  # 2228


# part2
@timing
def part2(input):
    y, x = 0, 0
    y_way, x_way = 1, 10
    for action, value in input:
        if action == 'F':
            y += y_way * value
            x += x_way * value
        elif action in directions:
            y_way += directions[action][0] * value
            x_way += directions[action][1] * value
        else:
            for _ in range(0, value, 90):
                y_way, x_way = (x_way, -y_way) if action == 'L' else (-x_way, y_way)
    print("part2: ", abs(y) + abs(x))


part2(input_list_sample)
part2(input_list)

# AdventCode Day 9
import time
from itertools import combinations

debug = False


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))
        return ret

    return wrap


# preamble of 25 numbers.
# After that, each number you receive should be the
# sum of any two of the 25 immediately previous numbers.
# The two numbers will have different values,
# and there might be more than one such pair.
@timing
def check_preamble(length, input_list):
    idx = length
    res = []
    while idx <= len(input_list):
        res = []
        preamble = input_list[idx - length:idx]
        current = int(input_list[idx])
        if not any((num1 + num2 == current) for num1, num2 in combinations(preamble, 2)):
            return current
        idx += 1
    print(res)
    return True


@timing
def part1(length, input):
    print("part1: length: ", length, ", nb: ", len(input), ":", check_preamble(length, input))


@timing
def part2(stop_value, input):
    for inf in range(input.index(stop_value)):
        for sup in range(input[inf + 1]):
            if sum(input[inf:sup]) > stop_value: break
            if sum(input[inf:sup]) == stop_value:
                input_part = input[inf:sup]
                print("som of input[", inf, ":", sup, "]=", stop_value, " //", input_part)
                print("min: ", min(input_part), "+", max(input_part), "=", min(input_part) + max(input_part))
                break


# Main
# part 1 sample
input_list_sample = list(map(int, open("day9_sample.lst").read().splitlines()))
print("input: ", input_list_sample)

part1_rep = check_preamble(5, input_list_sample)
print("direct check: ", part1(5, input_list_sample))
part1(5, input_list_sample)  # 127

input_list = list(map(int, open("day9.lst").read().splitlines()))
part1(25, input_list)  # 22477624

# https://github.com/filipmlynarski/Advent-of-Code/blob/master/2020/09.py
part_1 = None
for idx in range(25, len(input_list)):
    if not any(num_1 + num_2 == input_list[idx]
               for num_1, num_2 in combinations(input_list[idx - 25: idx], 2)):
        part_1 = (input_list[idx])
        break
print("\npart1_sol:", part_1)

# part2 sample: find proper sequence by replacing 1 replace jmp -> nop or nop-> jmp once per cmds
input_list_sample = list(map(int, open("day9_sample.lst").read().splitlines()))
part2(127, input_list_sample)

input_list = list(map(int, open("day9.lst").read().splitlines()))
part2(22477624, input_list)

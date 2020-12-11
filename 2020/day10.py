# AdventCode Day 10
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


# The charging outlet has an effective rating of 0 jolts, so the only adapters that could connect to it directly would need to have a joltage rating of 1, 2, or 3 jolts. Of these, only one you have is an adapter rated 1 jolt (difference of 1).
# From your 1-jolt rated adapter, the only choice is your 4-jolt rated adapter (difference of 3).
#  From the 4-jolt rated adapter, the adapters rated 5, 6, or 7 are valid choices. However, in order to not skip any adapters, you have to pick the adapter rated 5 jolts (difference of 1).
#  Similarly, the next choices would need to be the adapter rated 6 and then the adapter rated 7 (with difference of 1 and 1).
#  The only adapter that works with the 7-jolt rated adapter is the one rated 10 jolts (difference of 3).
#  From 10, the choices are 11 or 12; choose 11 (difference of 1) and then 12 (difference of 1).
#  After 12, only valid adapter has a rating of 15 (difference of 3), then 16 (difference of 1), then 19 (difference of 3).
#   Finally, your device's built-in adapter is always 3 higher than the highest adapter, so its rating is 22 jolts (always a difference of 3).

def get_next_adapter(input, path, which):
    print("get_next_adapter start current:", input[0], ", input: ", input, ", path: ", path) if debug else ""
    if len(input) == 0: return [], path, which
    if len(input) == 1:
        print("exit function:", which, "path: ", path, "input: ", input)
        # path.append(input[0])
        return [], path, which
    if path == []:
        path.append(input[0])
        local_input = input[1:]
    else:
        local_input = input
    # else:
    #    local_input = input
    res = [adapter for adapter in local_input if adapter <= input[0] + 3 and adapter > input[0]]
    sol = res[which]
    path.append(sol)
    new_input = local_input[local_input.index(sol):]
    print("get_next_adapter end current:", input[0], ", res", res, ", input: ", new_input
          , ", path: ", path) if debug else ""
    return get_next_adapter(new_input, path, which)


@timing
def part1(input):
    sorted_input = [0] + input + [max(input) + 3]
    print("sorted input:", sorted_input) if debug else ""
    diff_jol = {1: 0, 3: 0}
    local_input = sorted_input.copy()
    (_, path, which) = get_next_adapter(local_input, [], 0)
    diff = {1: 0, 3: 0}
    for i in range(1, len(path)):
        diff[path[i] - path[i - 1]] += 1
    print("nb of 1 and 3: ", diff, diff[1] * diff[3])


@timing
def part2(input):
    print("input:", input) if debug else ""
    paths = [0] * (max(input) + 1)
    paths[0] = 1
    for index in range(1, max(input) + 1):
        for x in range(1, 4):
            if (index - x) in input:
                paths[index] += paths[index - x]

    print("part 2: nb solutions: ", paths[-1])


# Main
# part 1 sample
debug = True
input_list_sample = sorted(list(map(int, open("day10_sample.lst").read().splitlines())))
print("input: ", input_list_sample)

part1(input_list_sample)  # expected : 1:7 3:5

debug = False
input_list = sorted(list(map(int, open("day10.lst").read().splitlines())))
part1(input_list)  # 2046

diff = {1: 0, 3: 0}
# https://github.com/filipmlynarski/Advent-of-Code/blob/master/2020/10.py
sorted_input = [0] + input_list + [input_list[-1] + 3]
for num_1, num_2 in zip(sorted_input, sorted_input[1:]):
    # print(num_1, num_2)
    diff[num_2 - num_1] += 1
print("\npart1 sol sample with zip :", diff[1] * diff[3])

# part2 sample: find proper sequence by replacing 1 replace jmp -> nop or nop-> jmp once per cmds
input_list = sorted(list(map(int, open("day10.lst").read().splitlines())))
sorted_input = [0] + input_list + [max(input_list) + 3]
part2(sorted_input)

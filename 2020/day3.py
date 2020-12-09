# AdventCode Day 3
import time

lList = []
lValues = []

with open('day3.lst', 'r') as f:
    for line in f:
        lList.append(line.strip())


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))
        return ret

    return wrap


@timing
def part1(nums):
    start_time = time.time()
    lineIdx, idx, r0, r1, r2 = 0, 0, 0, 0, 0
    for el in nums:
        idx = (3 * lineIdx) % (len(el))
        r0 += el[idx] == '.'
        r1 += el[idx] == '#'
        # print("part1: line: {}, idx: {}, string: {}, len {} ".format(lineIdx, idx, el[idx],len(el)))
        lineIdx += 1

    print("part1: (3,1): ", r1, ", time:", time.time() - start_time, "seconds")


# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

@timing
def part2(nums):
    start_time = time.time()
    line_idx, idx, r1, r2, r3, r4, r5, s2 = 0, 0, 0, 0, 0, 0, 0, 0
    idx1, idx2, idx3, idx4, idx5 = 0, 0, 0, 0, 0
    for el in nums:
        line_len = len(el)
        # print("part2: line: {}, idx: {}, string: {} ".format(line_idx % 2, idx, line_len))
        r1 += el[(line_idx) % line_len] == '#'
        r2 += el[(3 * (line_idx)) % line_len] == '#'
        r3 += el[(5 * (line_idx)) % line_len] == '#'
        r4 += el[(7 * (line_idx)) % line_len] == '#'
        r5 += (el[int(line_idx / 2) % line_len] == '#') and ((line_idx) % 2 == 0)
        # print("part2: r5: {}, idx: {}, string: {}, pair: {} , pos: {}".format(r5, line_idx, el[ line_idx % (line_len)], (line_idx+1) %2,int(line_idx/2) % (line_len - 1)))
        line_idx += 1

    print("\npart2: (1,1): {}, (3,1): {}, (5,1): {}, (7,1): {}, (1,2): {}, all: {}, time: {}".format(r1, r2, r3, r4, r5,
                                                                                                     r1 * r2 * r3 * r4 * r5,
                                                                                                     time.time() - start_time,
                                                                                                     "seconds"))


print("list size: {0}".format(str(len(lList))))
print("list: [0,0] :{0}".format(str(lList[0])))
part1(lList)
part2(lList)

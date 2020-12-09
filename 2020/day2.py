# AdventCode Day 2
import re
import time

lList = []
lValues = []

with open('day2.lst', 'r') as f:
    for line in f:
        lList.append(line.split())


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
    correct, r1, r2  = 0,0,0
    for el in nums:
        min, max = map(int, el[0].split('-'))
        letter = el[1][0]
        pwd = el[2]
        pattern = "[{letter}]{many}"
        m = re.findall(letter, pwd)
        correct += min <= len(m) <= max
        r1 += min <= pwd.count(letter) <= max

    print("part1: x to y times letter : correct ", correct, ", r1: ",r1,", time:", time.time() - start_time, "seconds")


@timing
def part2(nums):
    start_time = time.time()
    correct, r2 = 0, 0
    for el in nums:
        min, max = map(int, el[0].split('-'))
        letter = el[1][0]
        pwd = el[2]
        r2 += sum(pwd[x - 1] == letter for x in (min, max)) == 1
        if (pwd[min - 1] == letter or pwd[max - 1] == letter) and pwd[min - 1] != pwd[max - 1]:
            correct += 1

    print("\npart2: letter in pos1 or pos2 not both, correct ", correct, "r2: ", r2,", time:", time.time() - start_time, "seconds")

print("list size: {0}".format(str(len(lList))))
print("list: [0,0] :{0}".format(str(lList[0])))
part1(lList);
part2(lList);

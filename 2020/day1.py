# AdventCode Day 1
import time

with open('day1.lst', 'r') as f:
    lValues = [int(x) for x in f]

lValues.sort()


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
    triple = [(a, b) for a in nums for b in nums if a + b == 2020]
    print("find a,b where a+b=2020")
    for a, b in triple:
        print("part1 a: {0} x b:{1} = {2}".format(a, b, a * b))
    print("part1: ", time.time() - start_time, "seconds\n")


@timing
def part2(nums):
    start_time = time.time()
    triple = [(a, b, c) for a in nums for b in nums for c in nums if a + b + c == 2020]
    for a, b, c in triple:
        print("part2 a:{0} x b:{1}  x c:{2} = {3}".format(a, b, c, a * b * c))
    print("find a,b,c where a+b+c=2020")
    # print("part2 e1: {0}, e2:{1}, e3: {2} = {3}".format(triple, triple, str(c), str(el*el2*el3)))
    print("part2: ", time.time() - start_time, "seconds")


@timing
def special_pair(nums):
    start_time = time.time()
    pair = [(a, b) for a in nums for b in nums if a + b == 2020]
    print("special_pair:", time.time() - start_time, "seconds")
    return pair[0][0] * pair[0][1]


@timing
def special_triple(nums):
    start_time = time.time()
    triple = [(a, b, c) for a in nums for b in nums for c in nums if a + b + c == 2020]
    print("special_triple: ", time.time() - start_time, "seconds")
    return triple[0][0] * triple[0][1] * triple[0][2]


part1(lValues)
part2(lValues)

print("\nspecial part1: {}".format(special_pair(lValues)))
print("special part2: {}".format(special_triple(lValues)))

print("list size: {0}".format(str(len(lValues))))

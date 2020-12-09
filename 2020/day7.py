# AdventCode Day 1
import time

lList = []
debug = False

input_list_sample = open("day7_sample.lst").read().splitlines()
input_list = open("day7.lst").read().splitlines()


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))
        return ret

    return wrap


@timing
def fill_dic_with(input_list):
    bags = dict()
    for line in input_list:
        left_bag, right_bags = line.split(' contain ')
        # change left into tuple ('color1','color2)
        left_bag = tuple(left_bag.split()[:2])
        bags[left_bag] = list()
        if right_bags != "no other bags.":
            for right_bag in right_bags.split(', '):
                amount, *colors, _ = right_bag.split()
                bags[left_bag].append((int(amount), tuple(colors)))
        print("left bag: ", left_bag, ", right_bags:", bags[left_bag]) if debug else ""
    return bags


def part1(bag_color: tuple) -> bool:
    print("par1: bag: ", bag_color, ", right_bags:", bags[bag_color]) if debug else ""
    return any(color == target or part1(color) for _, color in bags[bag_color])


def part2(bag_color: tuple) -> int:
    return 1 + sum(cnt * part2(color) for cnt, color in bags[bag_color])


@timing
def get_ans1(d):
    return list(map(part1, d))


@timing
def get_ans2(d):
    return part2(target) - 1


bags = fill_dic_with(input_list_sample)

if debug:
    print("bags: ", bags)
    for key in bags.keys():
        print("for d key: ", key, bags[key])

# 4
target = ('shiny', 'gold')
ans = get_ans1(bags)
print("sample par1: ", sum(ans), " keys: ", list(ans))

ans = get_ans2(bags)
print("Sample par2: ", ans)

# 101
bags = fill_dic_with(input_list)
ans = get_ans1(bags)
print("par1: ", sum(ans), " keys: ", list(ans))

debug = True
# part 2
ans = get_ans2(target)
print("par2: ", ans)

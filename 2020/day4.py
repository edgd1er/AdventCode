# AdventCode Day 1
import re
import time

lList = []
lValues = []

input_list = open("day4.lst").read().strip().split("\n")
idx = 0
tmp = ""

rules = {'byr': 1,  # Birth year
         'iyr': 1,  # (Issue Year)
         'eyr': 1,  # (Expiration Year)
         'hgt': 1,  # (Height)
         'hcl': 1,  # (Hair Color)
         'ecl': 1,  # (Eye Color)
         'pid': 1,  # (Passport ID)
         # 'cid': 0  # (Country ID)
         }

for line in input_list:
    tmp += line + " "
    if line == "":
        lList.append(tmp.strip())
        # print("line: {}, {}".format(idx, tmp))
        idx += 1
        tmp = ""
lList.append(tmp.strip())


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))
        return ret

    return wrap


def check_valid(el):
    d = dict(fd.split(":") for fd in el.split(" "))
    keys = d.keys()
    return all(k in keys for k in rules.keys())


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
def check_valid2(el):
    d = dict(fd.split(":") for fd in el.split(" "))
    # required fields
    if not all(k in d.keys() for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
        return 0
    # byr is digit &  born between 1920 and 2020
    if not (d['byr'].isdigit() or len(d['byr']) == 4):
        return 0
    if not (1920 <= int(d['byr']) <= 2002):
        return 0
    # issue is digit 2010 2020
    if not d['iyr'].isdigit() or len(d['iyr']) != 4:
        return 0
    if not (2010 <= int(d['iyr']) <= 2020):
        return 0
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not d['eyr'].isdigit() or len(d['eyr']) != 4:
        return 0
    if not (2020 <= int(d['eyr']) <= 2030):
        return 0
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    if d['hgt'][-2:] not in {'cm', 'in'}:
        return 0
    if d['hgt'].endswith("cm") and not (150 <= int(d['hgt'][:-2]) <= 193):
        return 0
    if d['hgt'].endswith("in") and not (59 <= int(d['hgt'][:-2]) <= 76):
        return 0
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if not re.findall("#[0-9a-f]{6}", d['hcl']):
        return 0
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if not d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return 0
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if not d['pid'].isdigit() or len(d['pid']) != 9:
        return 0
    # cid (Country ID) - ignored, missing or not.
    return 1


# 131

@timing
def part1(pport):
    start_time = time.time()
    r1, r2 = 0, 0
    for el in pport:
        r1 += check_valid(el)

    print("part1: r1:", r1, ", time:", time.time() - start_time, "seconds")


@timing
def part2(pport):
    start_time = time.time()
    r2 = 0
    for el in pport:
        r2 += check_valid2(el)

    print("\npart2: r2:", r2, ", time:", time.time() - start_time, "seconds")


def part1sol(data):
    passports = data.split('\n\n')
    passports = [p.split() for p in passports]
    print("lines: ", len(passports))
    count = 0
    for passport in passports:
        # print("line: ",passport)
        keys = {p.split(':')[0] for p in passport}
        count += all(k in keys for k in {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'})
    return count


def part2sol(data):
    passports = data.split('\n\n')
    passports = [p.split() for p in passports]
    print("lines: ", len(passports))
    count = 0
    for passport in passports:
        keys = {p.split(':')[0]: p.split(':')[1] for p in passport}
        # print("keys: ",keys)
        if not all(k in keys for k in {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}):
            continue
        if not keys['byr'].isdigit():
            continue
        if not (1920 <= int(keys['byr']) <= 2002):
            continue
        if not keys['iyr'].isdigit():
            continue
        if not (2010 <= int(keys['iyr']) <= 2020):
            continue
        if not keys['eyr'].isdigit():
            continue
        if not (2020 <= int(keys['eyr']) <= 2030):
            continue
        if not keys['pid'].isdigit():
            continue
        if not len(keys['pid']) == 9:
            continue
        if not keys['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            continue
        if not keys['hcl'].startswith('#') or not len(keys['hcl']) == 7:
            continue
        if not (keys['hcl'][1:].isalnum()):
            continue
        if keys['hgt'][-2:] not in {'cm', 'in'}:
            continue
        if not keys['hgt'][:-2].isdigit():
            continue
        if keys['hgt'].endswith('cm') and not (150 <= int(keys['hgt'][:-2]) <= 193):
            continue
        if keys['hgt'].endswith('in') and not (59 <= int(keys['hgt'][:-2]) <= 76):
            continue
    return 1


print("list size: {0}".format(str(len(lList))))
print("list: [0]: {0}".format(str(lList[0])))
part1(lList)
part2(lList)

# print ("\n** Solution **")
# data= open("day4.lst", 'r').read()
# print(f'part1 sol: {part1sol(data)}')
# print(f'part2 sol: {part2sol(data)}')
# part2(lList)

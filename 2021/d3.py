#!/usr/bin/python3
# AdventCode Day 1

import time

# install requirements
# python3 -m venv advent
# source advent/bin/activate
# python3 -m pip install time
#
debug = False
#debug = True
input_list_sample = open("d3_sample.lst").read().splitlines()
input_list = open("d3.lst").read().splitlines()


# with open('d2.lst', 'r') as f:
# lValues = [int(x) for x in f]
# for line in f:
#    lValues.append(int(line.strip()))


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))
        return ret

    return wrap


@timing
def step1(input):
    """
    gamma: most common bit
    epsilon: least common bit
    gamma * epsilon
    :return:
    """
    arr = get_transposed_arr(input)

    g = []
    e = []
    for newline in arr:
        # most common bit = gamma
        g += "1" if newline.count("1") > newline.count("0") else "0"
        e += "1" if newline.count("1") < newline.count("0") else "0"
    cg = "".join(g)
    ce = "".join(e)
    print(
        f'step1: arr len: {len(arr)}, joined g: {cg}, int g: {int(cg, 2)}, joined e: {ce}, int e: {int(ce, 2)}, g*e: {int(ce, 2) * int(cg, 2)}')


def get_transposed_arr(input):
    input_size = len(input)
    unit_size = len(input[0])
    transposed_arr = [''] * unit_size
    if debug:
        print(f'L: {input_size}, l: {unit_size}, {input[0]}')
    for line in input:
        for idx, s in enumerate(line):
            transposed_arr[idx] = str(transposed_arr[idx]) + "" + s
    if debug:
        print(transposed_arr)
    return transposed_arr


def getOxygen(input):
    most_arr = input.copy()
    bits = len(input[0])
    for bit in range(bits):
        transposed_array = get_transposed_arr(most_arr)
        most_bits = "1" if transposed_array[bit].count("1") > transposed_array[bit].count("0") else "0"
        if transposed_array[bit].count("1") == transposed_array[bit].count("0"):
            most_bits = "1"
        if debug:
            print(f'oxygen bit:  {bit}, most: {most_bits}')
        temp_arr = []
        if len(most_arr) == 1:
            if debug:
                print(f'oxygen: last value: {most_arr[0]}, bit: {bit}')
            return most_arr[0]
        for el in most_arr:
            if el[bit] == most_bits:
                temp_arr.append(el)
                if debug:
                    print(f'oxygen: add value: {el}, bit: {bit}')
        most_arr = temp_arr.copy()
    return most_arr[0]


def getCo2(input):
    least_arr = input.copy()
    bits = len(input[0])
    for bit in range(bits):
        transposed_array = get_transposed_arr(least_arr)
        least_bits = "1" if transposed_array[bit].count("0") > transposed_array[bit].count("1") else "0"
        if transposed_array[bit].count("1") == transposed_array[bit].count("0"):
            least_bits = "0"
        temp_arr = []
        if debug:
            print(f'co2 len: {len(least_arr)}, least arr: {least_arr}')
        if len(least_arr) == 1:
            if debug:
                print(f'co2: last value: {least_arr[0]}, bit: {bit}, ')
            return least_arr[0]
        for el in least_arr:
            if el[bit] == least_bits:
                temp_arr.append(el)
                if debug:
                    print(f'co2: add value: {el}, bit: {bit}')
        least_arr = temp_arr.copy()
    return least_arr[0]


@timing
def step2(input):
    """
    O2: keep numbers with most bits
    co2: keep numbers with less bits
    :return:
    """
    oxygen = getOxygen(input)
    co2 = getCo2(input)
    ioxygen = int(oxygen, 2)
    ico2 = int(co2, 2)
    res = ioxygen * ico2
    print(f'step2: oxygene: {oxygen}, int o2: {ioxygen}, co2: {co2}, int co2: {ico2}, res: {res}')
    # print(f"nb values: {len(input_list)}, result: h: {totalh}, z: {totalz}, a: {totala} {totalz * totalh}")


# 198
print("step1: sample list")
step1(input_list_sample)
# 3633500
print("step1: puzzle list")
step1(input_list)

# 23 10 = 230
print("step2: sample list")
step2(input_list_sample)
# 1327x3429 = 4550283
print("step2: list")
step2(input_list)

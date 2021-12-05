#!/usr/bin/python3
# AdventCode Day 1

import time

# install requirements
# python3 -m venv advent
# source advent/bin/activate
# python3 -m pip install time

lValues = []

#
debug = False
#debug = True
# input_list_sample = open("day8_sample.lst").read().splitlines()
# input_list = open("day1.lst").read().splitlines()

with open('d1.lst', 'r') as f:
    lValues = [int(x) for x in f]
    # for line in f:
    #   lValues.append( int( line.strip() ) )


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))
        return ret
    return wrap


@timing
def step1():
    larger = 0
    for idx in range(0, len(lValues) - 1):
        if lValues[idx + 1] - lValues[idx] > 0:
            larger += 1
    print(f"nb values: {len(lValues)}, Augmentations: {larger}")

def larger(values):
    incr=0
    for idx in range(0,len(values)-1):
        if values[idx+1]>values[idx]:
            incr+=1
    return incr

@timing
def step11():
    print(f"step 1: nb: {len(lValues)},{larger(lValues)}")


def sum_windows(x):
    if x >= 0 and x <= len(lValues):
        return lValues[x] + lValues[x + 1] + lValues[x + 2]

def get_new_values(values):
    new_puzzle=[]
    for idx in range(0,len(values)-2):
        new_puzzle.append(sum(values[idx:idx+3]))
    return new_puzzle

@timing
def step2():
    increased = 0
    new_puzzle=get_new_values(lValues)
    #print(f'{new_puzzle}')
    increased+=larger(new_puzzle)
    print(f"step2: nb values: {len(new_puzzle)}, Augmentations: {increased}")


# 1709
step1()
step11()
# 1761
step2()
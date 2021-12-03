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
# debug = True
# input_list_sample = open("day8_sample.lst").read().splitlines()
input_list = open("d2.lst").read().splitlines()

#with open('d2.lst', 'r') as f:
    # lValues = [int(x) for x in f]
    #for line in f:
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
def step1():
    totalh = 0
    totalz = 0
    for fcmd in input_list:
        #print(f'{fcmd}')
        (h,z)=cmdToVal(fcmd)
        totalh+=h
        totalz+=z

    print(f"nb values: {len(input_list)}, result: {totalh}, {totalz}, {totalz*totalh}")


def cmdToVal(fullcmd):
    """"
    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.
    """
    delta_hor = 0
    delta_depth = 0
    (cmd, val) = fullcmd.split(" ")
    if cmd == "forward":
        delta_hor=int(val)
    if cmd == "up":
        delta_depth=-int(val)
    if cmd == "down":
        delta_depth=int(val)
    #print(f'cmd: {cmd}, val: {val}, h: {delta_hor}, z: {delta_depth}')

    return (delta_hor,delta_depth)

# 1451210346
def cmdToVal2(fullcmd,aim):
    """
    compute from full command modification of horizontal and depth.
    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.
    :param fullcmd:
    :return: +or - horizontal units, + or - depth units
    """
    delta_hor = 0
    delta_depth = 0
    delta_aim = 0
    (cmd, val) = fullcmd.split(" ")
    if cmd == "forward":
        delta_hor=int(val)
        delta_depth=aim*int(val)
    if cmd == "up":
        #delta_depth=-int(val)
        delta_aim=-int(val)
    if cmd == "down":
        #delta_depth=int(val)
        delta_aim=int(val)
    print(f'cmd: {cmd}, val: {val}, aim: {aim}, h: {delta_hor}, z: {delta_depth}, a: {delta_aim}')

    return (delta_hor,delta_depth, delta_aim)


@timing
def step2():
    totalh = 0
    totalz = 0
    totala = 0
    for fcmd in input_list:
        #print(f'{fcmd}')
        (h,z,a)=cmdToVal2(fcmd,totala)
        totalh+=h
        totalz+=z
        totala+=a


    print(f"nb values: {len(input_list)}, result: h: {totalh}, z: {totalz}, a: {totala} {totalz*totalh}")
# 1250395
step1()

# 1761
step2()

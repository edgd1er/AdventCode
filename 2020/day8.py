# AdventCode Day 1
import time

debug = False
input_list_sample = open("day8_sample.lst").read().splitlines()
input_list = open("day8.lst").read().splitlines()


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))
        return ret

    return wrap


def fill_dic_with(input_list):
    cmds = dict()
    i = 0
    for line in input_list:
        cmd, oper = line.split(" ")
        cmds[i] = (cmd, oper)
        i += 1
    return cmds


def part1(code_env: tuple) -> tuple:
    i, cmds, acc, history = (code_env)
    print("part1: i:", i, ", cmds:", len(cmds), " acc:", acc, ", history: ", history, ", cmd: ",
          cmds[i]) if debug else ""
    if i in history:
        print("part1: infinite loop:", i, "acc:", acc)
        return 0
    if i > len(cmds): return 1
    history.append(i)
    current_cmd, current_arg = cmds[i]
    if current_cmd in ['acc', 'jmp', 'nop']:
        if current_cmd == 'nop':
            i += 1
            return part1((i, cmds, acc, history))
        if current_cmd == 'acc':
            i += 1
            acc += int(current_arg)
            return part1((i, cmds, acc, history))
        if current_cmd == 'jmp':
            i += int(current_arg)
            return part1((i, cmds, acc, history))
    else:
        print("Error: ", current_cmd, " arg: ", current_arg, current_cmd == 'jmp')
    # return any( == target or part1(color) for i,cmds,acc in code_env )


def run(run_cmds):
    history = set()
    idx = 0
    acc = 0
    while True:
        if idx >= len(run_cmds):
            print("finished:", history) if debug else ""
            return True, acc, idx  # normal end
        history.add(idx)
        # print("idx",idx," ,cmds:",run_cmds) if debug else ""
        print("idx", idx, " ,cmds:", run_cmds[idx]) if debug else ""
        (cmd, arg) = run_cmds[idx]
        if cmd == 'nop':
            idx += 1
        elif cmd == 'acc':
            acc += int(arg)
            idx += 1
        elif cmd == 'jmp':
            idx += int(arg)
        if idx in history:
            print("broken at:", idx, "history:", history) if debug else ""
            return None, acc, idx


@timing
def part2(cmds):
    for line_idx in range(0, len(cmds), 1):
        # wait for an acc change, all other actions are unneeded before first acc
        # print("idx:",line_idx, "new cmd: ",cmds[line_idx])
        cmd = cmds[line_idx][0]
        arg = cmds[line_idx][1]
        if cmd.startswith('acc'):
            continue
        new_cmds = cmds.copy()
        new_cmds[line_idx] = ({'jmp': 'nop', 'nop': 'jmp'}[cmd], arg)
        # print(run(new_cmds))
        finished, acc, idx = run(new_cmds)
        if finished:
            print("finished:", finished, "acc: ", acc, "idx:", idx)
            break


# Main
# part 1 sample
cmds = fill_dic_with(input_list_sample)
part1((0, cmds, 0, []))  # 5
res = run(cmds)
print("part1 sample run: loop {},acc {}".format(res[2], res[1]))

# part1: compute acc value when looping
cmds = fill_dic_with(input_list)
part1((0, cmds, 0, []))  # 1928
res = run(cmds)
print("part1 full run: loop {},acc {}\n".format(res[2], res[1]))

# part2 sample: find proper sequence by replacing 1 replace jmp -> nop or nop-> jmp once per cmds
cmds = fill_dic_with(open("day8_sample_p2.lst").read().splitlines())
part2(cmds)

# part2
cmds = fill_dic_with(open("day8.lst").read().splitlines())
part2(cmds)

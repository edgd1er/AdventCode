# AdventCode Day 1
import time

lList = []
groups_answers = []
tmp = ""

input_list = open("day6.lst").readlines()

for line in input_list:
    if line != "\n":
        tmp += line
    else:
        lList.append(tmp.strip())
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


def get_unique(group_answers):
    answers = []
    # print(group_answers)
    for answer in group_answers:
        # print(answer)
        answers += [char for char in answer if not char in answers and char.isalpha() and char != "\n"]

    return {"nb": len(answers), "answers": answers}


def get_groups(groups, part):
    res = []
    idx = 0
    # new_groups = [group for group in groups.split("\n\n")]
    for ngroup in groups:
        g_res = get_unique(ngroup) if part == 1 else get_common(ngroup)
        # print(" group:", ngroup.replace('\n', ','), "group res:", g_res)
        res.append(g_res)
        idx += 1
    return res


def get_total(reps):
    total = 0
    # print(reps)
    for rep in reps:
        # print(rep)
        total += rep['nb']
    return total


@timing
def part1(to_decode):
    start_time = time.time()
    reps = get_groups(to_decode, 1)
    total = get_total(reps)
    # print("len reps: ", len(reps), "total: ", total, "reps:", reps)
    print("part1: nb groups: {}, count yes answer: {}, time {} seconds".format(len(reps), total,
                                                                               time.time() - start_time))


@timing
def part2(to_decode):
    start_time = time.time()
    res = get_groups(to_decode, 2)
    total = sum(my_res['nb'] for my_res in res)
    print("part2: nb groups: {}, common yes: {}, time: {} seconds".format(len(res), total, time.time() - start_time))


def get_common(ngroup):
    group_answers = []
    answers_by_person = ngroup.split('\n')
    for answers in answers_by_person:
        group_answers.append([char for char in answers])

    if len(group_answers) == 1:
        all_answered = set(group_answers[0]).intersection(group_answers[0])
    else:
        all_answered = set(group_answers[0]).intersection(*group_answers[1:])
    # print("\nby person: ", answers_by_person, ", split answer by person: ", group_answers, ", all: ", all_answered)

    # print("common answers: {}, details: {}, by person: {}".format(len(all_answered), all_answered, answers_by_person))
    return {'nb': len(all_answered), "answers": all_answered}


print("checks")
# 6 yes a b c x y z = 1 group
to_decode = "abcx\nabcy\nabcz"
rep = [get_unique(to_decode)]

print("expected 1 group, 6 yes, curreent: group: {}, rep: {}, details: {}".format(len(rep), get_total(rep), rep))

# This list represents answers from five groups:
# The first group contains one person who answered "yes" to 3 questions: a, b, and c.
#    The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
#    The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
#    The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
#    The last group contains one person who answered "yes" to only 1 question, b.
#    In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.
inp = ['abc', 'a\nb\nc', 'ab\nac\n', 'a\na\na\na', 'b']
reps = get_groups(inp, 1)
# print("Expected 5 groups, 3,3,3,1,1 = 11 yes, current group: {}, yes: {}, details: {}".format(len(reps),get_total(reps), reps))
print(
    "Expected 5 groups, 3,3,3,1,1 = 11 yes, current group: {}, yes: {}, details: {}".format(len(reps), get_total(reps),
                                                                                            0))

print("list size: {0}".format(str(len(lList))))
part1(lList)  # 6351
print("\n ********************** \n")
# 3 + 0 + 1 + 1 + 1 = 6
inp = ['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b']
res = get_groups(inp, 2)
total = sum(my_res['nb'] for my_res in res)
print("Expected 5 groups, 6 common yes, nb groups: {}, common yes: {}".format(len(res), total))
part2(lList)  # 3143
quit()

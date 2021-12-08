from functools import reduce
import math


def gen_sig_set(lines, sig):
    sums = [0] * (len(lines[0]))
    final_msig = [0] * (len(lines[0]))

    for line in lines:
        for iter in range(len(line)):
            sums[iter] += int(line[iter])
    for iter in range(len(sums)):
        if sums[iter] < math.ceil(len(lines) / 2.0):
            final_msig[iter] = 0
        else:
            final_msig[iter] = 1
    return [int(not x) for x in final_msig] if sig == 0 else final_msig


def fn_filter(lines, sig):
    line_length = len(lines[0])
    for iter in range(line_length):
        print(len(lines))
        print(len(lines))
        lines = list(filter(lambda x: int(x[iter]) == int(
            gen_sig_set(lines, sig)[iter]), lines))
        if len(lines) <= 1:
            return lines


with open('/home/dreeko/PROJECT/aoc2021/day3/input.txt', 'r') as f:
    lines = [list(x.replace('\n', '')) for x in f.readlines()]
    msig, lsig = [0, 0]
    msig = int('0b'+''.join([str(x) for x in fn_filter(lines, 1)[0]]), 2)
    lsig = int('0b'+''.join([str(x) for x in fn_filter(lines, 0)[0]]), 2)
print(msig, ' ', lsig, msig * lsig)

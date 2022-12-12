import functools as fun
with open('/home/dreeko/PROJECT/aoc2021/day1/input.txt', 'r') as f:
    prev = [9999999999999, 9999999999999, 9999999999999]
    tally = 0
    lines = f.readlines()
    for iter in range(len(lines) - 1):
        curr = [0] * 3
        curr[0] = int(lines[iter])
        curr[1] = 0 if iter+1 > len(lines) - 1 else int(lines[iter+1])
        curr[2] = 0 if iter+2 > len(lines) - 1 else int(lines[iter+2])
        if sum(curr) > sum(prev):
            tally += 1
        prev = curr
print(tally)
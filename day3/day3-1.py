import math
with open('/home/dreeko/PROJECT/aoc2021/day3/input.txt', 'r') as f:
    lines = f.readlines()
    sums = [0] * (len(lines[0]) - 1)
    final_msig = [0] * (len(lines[0]) - 1)  # minus newline
    for line in lines:
        for iter in range(len(line)-1):
            sums[iter] += int(line[iter])
    for iter in range(len(sums)):
        if sums[iter] < math.ceil(len(lines) / 2.0):
            final_msig[iter] = 0
        else:
            final_msig[iter] = 1
        msig_str = '0b' + ''.join([str(x) for x in final_msig])
        msig_int = int(msig_str, 2)
        lsig_str = '0b' + ''.join([str(int(not x)) for x in final_msig])
        lsig_int = int(lsig_str, 2)
print(
f"""msig b: {msig_str} 
msig int: {msig_int}, 
lsig b: {lsig_str} 
lsig int: {lsig_int}
product: {msig_int * lsig_int}""")
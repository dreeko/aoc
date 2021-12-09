#import numpy as np
#np. set_printoptions(threshold=np. inf)
field = [[0 for i in range(1000)] for j in range(1000)]
tally = 0
with open('/home/dreeko/PROJECT/aoc2021/day5/input.txt', 'r') as f:
    for line in f:
        start, end = line.replace('\n', '').split(' -> ')
        x1, y1 = int(start.split(',')[0]), int(start.split(',')[1])
        x2, y2 = int(end.split(',')[0]), int(end.split(',')[1])
        if not (x1 == x2 or y1 == y2):
            continue
        for i in range(min(x1, x2), max(x1, x2) + 1):
            for j in range(min(y1, y2), max(y1, y2) + 1):
                field[i][j] += 1
                if field[i][j] == 2:
                    tally += 1
print(tally)
# mat = np.matrix(field)
# with open('outfile.txt', 'wb') as f:
#     for line in mat:
#         np.savetxt(f, line, fmt='%d')

# and (int(field[i - 1][j]) > 0 and int(field[i][j-1]) > 0) \
#         or (int(field[i + 1][j]) > 0 and int(field[i][j+1]) > 0):

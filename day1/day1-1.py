with open('./input.txt', 'r') as f:
    prev = 9999999999999
    curr = 0
    tally = 0
    for line in f:
        curr = int(line)
        if (curr > prev):
            tally += 1
        prev = curr
print(tally)
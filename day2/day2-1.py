with open('/home/dreeko/PROJECT/aoc2021/day2/input.txt', 'r') as f:
    hor = 0
    vert = 0
    for line in f:
        command, amt = line.split(' ', 2)
        if(command == 'forward'):
            hor += int(amt)
        if(command == 'up'):
            vert -= int(amt)
        if (command == 'down'):
            vert += int(amt)
print(f"hor: {hor}, vert: {vert}, product: {hor * vert}")

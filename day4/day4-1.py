import re
def fn_build_board():
    boards = []
    with open('/home/dreeko/PROJECT/aoc2021/day4/input.txt', 'r') as f:
        input_lines = list(filter(lambda x: not x[0] == '\n', f.readlines()))

    lines = [re.split("[ ]+", re.sub("[\n]|^ ", "", x)) for x in input_lines]
    random_draws = input_lines[0]
    lines = lines[1:]  # get rid of random draw line
    iter = 0
    while iter < len(lines):
        board = [[0] * 5] * 5
        for i in range(0, 5):
            board[i] = lines[iter+i]
        iter += 5
        boards.append(board)
    return boards, [[[0] * 5] * 5 ] * len(boards), random_draws

board, marked, draws = fn_build_board()

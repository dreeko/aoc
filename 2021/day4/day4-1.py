import re

def fn_build_board():
    boards = []
    with open('/home/dreeko/PERSONAl/aoc2021/day4/input.txt', 'r') as f:
        input_lines = list(filter(lambda x: not x[0] == '\n', f.readlines()))
    random_draws = input_lines[0].replace('\n', '').split(',')
    lines = input_lines[1:]  # get rid of random draw line
    lines = [re.split("[ ]+", re.sub("[\n]|^ ", "", x)) for x in lines]
    iter = 0
    while iter < len(lines):
        board = [[0 for i in range(5)] for j in range(5)]
        for i in range(0, 5):
            board[i] = lines[iter+i]
        iter += 5
        boards.append(board)
    return boards, random_draws


def fn_check_complete(marked, row, col):
    return all((marked[row][0], marked[row][1], marked[row][2], marked[row][3], marked[row][4])) or \
        all((marked[0][col], marked[1][col], marked[2]
             [col], marked[3][col], marked[4][col]))


def fn_search_and_mark(board, draws, min_complete):
    marked = [[False for i in range(5)] for j in range(5)]
    completed_in = 0
    for draw in draws:
        completed_in += 1
        if completed_in >= min_complete:
            return 100, board, marked, draws[-1]
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == draw:
                    marked[i][j] = True
                    if fn_check_complete(marked, i, j):
                        return completed_in, board, marked, draws[completed_in]
    return 100, board, marked, draws[-1]


boards, draws = fn_build_board()
completions = []
min_complete = 9999
for iter in range(0, len(boards)):
    completed_in, board, marked_mat, last_draw = fn_search_and_mark(boards[iter], draws, min_complete)
    completions.append([completed_in, board, marked_mat, last_draw])
    min_complete, idx = [completed_in, iter] if completed_in < min_complete else [min_complete, idx]
sum_unmarked = 0
for i in range(len(completions[idx][1])):
    for j in range(len(completions[idx][1][0])):
        sum_unmarked += int(completions[idx][1][i][j]) if (not completions[idx][2][i][j]) else 0

last_draw = draws[min_complete-1]
product = int(sum_unmarked * int(last_draw))
print(
    f"last draw: {last_draw}\nsum of unmarked: {sum_unmarked}\nproduct: {product}")
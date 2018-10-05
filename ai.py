import copy, time, random
from end import win_in_game, field_cut, empty_or_draw

def ai_move(answ):
    field = copy.deepcopy(answ[0])

    # recursion depth
    depth = len(empty_cells(field))

    # cell selection if first move
    if depth==len(field)**2:
        print('пустое поле')
        sec = [0, len(field)-1]
        x = random.choice(sec)
        y = random.choice(sec)
        field[x][y] = 1
        return [field, 1, answ[2]]
    # cell selection, if the difficulty is easy and the field is 3x3
    elif answ[2]==0 and len(field)==3:
        print('лёгкая игра 3х3')
        cell = random.choice(empty_cells(field))
        x, y = cell[0], cell[1]
        field[x][y] = 1
        return [field, 1, answ[2]]
    # cell selection if complexity is easy and 4x4 field
    elif answ[2]==0 and depth > 9:
        print('лёгкая игра 4x4', depth)
        depth = 3
    # cell selection if complexity is normal and 4x4 field
    elif answ[2]==1 and depth > 9:
        print('сложная игра 4x4', depth)
        depth = 5
        
    s_time = time.clock()
    # best move for ai
    best = minimax(field, depth, 1)
    print(time.clock()-s_time, 'sec время BEST')
    # replacement of the value of the selected cell (move ai)
    x, y = best[0], best[1]
    field[x][y] = 1
    
    return [field, 1, answ[2]]

# list of empty cells available moves
def empty_cells(field):
    cells = []
    for x, row in enumerate(field):
        for y, cell in enumerate(row):
            if cell == 0: cells.append([x, y])
    return cells

# cell value estimate
def evaluate(field):
    win_row = field_cut(field)
    if win_in_game(win_row, len(field)) == 1:
        value = -1
    elif win_in_game(win_row, len(field)) == 0:
        value = +1
    else:
        value = 0
    return value

def minimax(field, depth, player):

    ai, hu = 1, -1

    # determining the best move
    if player == ai:
        best = [None, None, -999]
    else:
        best = [None, None, 999]

    # check for the end of the game if draw
    if depth==0 or empty_or_draw(field):
        
        value = evaluate(field)
        return [None, None, value]

    for cell in empty_cells(field):
        # coordinates of an empty cell
        x, y = cell[0], cell[1]

        # presumptive move
        field[x][y] = player

        # state of winning lines after the move
        win_row = field_cut(field)

        # win check
        if win_in_game(win_row, len(field)) == 1:
            score = [x, y, -1]
        elif win_in_game(win_row, len(field)) == 0:
            score = [x, y, 1]
        else:
            score = minimax(field, depth-1, -player)

        # zeroing the cell after hypothetical moves
        field[x][y] = 0

        score[0], score[1] = x, y

        # pre-best run recording
        if player == ai:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best

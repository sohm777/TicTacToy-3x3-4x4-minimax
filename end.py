'''Checking the end of the game and determining the winner'''

def check_end(field):
    # winner text
    winner = ['You lose!',
              'You won!',
              'Draw']
    
    # "winner" variable
    l = len(field)
    win_row = field_cut(field)
    zinner = win_in_game(win_row, l)
    
    if zinner == 0:
        # the AI won
        return winner[0], True
    elif zinner == 1:
        # the player won
        return winner[1], True
    else:
        if empty_or_draw(field):
            # draw
            return winner[2], True
        else:
            # The game continues
            return None, False

# dictionary of values of the winning lines of the playing field
def field_cut(field):
    l = len(field)
    
    # number of winning decisions
    w = l*2 + 2
    
    win_row = {a:[] for a in range(w)}
    
    j = 0
    for x in range(l):
        for y in range(l):
            win_row[x].append(field[x][y])
            win_row[x+l].append(field[y][x])
            if x == y:
                win_row[l*2].append(field[x][y])
            if x == j and y == (l-1)-j:
                win_row[l*2+1].append(field[x][y])
        j += 1

    return win_row

# win check
def win_in_game(win_row, l):
    # winning line
    ai, hu = [], []
    for m in range(l):
        ai.append(1)
        hu.append(-1)
    for n in range(len(win_row)):
        if win_row[n] == ai:
            return 0
        elif win_row[n] == hu:
            return 1
    return -1

# check for empty cells, for a draw
def empty_or_draw(field):
    i = 0
    for row in field:
        for value in row:
            if value == 0:
                i += 1
    if i == 0:
        # no empty cells - draw
        return 1
    else:
        # there are empty cells - THE GAME CONTINUES
        return 0

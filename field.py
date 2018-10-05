'''construction of the playing field, the main functions of the game'''

# answ = [0.playing field, 1.first move, 2.difficulty]

import time
from tkinter import *
from ai import ai_move
from end import check_end

# checking the turn
def check_move(parent, answ):
    if answ[1] == 0:
        s_time = time.clock()
        answ = ai_move(answ)
        z = 0
        for x in range(len(answ[0])):
            for y in range(len(answ[0])):
                z += 1
                one_AI_Btn(parent, x, y, z, answ)
        end_text, check = check_end(answ[0])
        if check:
            end_game(parent, answ[0], end_text)
    else:
        for x in range(len(answ[0])):
            for y in range(len(answ[0])):
                one_PLR_Btn(parent, x, y, answ)

# one cell of the playing field AI
def one_AI_Btn(parent, x, y, z, answ):
    frame = Frame(parent)
    frame.config(padx=5, pady=5, bg='black')
    btn = Button(frame, bg='silver')
    play_field = answ[0]

    # single cell drawing
    cell(play_field[x][y], btn)
    
    if z == (len(answ[0]))**2:
        check_move(parent, answ)
    btn.grid()
    frame.grid(row=x, column=y)

# one cell of the playing field PLAYER
def one_PLR_Btn(parent, x, y, answ):
    frame = Frame(parent)
    frame.config(padx=5, pady=5, bg='black')
    btn = Button(frame, bg='silver')
    play_field = answ[0]

    # single cell drawing
    cell(play_field[x][y], btn)

    btn.config(command=lambda:clickBtn(btn, x, y, answ, parent, frame))    
    btn.grid()
    frame.grid(row=x, column=y)

# click on the cell field
def clickBtn(btn, x, y, answ, parent, frame):
    field = answ[0]
    # change cell value to X
    field[x][y] = -1
    # pass transfer AI
    answ[1] = 0

    end_text, check = check_end(field)
    if check:
        btn.config(text='X', width=3, height=1,
                   font='Times, 40', state=DISABLED)
        btn.grid()
        frame.grid(row=x, column=y)
        print('КОНЕЦ ПО КЛИКУ!!! clickBtn')
        end_game(parent, field, end_text)
    else:
        print('x, y игрока ', x, y)
        check_move(parent, answ)

# отрисовка одной ячейки
def cell(one_cell, btn):
    if one_cell == 0:
        btn.config(text=' ', width=3, height=1,
                   font='Times, 40')
    elif one_cell == 1:
        btn.config(text='O', width=3, height=1,
                   font='Times, 40', state=DISABLED)
    elif one_cell == -1:
        btn.config(text='X', width=3, height=1,
                   font='Times, 40', state=DISABLED)
    

# tablet - the end of the game
def end_game(parent, field, end_text):
    frame = Frame(parent)
    frame.config(padx=5, pady=5, bg='black')
    frame.grid(row=0, column=0, columnspan=len(field),
               rowspan=len(field))
    label = Label(frame, text=end_text)
    label.config(font='Times, 20')
    label.grid(row=0, column=0)

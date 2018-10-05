'''basic game settings, player questions'''

import random
from tkinter import Frame, Button, Label, IntVar, Radiobutton

# field size
cells = {'3x3': 3,
        '4x4': 4}

# first move
first_move = {'computer': 0,
              'player': 1,}

# difficulty
difficulty = {'I want to win!': 0,
              'I want to strain!': 1}

answers = []

'''separate window,
questions to the player at the beginning of the game'''
def startQuest(parent):
    # field size selection
    frame_1 = Frame(parent)
    frame_1.config(padx=20, pady=10)
    frame_1.grid(row=0, column=0)
    label_1 = Label(frame_1, text='Choose field size')
    label_1.config(font='Times, 14')
    label_1.grid(row=0, column=0, columnspan=2)
    var_1 = IntVar()
    var_1.set(3)
    col_1 = 0
    for key in cells:
        rad = Radiobutton(frame_1, text=key,
                          variable=var_1, value=cells[key])
        rad.config(font='Times, 12')
        rad.grid(row=1, column=col_1)
        col_1 += 1
        
    # first turn selection
    frame_2 = Frame(parent)
    frame_2.config(padx=20, pady=10)
    frame_2.grid(row=1, column=0)
    label_2 = Label(frame_2, text='Who makes the first move?')
    label_2.config(font='Times, 14')
    label_2.grid(row=0, column=0, columnspan=2)
    var_2 = IntVar()
    var_2.set(0)
    col_2 = 0
    for key in first_move:
        f_movie = Radiobutton(frame_2, text=key, variable=var_2,
                              value=first_move[key])
        f_movie.config(font='Times, 12')
        f_movie.grid(row=1, column=col_2)
        col_2 += 1

    # choice of difficulty
    frame_3 = Frame(parent)
    frame_3.config(padx=20, pady=10)
    frame_3.grid(row=2, column=0)
    label_3 = Label(frame_3, text='Choose the difficulty of the game')
    label_3.config(font='Times, 14')
    label_3.grid(row=0, column=0, columnspan=2)
    var_3 = IntVar()
    var_3.set(0)
    col_3 = 0
    for key in difficulty:
        diff = Radiobutton(frame_3, text=key, variable=var_3,
                           value=difficulty[key])
        diff.config(font='Times, 12')
        diff.grid(row=1, column=col_3)
        col_3 += 1

    # data return button
    frame_4 = Frame(parent)
    frame_4.config(padx=20, pady=10)
    frame_4.grid(row=3, column=0)
    btn = Button(frame_4)
    btn = Button(frame_4, command=parent.destroy)
    btn.config(bg='silver', text='Accept',
               font='Times, 10')
    btn.grid(row=0, column=0)

    # focus on dialogue, waiting for the window to close
    parent.focus_set()
    parent.grab_set()
    parent.wait_window()
        
    # building a game array
    play_array = [[0 for x in range(var_1.get())]
                  for y in range(var_1.get())]

    answers.append(play_array)
    
    # choosing the first move randomly
    if var_2.get() == 2:
        f_move = random.choice([0, 1])
        print ('f_move', f_move)
        answers.append(f_move)
    else:
        answers.append(var_2.get())

    answers.append(var_3.get())

    return answers

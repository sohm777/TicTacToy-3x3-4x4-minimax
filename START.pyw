'''The main window of the game that runs the file'''

import sys
import os
from tkinter import Tk, Frame, Button, Toplevel
from settings import startQuest
from field import check_move

def start():
    
    root = Tk()
    root.title('Tic Tac Toy')
    root.iconbitmap('ttt.ico')
    # hide root window
    root.withdraw()
    # prohibit the expansion of the game window
    root.resizable(width=False, height=False)

    # questions to the player
    win = Toplevel(root)
    win.title('question')
    win.iconbitmap('ttt.ico')
    win.resizable(width=False, height=False)
    answers = startQuest(win)
    print('answers', answers)

    # playing field
    play_box = Frame(root)

    # return the root window
    root.deiconify()

    check_move(play_box, answers)
    play_box.grid(columnspan=2)

    # bottom menu - footer
    n_game = Frame(root, bd=5)
    new = Button(n_game, text="New game",
                 command=lambda:restart(root))
    new.config(bg='silver', font='Times, 14')
    new.grid(row=0, column=0)
    n_game.grid(row=1, column=0)

    e_game = Frame(root, bd=5)
    exit_game = Button(e_game, text="Exit",
                       command=lambda:exit(root))
    exit_game.config(bg='silver', font='Times, 14')
    exit_game.grid(row=0, column=1)
    e_game.grid(row=1, column=1)

    root.mainloop()

if __name__ == '__main__':
    def exit(root):
        root.destroy()
    
    def restart(root):
        root.destroy()
        start()

    start()

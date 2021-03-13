import time
import random
import functools
import tkinter as tk
from tkinter import messagebox

SQUARE_LENGTH = 4
buttons = [None] * (SQUARE_LENGTH * SQUARE_LENGTH)

def getInd(i, j):
    return i * SQUARE_LENGTH + j

def placeButtons():
    wait_number = 1
    for i in range(SQUARE_LENGTH):
        for j in range(SQUARE_LENGTH):
            ind = getInd(i, j)
            if buttons[ind] is not None:
                buttons[ind].grid(row=i, column=j, sticky='NEWS')
                if buttons[ind]['text'] == str(wait_number):
                    wait_number += 1

    if wait_number == SQUARE_LENGTH * SQUARE_LENGTH:
        messagebox.showinfo('You won!')
        resetGame()

def resetGame():
    random.shuffle(buttons)
    placeButtons()

def clickHandler(button):
    button_i, button_j = button.grid_info()['row'], button.grid_info()['column']
    button_ind = getInd(button_i, button_j)
    dis = [-1, 1, 0, 0]
    djs = [0, 0, -1, 1]
    for d_ind in range(len(dis)):
        i = button_i + dis[d_ind]
        j = button_j + djs[d_ind]
        if i >= 0 and i < SQUARE_LENGTH and j >= 0 and j < SQUARE_LENGTH:
            ind = getInd(i, j)
            if buttons[ind] is None:
                buttons[button_ind], buttons[ind] = buttons[ind], buttons[button_ind]
                placeButtons()
                break


space = tk.Tk()
space.title('15')
topSpace = tk.Frame(space)
topSpace.grid(sticky='NEW')
botSpace = tk.Frame(space)
botSpace.grid(sticky='NEWS')

space.rowconfigure(1, weight=1)
space.columnconfigure(0, weight=1)
for i in range(2):
    topSpace.columnconfigure(i, weight=1)

for i in range(SQUARE_LENGTH):
    botSpace.rowconfigure(i, weight=1, minsize=50)
for j in range(SQUARE_LENGTH):
    botSpace.columnconfigure(j, weight=1)

newButton = tk.Button(topSpace, text='New', command=resetGame)
newButton.grid(row=0, column=0)
quitButton = tk.Button(topSpace, text='Quit', command=space.quit)
quitButton.grid(row=0, column=1)

for i in range(1, SQUARE_LENGTH * SQUARE_LENGTH):
    buttons[i] = tk.Button(botSpace, text=str(i))
    buttons[i].configure(command=functools.partial(clickHandler, buttons[i]))





resetGame()
space.mainloop()
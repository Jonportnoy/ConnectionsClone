"""
@file gui file for connections program
"""
from tkinter import ttk
from tkinter import *
from typing import Any

from src.util import sorted_dict

def button_press(btn: Button) -> Any:
    print(f'Button {btn.__getitem__('text')} pressed')

def startup(testing: bool = False):
    """
    Creates a frame for the connections game to begin
    """
    root = Tk()
    root.geometry("500x400")
    root.title("Connections Clone")
    root.grid_columnconfigure(0, weight=1, minsize=500)
    root.grid_rowconfigure(0, weight=1)
    root.propagate(True)
    frame = ttk.Frame(root, padding=(1, 1))
    frame.pack(anchor='center')

    buttons = {}
    """Dict of created buttons"""

    for x in range(1, 5):
        for y in range(1, 5):
            b = Button(frame, text=str(x + ((y - 1) * 4)), relief='raised', height=5, width=5)
            b.configure( command= lambda btn = b: button_press(btn))
            b.grid(column=x, row=y)
            buttons[x + ((y - 1) * 4)] = b

    buttons = sorted_dict(buttons) ## sorts buttons

    if not testing:
        root.mainloop()


def gui(testing: bool = False):
    startup(testing)


if __name__ == '__main__':
    gui()

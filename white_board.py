from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk


# making a basic screen, which is not resizable because otherwise there will be issues with all the draws on the board
root = Tk()
root.title("White board")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False, False)

# make the window show up
root.mainloop()

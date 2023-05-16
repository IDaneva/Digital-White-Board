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

# set an icon for the window
image_icon = PhotoImage(file= "whiteboard.png")
root.iconphoto(False, image_icon)

# set a label for the colors on the side
color_box = PhotoImage(file="color box.png")
Label(root, image=color_box, bg="#f2f3f5").place(x=10, y=20)


# make the window show up
root.mainloop()

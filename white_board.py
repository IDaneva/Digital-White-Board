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

# set the placeholder for the colors
colors = Canvas(root, bg="#ffffff", width=37, height=300, bd=0)
colors.place(x=20, y=50)

# set the colors for the palette
def display_palette():
    id = colors.create_rectangle((10, 10, 30, 30), fill="black")
    colors.tag_bind(id, "Button-1", lambda x: show_color("black"))

    id = colors.create_rectangle((10, 40, 30, 60), fill="gray")
    colors.tag_bind(id, "Button-1", lambda x: show_color("gray"))

    id = colors.create_rectangle((10, 70, 30, 90), fill="brown4")
    colors.tag_bind(id, "Button-1", lambda x: show_color("brown4"))

    id = colors.create_rectangle((10, 100, 30, 120), fill="red")
    colors.tag_bind(id, "Button-1", lambda x: show_color("red"))

    id = colors.create_rectangle((10, 130, 30, 150), fill="orange")
    colors.tag_bind(id, "Button-1", lambda x: show_color("orange"))

    id = colors.create_rectangle((10, 160, 30, 180), fill="yellow")
    colors.tag_bind(id, "Button-1", lambda x: show_color("yellow"))

    id = colors.create_rectangle((10, 190, 30, 210), fill="green")
    colors.tag_bind(id, "Button-1", lambda x: show_color("green"))

    id = colors.create_rectangle((10, 220, 30, 240), fill="blue")
    colors.tag_bind(id, "Button-1", lambda x: show_color("blue"))

    id = colors.create_rectangle((10, 250, 30, 270), fill="purple")
    colors.tag_bind(id, "Button-1", lambda x: show_color("purple"))


display_palette()


# set the eraser for the white board
eraser = PhotoImage(file="cartoon-eraser-icon-png.png")
Button(root, image=eraser, bg="#f2f3f5").place(x=20, y=400)

# set the canvas place for drawing
canvas = Canvas(root, width=930, height=500, bg="white", cursor="hand2")
canvas.place(x=100, y=10)

canvas.bind("<Button-1>", locate_xy)
canvas.bind("<B1-Motion>", addLine)


# make the window show up
root.mainloop()

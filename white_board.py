from tkinter import *
from tkinter import ttk
import tkinter as tk


# making a basic screen, which is not resizable because otherwise there will be issues with all the draws on the board
root = Tk()
root.title("White board")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False, False)

current_x = 0
current_y = 0
color = "black"


# setting the x and y coordinates to the position of the mouse
def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y


# drawing a line depending on the position of the mouse and pointer direction
def add_line(work):
    global current_x, current_y
    canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(), fill=color,
                       capstyle=ROUND, smooth=TRUE)
    current_x = work.x
    current_y = work.y


# choosing color from the palette
def show_color(new_color):
    global color
    color = new_color


# resetting the canvas space
def new_canvas():
    canvas.delete("all")
    display_palette()
    # global current_x, current_y
    # canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(), fill="white",
    #                    capstyle=ROUND, smooth=TRUE)
    # current_x = work.x
    # current_y = work.y


# set an icon for the window
image_icon = PhotoImage(file="whiteboard.png")
root.iconphoto(False, image_icon)

# set a label for the colors on the side
color_box = PhotoImage(file="color box.png")
Label(root, image=color_box, bg="#f2f3f5").place(x=10, y=20)

# set the placeholder for the colors
colors = Canvas(root, bg="#ffffff", width=37, height=300, bd=0)
colors.place(x=20, y=50)


# set the colors for the palette
def display_palette():
    color_id = colors.create_rectangle((10, 10, 30, 30), fill="black")
    colors.tag_bind(color_id, "<Button-1>", lambda x: show_color("black"))

    color_id = colors.create_rectangle((10, 40, 30, 60), fill="gray")
    colors.tag_bind(color_id, "<Button-1>", lambda x: show_color("gray"))

    color_id = colors.create_rectangle((10, 70, 30, 90), fill="brown4")
    colors.tag_bind(color_id, "<Button-1>", lambda x: show_color("brown4"))

    color_id = colors.create_rectangle((10, 100, 30, 120), fill="red")
    colors.tag_bind(color_id, "<Button-1>", lambda x: show_color("red"))

    color_id = colors.create_rectangle((10, 130, 30, 150), fill="orange")
    colors.tag_bind(color_id, "<Button-1>", lambda x: show_color("orange"))

    color_id = colors.create_rectangle((10, 160, 30, 180), fill="yellow")
    colors.tag_bind(color_id, "<Button-1>", lambda x: show_color("yellow"))

    color_id = colors.create_rectangle((10, 190, 30, 210), fill="green")
    colors.tag_bind(color_id, "<Button-1>", lambda x: show_color("green"))

    color_id = colors.create_rectangle((10, 220, 30, 240), fill="blue")
    colors.tag_bind(color_id, "<Button-1>", lambda x: show_color("blue"))

    color_id = colors.create_rectangle((10, 250, 30, 270), fill="purple")
    colors.tag_bind(color_id, "<Button-1>", lambda x: show_color("purple"))


display_palette()


# set the eraser for the whole white board aka "deleter of everything"
deleter = PhotoImage(file="trash can.png")
Button(root, image=deleter, bg="#f2f3f5", command=new_canvas).place(x=25, y=370)

eraser = PhotoImage(file="cartoon-eraser-icon-png.png")
Button(root, image=eraser, bg="#f2f3f5", command=new_canvas).place(x=22, y=425)

# set the canvas place for drawing
canvas = Canvas(root, width=930, height=500, bg="white", cursor="hand2")
canvas.place(x=100, y=10)

# set a slider for the size of the cursor and get the value of it
current_value = tk.DoubleVar()


def get_current_value():
    return f"{(current_value.get()):.2f}"


def slider_changed(event):
    value_label.configure(text=get_current_value())


slider = ttk.Scale(root, from_=0, to=10, orient="horizontal", command=slider_changed, variable=current_value)
slider.place(x=30, y=530)

# set a label for the value of the chosen size from the slider
value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)

canvas.bind("<Button-1>", locate_xy)
canvas.bind("<B1-Motion>", add_line)
canvas.bind("<<Button-2>", )


# make the window show up
root.mainloop()


# TODO: "make eraser function for the eraser button
#  currently the trash bin and the eraser delete everything on the board so there must be a new function for the eraser"

#TODO: "make a readme file for github"

# Python program to create color chooser dialog box
 
# importing tkinter module
from tkinter import *
from tkinter import colorchooser as Cc
 
def choose_color():
 
    # variable to store hexadecimal code of color
    color_code = Cc.askcolor(title ="Choose Background color")
    print(color_code)
    if color_code:
        core.configure(bg=color_code[1])
 
core = Tk()
button = Button (core, text = "Select color",
                   command = choose_color)
button.pack()
core.geometry("300x300")

core.mainloop()
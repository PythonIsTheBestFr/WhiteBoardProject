import tkinter as TK
from tkinter.colorchooser import askcolor


def to_draw(event):
    global is_drawQuestionMark, b4_x, b4_y
    is_drawQuestionMark = True
    b4_x, b4_y = event.x, event.y

def draw(event):
    global is_drawQuestionMark, b4_x, b4_y
    if is_drawQuestionMark:
        rn_x, rn_y = event.x, event.y
        canvas.create_line(b4_x, b4_y, rn_x, rn_y,fill=draw_color, width=line_width, capstyle=TK.ROUND, smooth=True)
        b4_x, b4_y = rn_x, rn_y

def not_to_draw(event):
    global is_drawQuestionMark
    is_drawQuestionMark = False


# Tkinter window making and core setup :> :) B) 8)

core = TK.Tk()
core.title("Whiteboard Prototype")

canvas = TK.Canvas(core, bg="white")
canvas.pack(fill="both", expand=True)

#program Defaults Values
line_width = 2
draw_color = 'black'
is_drawQuestionMark = False

#window size

core.geometry("800x600")

#activating the functions with keys(i googled this hehe)

canvas.bind("<Button-1>", to_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", not_to_draw)




#im gonna add some fuctions but im just gonna copy most :>

#making a jagah for all the controls like clear and clear and clear and idk more

controls_ki_jagah = TK.Frame(core)
controls_ki_jagah.pack(side="top",fill="x")

clear_button = TK.Button(controls_ki_jagah, text="Clear Canvas", command=lambda: canvas.delete("all"))
clear_button.pack(side="left", padx=5, pady=5)

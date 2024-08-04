import tkinter as TK
from tkinter.colorchooser import askcolor


#define Functions 


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

def change_color():
    global draw_color
    draw_color = askcolor()[1]
    if color: # type: ignore
        draw_color = color # type: ignore

def change_pen_thickness(somethingx):
    global line_width
    line_width = int(somethingx)

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

Colorchange_button = TK.Button(controls_ki_jagah, text="Choose Color", command=change_color)
Colorchange_button.pack(side="left", padx=5, pady=5)

line_width_ka_text=TK.Label(controls_ki_jagah, text="Line Width")
line_width_ka_scale=TK.Scale(controls_ki_jagah, from_= 1, to=15, orient="horizontal", command=lambda val: change_pen_thickness(val))

line_width_ka_text.pack(side = 'right', padx=5, pady=5)
line_width_ka_scale.pack(side = 'right', padx=5, pady=5)


core.mainloop()




import tkinter as TK
from tkinter.colorchooser import askcolor
from tkinter import colorchooser as coch
from tkinter import messagebox
from tkinter.simpledialog import askstring  # Import askstring from simpledialog

# Defining Functions 

def to_draw(event):
    global is_drawQuestionMark, b4_x, b4_y
    is_drawQuestionMark = True
    b4_x, b4_y = event.x, event.y

def draw(event):
    global is_drawQuestionMark, b4_x, b4_y
    if is_drawQuestionMark:
        rn_x, rn_y = event.x, event.y
        line = canvas.create_line(b4_x, b4_y, rn_x, rn_y, fill=draw_color, width=line_width, capstyle=TK.ROUND, joinstyle="round", smooth=True)
        b4_x, b4_y = rn_x, rn_y
        # Add the drawn line to the undo stack
        undo_stack.append(line)
        redo_stack.clear()  # Clear redo stack when a new action is taken

def not_to_draw(event):
    global is_drawQuestionMark
    is_drawQuestionMark = False

def change_color():
    global draw_color
    draw_color = askcolor()[1]
    print('Pen Color Set to', draw_color, 'hexadecimal.')

def change_pen_thickness(somethingx):
    global line_width
    line_width = int(somethingx)

def change_background_color():
    Color_Code = coch.askcolor(title='Choose a Background Color')
    print('Background Color Set to', Color_Code[1], 'hexadecimal.')
    if Color_Code:
        canvas.configure(background=Color_Code[1])

def clear_canvas():
    confirmation = messagebox.askyesno("Confirmation", "Are you Sure you want to Clear the Canvas?")
    if confirmation:
        canvas.delete('all')
        undo_stack.clear()  # Clear undo stack when canvas is cleared
        redo_stack.clear()  # Clear redo stack when canvas is cleared

# Add text entry function, but trigger via button instead of direct binding
def add_text_entry_mode():
    global text_tool_active
    text_tool_active = True
    print("Text tool activated. Click on the canvas to add text.")

def add_text_entry(event):
    global text_tool_active
    if text_tool_active:
        text = askstring("Input", "Enter text:")
        if text:
            text_id = canvas.create_text(event.x, event.y, text=text, fill=draw_color, font=("Arial", line_width * 2))
            undo_stack.append(text_id)  # Add text to undo stack
            redo_stack.clear()  # Clear redo stack when a new action is taken
        text_tool_active = False  # Deactivate the text tool after use

def undo_action():
    if undo_stack:
        last_action = undo_stack.pop()
        canvas.delete(last_action)
        redo_stack.append(last_action)  # Move the action to the redo stack

def redo_action():
    if redo_stack:
        last_undone_action = redo_stack.pop()
        # Since we're only dealing with deletions for undo/redo, there's no need to re-create the items.
        # However, you can track the parameters and re-create items if needed.
        # This setup focuses on simple delete/restore operations.
        canvas.itemconfig(last_undone_action, state='normal')
        undo_stack.append(last_undone_action)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Tkinter window setup

core = TK.Tk()
core.title("Whiteboard Prototype")
core.geometry("1000x700")

# Canvas setup
canvas = TK.Canvas(core, bg="white")
canvas.pack(fill="both", expand=True)
canvas.bind("<Button-1>", to_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", not_to_draw)

# Bind the canvas for adding text when text tool is active
canvas.bind("<Button-1>", add_text_entry, add="+")  # Note: add="+" ensures this binding doesn't overwrite others

# Program default values
line_width = 2
draw_color = 'black'
is_drawQuestionMark = False
text_tool_active = False  # Flag to track if the text tool is active
undo_stack = []  # Stack to store actions for undo
redo_stack = []  # Stack to store undone actions for redo

# Control panel
controls_ki_jagah = TK.Frame(core)

clear_button = TK.Button(controls_ki_jagah, text="Clear Canvas", command=clear_canvas)
Colorchange_button = TK.Button(controls_ki_jagah, text="Choose Color", command=change_color)
line_width_ka_text = TK.Label(controls_ki_jagah, text="Line Width:")
line_width_ka_scale = TK.Scale(controls_ki_jagah, from_=1, to=30, length=250, orient="horizontal", command=change_pen_thickness)
Background_Color_Button = TK.Button(controls_ki_jagah, text="Choose Background Color", command=change_background_color)
add_text_entry_Button = TK.Button(controls_ki_jagah, text="Add Text", command=add_text_entry_mode)
undo_button = TK.Button(controls_ki_jagah, text="Undo", command=undo_action)
redo_button = TK.Button(controls_ki_jagah, text="Redo", command=redo_action)

# Packing controls
controls_ki_jagah.pack(side="top", fill="x")
clear_button.pack(side="left", padx=5, pady=5)
Colorchange_button.pack(side="left", padx=5, pady=5)
line_width_ka_text.pack(side="right", padx=5, pady=5)
line_width_ka_scale.pack(side="right", padx=5, pady=5)
Background_Color_Button.pack(side="left", padx=5, pady=5)
add_text_entry_Button.pack(side="right", pady=5, padx=5)
undo_button.pack(side="left", padx=5, pady=5)


core.mainloop()
###I USED BEAUTIFY WEBSIDE IT LOOKS BETTER I GUESS
###
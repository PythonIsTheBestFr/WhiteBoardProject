import tkinter as TK
from tkinter.colorchooser import askcolor
from tkinter import colorchooser as coch
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import PhotoImage

# Drawing mode and default values
is_drawQuestionMark = False
is_erasing = False
eraser_thickness = 10
text_tool_active = False
line_width = 2
draw_color = 'black'

# Undo and Redo stacks
undo_stack = []
redo_stack = []


def to_draw(event):
    global is_drawQuestionMark, b4_x, b4_y
    is_drawQuestionMark = True
    b4_x, b4_y = event.x, event.y

def draw(event):
    global is_drawQuestionMark, b4_x, b4_y
    if is_drawQuestionMark:
        rn_x, rn_y = event.x, event.y
        if is_erasing:
            color = canvas['bg']
            width = eraser_thickness
        else:
            color = draw_color
            width = line_width
        
        line = canvas.create_line(
            b4_x, b4_y, rn_x, rn_y,
            fill=color, width=width, capstyle=TK.ROUND, joinstyle="round", smooth=True
        )
        undo_stack.append(('line', line, b4_x, b4_y, rn_x, rn_y, color, width))
        b4_x, b4_y = rn_x, rn_y
        redo_stack.clear()

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
    if Color_Code[1]:  # Check if a color was selected
        canvas.configure(background=Color_Code[1])
        print('Background Color Set to', Color_Code[1], 'hexadecimal.')

def clear_canvas():
    confirmation = messagebox.askyesno("Confirmation", "Are you Sure you want to Clear the Canvas?")
    if confirmation:
        canvas.delete('all')
        undo_stack.clear()
        redo_stack.clear()

def add_text_entry_mode():
    global text_tool_active
    text_tool_active = True
    print("Text tool activated. Click on the canvas to add text.")

def add_text_entry(event):
    global text_tool_active
    if text_tool_active:
        text = askstring("Input", "Enter text:")
        if text:
            font = selected_font.get()  # Get the selected font
            text_id = canvas.create_text(
                event.x, event.y,
                text=text, fill=draw_color, font=(font, int(line_width * 2))
            )
            undo_stack.append(('text', text_id, event.x, event.y, text, draw_color, font, line_width))
            redo_stack.clear()
        text_tool_active = False

def undo_action():
    if undo_stack:
        last_action = undo_stack.pop()
        if last_action[0] == 'line':
            canvas.delete(last_action[1])
        elif last_action[0] == 'text':
            canvas.delete(last_action[1])
        redo_stack.append(last_action)

def redo_action():
    if redo_stack:
        last_undone_action = redo_stack.pop()
        action_type = last_undone_action[0]
        
        if action_type == 'line':
            _, _, x1, y1, x2, y2, color, width = last_undone_action
            line = canvas.create_line(
                x1, y1, x2, y2, fill=color, width=width, capstyle=TK.ROUND, joinstyle="round", smooth=True
            )
            undo_stack.append(('line', line, x1, y1, x2, y2, color, width))
        
        elif action_type == 'text':
            _, _, x, y, text, color, font, width = last_undone_action
            text_id = canvas.create_text(
                x, y, text=text, fill=color, font=(font, width * 2)
            )
            undo_stack.append(('text', text_id, x, y, text, color, font, width))

def toggle_eraser():
    global is_erasing
    is_erasing = not is_erasing
    eraser_button.config(relief=TK.SUNKEN if is_erasing else TK.RAISED)
    print("Eraser activated." if is_erasing else "Eraser deactivated.")

def toggle_fullscreen(event=None):
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    core.attributes('-fullscreen', is_fullscreen)

def end_fullscreen(event=None):
    global is_fullscreen
    is_fullscreen = False
    core.attributes('-fullscreen', False)

def on_mouse_wheel(event):
    if event.delta > 0:
        undo_action()
    elif event.delta < 0:
        redo_action()

# Tkinter window setup
core = TK.Tk()
core.title("Whiteboard")
core.geometry("1000x700")\

# Define Fonts
fonts = ["Arial", "Courier", "Helvetica", "Times New Roman", "Verdana"]
selected_font = TK.StringVar()


# Set the icon
try:
    icon = PhotoImage(file='path_to_your_icon.png')  # Update with the correct path
    core.iconphoto(False, icon)
except TK.TclError:
    print("Icon file not found. Ensure the path to your .png file is correct.")

# Start in fullscreen mode
is_fullscreen = True
core.attributes('-fullscreen', is_fullscreen)

# Handle fullscreen toggle with the Escape key
core.bind("<Escape>", end_fullscreen)

# Handle mouse wheel for undo/redo
core.bind("<MouseWheel>", on_mouse_wheel)

# Control panel
controls_ki_jagah = TK.Frame(core)
controls_ki_jagah.pack(side="top", fill="x")

# Create buttons and controls
clear_button = TK.Button(
    controls_ki_jagah, text="Clear Canvas", command=clear_canvas
)
Colorchange_button = TK.Button(
    controls_ki_jagah, text="Choose Color", command=change_color
)
line_width_ka_text = TK.Label(
    controls_ki_jagah, text="Line Width:"
)
line_width_ka_scale = TK.Scale(
    controls_ki_jagah, from_=1, to=30, length=250, orient="horizontal",
    command=change_pen_thickness
)
Background_Color_Button = TK.Button(
    controls_ki_jagah, text="Choose Background Color", command=change_background_color
)
add_text_entry_Button = TK.Button(
    controls_ki_jagah, text="Add Text", command=add_text_entry_mode
)
eraser_button = TK.Button(
    controls_ki_jagah, text="Eraser", command=toggle_eraser
)
fullscreen_button = TK.Button(
    controls_ki_jagah, text="Toggle Fullscreen", command=toggle_fullscreen
)

# Font selection dropdown
selected_font.set(fonts[0])  # Set default font
font_menu = TK.OptionMenu(controls_ki_jagah, selected_font, *fonts)
font_menu.pack(side="left", padx=5, pady=5)

# Packing controls
clear_button.pack(side="left", padx=5, pady=5)
Colorchange_button.pack(side="left", padx=5, pady=5)
line_width_ka_text.pack(side="right", padx=5, pady=5)
line_width_ka_scale.pack(side="right", padx=5, pady=5)
Background_Color_Button.pack(side="left", padx=5, pady=5)
add_text_entry_Button.pack(side="right", pady=5, padx=5)
eraser_button.pack(side="left", padx=5, pady=5)
fullscreen_button.pack(side="left", padx=5, pady=5)

# Canvas setup
canvas = TK.Canvas(core, bg="white")
canvas.pack(fill="both", expand=True)
canvas.bind("<Button-1>", to_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", not_to_draw)
canvas.bind("<Button-1>", add_text_entry, add=True)  # Add this binding

core.mainloop()


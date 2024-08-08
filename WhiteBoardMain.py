import tkinter as TK
from tkinter.colorchooser import askcolor
from tkinter import colorchooser as coch
from tkinter import messagebox
#importing Tkinter and Askcolor fuction from it


#Defining Functions 

#Defining a Fuction to Set Draw on which Takes an Event(in this case it is mouse press m1)
#It sets is drawing var as true when mouse down
#changes before(b4) coordinates(x, y) to event.x and event.y(mouse position at point of click)
def to_draw(event):
    global is_drawQuestionMark, b4_x, b4_y
    is_drawQuestionMark = True
    b4_x, b4_y = event.x, event.y

#Definig a Fuction to Draw the acctuall line it draws the line from before x to event x (mouse click position)
#and before y to event y(mouse click position)
#then it uses create_line fuction to draw the line use color as color var and width as width var capstyle as tk.round(will try to add more later)
#and smooth = true because yes
def draw(event):
    global is_drawQuestionMark, b4_x, b4_y
    if is_drawQuestionMark:
        rn_x, rn_y = event.x, event.y
        canvas.create_line(b4_x, b4_y, rn_x, rn_y,fill=draw_color, width=line_width, capstyle=TK.ROUND,joinstyle="round", smooth=True)
        b4_x, b4_y = rn_x, rn_y

#Defining a Functiong to Stop Drawing cus after i click i dont want it to keep drawing
#not much to explain it just sets a var as false
def not_to_draw(event):
    global is_drawQuestionMark
    is_drawQuestionMark = False

#Defining a Fuction to use Tkinter's inbuilt color asked askcolor()[1]<-- the 1 means how many values in this case 1 value
def change_color():
    global draw_color
    draw_color = askcolor()[1]
    print('Pen Color Set to',draw_color[1],'hexadecimal.')

#defining a fuction to change Pen Width
def change_pen_thickness(somethingx):
    global line_width
    line_width = int(somethingx)

#Defining a Fuction to Change to change baground color
def change_background_color():

    Color_Code = coch.askcolor(title='Choose a Background Color')
    print('Background Color Set to',Color_Code[1],'hexadecimal.')
    if Color_Code:
        canvas.configure(background=Color_Code[1])

# Defining a Fuction that Clears the Screen and Asks for Confirmation
def clear_canvas():
    confirmation = messagebox.askyesno("Confirmation,","Are you Sure you want to Clear the Canvas?")
    if confirmation:
        canvas.delete('all')

# Defining a Fuction to Add Text Entry in Canvas
def add_text_entry(event):
    text = TK.askstring("Input", "Enter text:")
    if text:
        canvas.create_text(event.x, event.y, text=text, fill=draw_color, font=("Arial", line_width * 2))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Tkinter window making and core setup :> :) B) 8)

#core or master or main or else
core = TK.Tk()
core.title("Whiteboard Prototype")
core.geometry("1000x700")
secondarycore = TK.Toplevel() #<----------------------im stuck here cus idk how to use a image
secondarycore.geometry('500x500')


#making a canvas drawing area
canvas = TK.Canvas(core, bg="white")
canvas.pack(fill="both", expand=True)
#Taking Fuctions and using them
canvas.bind("<Button-1>", to_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", not_to_draw)

#program Defaults Values
line_width = 2
draw_color = 'black'
is_drawQuestionMark = False
core.configure(bg='white')
#styling and Pakaging
#making a jagah for all the controls like clear and clear and clear and idk more
controls_ki_jagah = TK.Frame(core)# frame is a thing that holds things in a line

clear_button = TK.Button(controls_ki_jagah,text="Clear Canvas", command=clear_canvas)
                        #clear button definition


Colorchange_button = TK.Button(controls_ki_jagah, 
                               text="Choose Color", 
                               command=change_color)
                               #buttan 4 colar change


line_width_ka_text=TK.Label(controls_ki_jagah, 
                            text="Line Width:")
                            # it is text that says 'Line Width:'
line_width_ka_scale=TK.Scale(controls_ki_jagah, 
                            from_= 1, to=30,
                            length=250, 
                            orient="horizontal", 
                            command=lambda val: change_pen_thickness(val))
Background_Color_Button = TK.Button(controls_ki_jagah, 
                                   text="Choose Backround Color", 
                                   command=change_background_color)
add_text_entry_Button = TK.Button(controls_ki_jagah, 
                                   text="Add Text", 
                                   command=add_text_entry)


#packing everything
controls_ki_jagah.pack(side="top",fill="x")#jagah banaraha hai

clear_button.pack(side="left", padx=5, pady=5)#clear karna ki button to pack kar raha hai

Colorchange_button.pack(side="left", padx=5, pady=5)# color change ki button to pack kar raha hai

line_width_ka_scale.pack(side = 'right', padx=5, pady=5)# line width ka Slider to pack kar raha hai

line_width_ka_text.pack(side = 'right', padx=5, pady=5)# line width ka text to pack kar raha hai

Background_Color_Button.pack(side='left', padx=5, pady=5)

add_text_entry_Button.pack(side="right", pady=5, padx=5)


core.mainloop()




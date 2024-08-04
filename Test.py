import tkinter as tk
from tkinter import messagebox

def clear_canvas():
    # Function to clear the canvas contents after confirmation
    result = messagebox.askyesno("Confirmation", "Are you Sure?")
    if result:  # If the user clicked 'Yes'
        canvas.delete("all")  # Delete all items from the canvas

# Create the main application window
root = tk.Tk()
root.title("Tkinter Canvas Clear Example")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Add some example items to the canvas (optional)
canvas.create_line(10, 10, 390, 390, fill="black", width=2)
canvas.create_oval(100, 100, 300, 300, outline="red", width=2)

# Create a Button to clear the canvas
clear_button = tk.Button(root, text="Clear Canvas", command=clear_canvas)
clear_button.pack(pady=10)

# Run the main event loop
root.mainloop()

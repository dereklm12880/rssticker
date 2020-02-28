from tkinter import *
from tkinter import ttk

# Creates tkinter window
root = Tk()

# Sets the minimum size of the root window
root.minsize(300,30) 

root.title("RSSticker")
myLabel = Label(root, text="Accio, hello world!")

# Shows tkinter window on the screen
myLabel.pack()

root.mainloop()
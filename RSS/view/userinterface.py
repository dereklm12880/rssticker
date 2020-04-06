import tkinter
import feedparser
import webbrowser
import os
import tkinter as tk
from tkinter import ttk

class RSSticker(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.style()
    
    #def size(self):
        #size = ttk.Frame(self.master, width=500, height=500)
        #size.pack()

    def style(self):
        style = ttk.Label(self.master, text = "oh man idk what i'm doing", foreground = "black", background = "white")
        style.pack()

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("RSSticker")
    app = RSSticker(master=root)
    app.mainloop()
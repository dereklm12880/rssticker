import tkinter
import feedparser
import webbrowser
import os
import tkinter as tk
from tkinter import ttk

class RSSticker(tk.Frame):
    root = tkinter.Tk()
    label = ttk.Label(root)
    cancel = ttk.Button(root)
    feed = []

    def __init__(self):
        self.loop()
    
    def loop(self):
        self.root.mainloop()
    
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
        self.popup_window = ttk.Label(master)
    
        self.build_window()
        self.pack()
    
    def start(self):
        self.master.mainloop()

    def build_window(self):
        self.popup_window.pack(side="top")

    def refresh(self, headline, link):
        print("headline:", headline, "\nlink:", link)
        self.popup_window.configure(text=headline)
        self.popup_window.configure("<Button-1>", lambda e: webbrowser.open_new(link))

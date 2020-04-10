import tkinter
import feedparser
import webbrowser
import os
import tkinter as tk
from tkinter import ttk

class RSSticker(tk.Frame):

    entry_headline = "[insert headline here]"
    entry_url = "[insert url here]"

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.build_window()
        self.start()

    def start(self):
        self.master.update()
    
    def build_window(self):
        self.master["test"] = self.entry_headline
        self.master.bind("<Button-1>", lambda e,
                        master=self.entry_url:
                        self.open_article(self.entry_url))
        self.pack()
    
    #def refresh(self):
        # will show the cycled headlines

    #def open_article(self):
        # will open the entry_url in another tab in a webbrowser

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("RSSticker")
    app = RSSticker(master=root)
    app.mainloop()